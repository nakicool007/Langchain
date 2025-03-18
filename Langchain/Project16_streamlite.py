import streamlit as st
import faiss
import pickle
import torch
from transformers import pipeline
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# ✅ Set Device (Enable GPU if available)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🚀 Using {DEVICE} for LLM & Embeddings")

# ✅ Load FAISS index only once (Caching)
@st.cache_resource
def load_faiss():
    with open("faiss_store_hnsw.pkl", "rb") as f:
        return pickle.load(f)

# ✅ Load Faster LLM (Optimized for Gemma-2B)
@st.cache_resource
def load_model():
    model = pipeline("text-generation", model="google/gemma-2b", device=0 if torch.cuda.is_available() else -1)
    
    # 🔥 Torch Compile for Speedup (GPU Optimized)
    if torch.cuda.is_available():
        model.model = torch.compile(model.model)
    
    return model

# ✅ Streamlit UI
st.title("📄 RAG Chatbot using Gemma-2B 🚀")
st.write("Ask any question, and I will find the answer from the uploaded PDFs.")

# ✅ Load FAISS & LLM
vector_db = load_faiss()
llm = load_model()

# ✅ User Input
query = st.text_input("🔍 Enter your question:")

if st.button("🔎 Search"):
    if query:
        with st.spinner("🔍 Searching for relevant documents..."):
            # Retrieve top 5 relevant chunks for better context
            docs = vector_db.similarity_search(query, k=5)
            retrieved_text = "\n".join([doc.page_content for doc in docs])
            
            # Construct the prompt efficiently
            prompt = f"Answer the question based on the following context:\n\n{retrieved_text}\n\nQuestion: {query}"
            
            # 🔥 Optimized LLM call
            response = llm(prompt, max_new_tokens=100, do_sample=True)

            st.success(f"**Answer:** {response[0]['generated_text']}")
    else:
        st.warning("⚠️ Please enter a question.")
