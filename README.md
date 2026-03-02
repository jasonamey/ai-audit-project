# AI Audit Project: Scholarly "Signature" Benchmarking

This project is an algorithmic auditing framework designed to evaluate how major LLM APIs represent core academic scholarship. Rather than testing simple fact retrieval, this system uses a "Signature Question" methodology to probe an AI's deep understanding of specific, complex corpora.

## Project Vision

Most AI benchmarks focus on general knowledge. This project audits **Domain-Specific Alignment**:
* **Signature Question Synthesis:** Distilling a corpus of academic PDFs into high-level questions that represent the "intellectual signature" of the source material.
* **Model Auditing:** Systematically probing different LLM APIs (OpenAI, Anthropic) with these questions to identify gaps in synthesis, hallucinations, or misalignments with the source scholarship.
* **Vector Bias Evaluation:** Investigating how different embedding strategies (OpenAI vs. Hugging Face) influence the model's ability to "see" core academic concepts during the retrieval phase.

## The Methodology: "Signature Questions"

The system identifies thematic anchors within academic papers. It then uses these anchors to generate questions to probe the major LLM APIs. 



## Project Structure

```text
ai-audit-project/
├── docs/               # Source academic PDFs (The "Audit Corpus")
├── config.py           # Infrastructure config (ChromaDB, Embedding models)
├── core.py             # Ingestion engine & Semantic search logic
├── main.py             # Audit execution and benchmarking entry point
└── test_models.py    # Testing