from core import SustainabilityKnowledgeBase
import os

def main():
    kb = SustainabilityKnowledgeBase()
    docs_folder = "./docs"

    # Check if we need to initialize the directory
    if kb.collection.count() == 0:
        print("🚀 Initializing Vector Database...")
        if os.path.exists(docs_folder):
            kb.ingest_directory(docs_folder)
        else:
            print(f"❌ Error: {docs_folder} directory not found.")
            return
    else:
        print(f"📚 DB already contains {kb.collection.count()} chunks. Skipping ingestion.")

    # Test Query
    query = "What are the carbon emissions projections for AI servers?"
    print(f"\n❓ Query: {query}")
    results = kb.search(query, n_results=1)
    
    if results['documents']:
        print(f"✅ Best Match from {results['metadatas'][0][0]['source']}:")
        print(f"   {results['documents'][0][0][:200]}...")

if __name__ == "__main__":
    main()