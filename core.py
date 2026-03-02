import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import client, Config

class SustainabilityKnowledgeBase:
    def __init__(self, collection_name, embedding_func):
        """
        Initializes the Knowledge Base with a specific collection and model.
        :param collection_name: String name (e.g., 'kb_openai' or 'kb_huggingface')
        :param embedding_func: The embedding function object from config.py
        """
        # Connect to or create the specific collection in Chroma
        self.collection = client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_func,
            metadata={"hnsw:space": "cosine"}
        )

    def ingest_directory(self, directory_path):
        """
        Parses all PDFs in the directory using fitz (PyMuPDF) and 
        loads them into the vector store.
        """
        if not os.path.exists(directory_path):
            print(f"❌ Error: Directory {directory_path} does not exist.")
            return

        # 1. Discover PDF files
        pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
        
        if not pdf_files:
            print(f"⚠️ No PDF files found in {directory_path}")
            return

        print(f"📂 Found {len(pdf_files)} papers in '{directory_path}'. Starting ingestion...")

        raw_documents = []
        for filename in pdf_files:
            file_path = os.path.join(directory_path, filename)
            # PyMuPDFLoader uses fitz for high-speed academic PDF parsing
            loader = PyMuPDFLoader(file_path)
            raw_documents.extend(loader.load())
            print(f"  📄 Parsed: {filename}")

        # 2. Split into semantic chunks (Week 5, Day 2 strategy)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(raw_documents)

        # 3. Batch Add to ChromaDB
        # Using enumerate to ensure every chunk gets a unique ID
        self.collection.add(
            documents=[doc.page_content for doc in chunks],
            metadatas=[doc.metadata for doc in chunks],
            ids=[f"{doc.metadata.get('source', 'doc')}_{i}" for i, doc in enumerate(chunks)]
        )
        
        print(f"✅ Ingestion complete. {self.collection.name} now has {self.collection.count()} chunks.")

    def search(self, question, n_results=3):
        """Performs a semantic search and returns results with distance scores."""
        return self.collection.query(
            query_texts=[question], 
            n_results=n_results
        )