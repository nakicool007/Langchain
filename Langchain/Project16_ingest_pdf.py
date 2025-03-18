import os
import faiss
import pickle
import glob
import torch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS

# ✅ Set PDF directory
PDF_FOLDER = r"C:\Langchain\alldoc"

# ✅ Use GPU if available
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🚀 Using {DEVICE} for embeddings!")

# ✅ Load PDF files
def load_pdfs(pdf_folder):
    pdf_files = glob.glob(os.path.join(pdf_folder, "*.pdf"))
    docs = []
    for pdf_file in pdf_files:
        loader = PyPDFLoader(pdf_file)
        docs.extend(loader.load())
    return docs

# ✅ Split text into chunks
def split_text(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return text_splitter.split_documents(docs)

# ✅ Convert text to FAISS with HNSW Index for FAST retrieval
def create_faiss_index(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5", model_kwargs={"device": DEVICE})
    
    # Use HNSW Index for Fast Approximate Search
    vector_db = FAISS.from_documents(text_chunks, embeddings)
    index = vector_db.index

    # Convert to HNSW Index
    faiss_index = faiss.IndexHNSWFlat(index.d, 32)  # 32 is the number of neighbors
    faiss_index.hnsw.efConstruction = 64
    faiss_index.hnsw.efSearch = 32
    faiss_index.add(index.reconstruct_n(0, index.ntotal))

    vector_db.index = faiss_index
    return vector_db

if __name__ == "__main__":
    print("🔹 Loading PDFs...")
    documents = load_pdfs(PDF_FOLDER)
    
    print("🔹 Splitting text into chunks...")
    text_chunks = split_text(documents)
    
    print("🔹 Creating FAISS HNSW index for fast retrieval...")
    vector_db = create_faiss_index(text_chunks)
    
    # ✅ Save FAISS index
    faiss.write_index(vector_db.index, "faiss_index_hnsw.idx")
    
    # ✅ Save document store
    with open("faiss_store_hnsw.pkl", "wb") as f:
        pickle.dump(vector_db, f)

    print("✅ FAISS HNSW index created and saved successfully.")
