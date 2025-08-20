Langchain

This repository contains a simple, interactive application that allows you to chat with your own PDF documents. Built using the LangChain framework, this project demonstrates how to ingest, process, and query document data to create a question-answering bot.

🌟 Features
PDF Ingestion: Upload and process PDF files to build a searchable knowledge base.

Vector Store: Utilizes a ChromaDB vector store for efficient semantic search.

Conversational AI: Engage in a natural language conversation with your documents.

User-Friendly Interface: A clean and interactive user interface powered by Streamlit.

🚀 Technologies Used
LangChain: The core framework for building the application logic.

ChromaDB: A powerful vector database for storing and retrieving document embeddings.

Streamlit: For creating the interactive web application interface.

Python: The primary programming language.

🛠️ Installation and Setup
To get this project up and running on your local machine, follow these steps:

Clone the repository:

Bash

git clone https://github.com/your-username/Langchain.git
cd Langchain
Create a virtual environment (recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the dependencies:

This project uses a requirements.txt file to manage its dependencies.

Bash

pip install -r requirements.txt
📜 Usage
This project consists of two main parts: the data ingestion script and the Streamlit application.

1. Ingesting Documents
Before you can chat with your documents, you need to process them. Run the ingestion script from your terminal:

Bash

python Project16_ingest_pdf.py
This script will process any PDF files you have and store the embeddings in the chroma_db directory.

2. Running the Application
Once the documents are ingested, start the Streamlit application to begin chatting:

Bash

streamlit run Project16_streamlit.py
This command will open the application in your default web browser.

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please feel free to open an issue or submit a pull request.











Tools

