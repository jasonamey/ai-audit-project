# AI Audit Project: Signature Question RAG

This project is a specialized Retrieval-Augmented Generation (RAG) system designed to audit and collect answers from major chatbot APIs. Instead of standard "needle-in-a-haystack" queries, this system investigates the ability to synthesize **"Signature Questions"**—high-level, representative inquiries derived from the core scholarship contained within a specific corpus of academic PDFs.

## 🎯 Project Goals
* **Automated Scholarship Synthesis:** Ingest complex academic papers (PDFs) and extract thematic "signature questions."
* **Cross-API Auditing:** Use these synthesized questions to probe and compare the knowledge/alignment of major LLM APIs.
* **Retrieval Evaluation:** Compare the performance of different embedding models (OpenAI vs. Hugging Face) in identifying core academic concepts.

## 🏗️ Project Structure
```text
ai-audit-project/
├── docs/               # Source academic PDFs (Goldman Sachs, de Vries, etc.)
├── config.py           # Configuration for ChromaDB and Embedding models
├── core.py             # Logic for fitz (PyMuPDF) ingestion and vector search
├── main.py             # Entry point for DB initialization and testing
└── requirements.txt    # Project dependencies