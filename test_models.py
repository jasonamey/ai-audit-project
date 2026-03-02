from core import SustainabilityKnowledgeBase
from config import hf_ef, oai_ef

def run_test(kb, model_label, questions):
    print(f"\n{model_label}:")
    print("-" * 20)
    
    for q in questions:
        print(f"\n❓ Question: {q}")
        # Search for top 5 to see the distribution of scores
        results = kb.search(q, n_results=5)
        
        # Best match
        best_doc = results['documents'][0][0]
        best_dist = results['distances'][0][0]
        # Distance to Score conversion (for Cosine)
        best_score = 1 - best_dist 
        
        print(f"✅ Best match (score: {best_score:.4f}):")
        print(f"   Chunk 1: {best_doc[:80].strip()}...")

        print(f"\n   All scores:")
        for i, dist in enumerate(results['distances'][0]):
            score = 1 - dist
            print(f"   Chunk {i+1}: {score:.4f}")

def main():
    # 1. Initialize two separate collections
    kb_hf = SustainabilityKnowledgeBase("kb_huggingface", hf_ef)
    kb_oai = SustainabilityKnowledgeBase("kb_openai", oai_ef)

    # 2. Ingest papers into BOTH if they are empty
    for kb in [kb_hf, kb_oai]:
        if kb.collection.count() == 0:
            kb.ingest_directory("./docs")

    # 3. Define your test questions
    test_questions = [
        "What are the carbon emissions projections for AI servers?",
        "How much water do AI data centers consume?",
        "Which US states are best for sustainable AI infrastructure?"
    ]

    # 4. Run the Comparison
    run_test(kb_oai, "OPEN_AI", test_questions)
    run_test(kb_hf, "HUGGING_FACE", test_questions)

if __name__ == "__main__":
    main()