# Implementation 5 Testing Report

- Built a mini RAG pipeline with document retrieval and answer generation.
- Used TF-IDF retrieval to select context and produced grounded answers.
- Processed 4 questions across 8 documents.

## Query Results
- Q: What does RAG combine? -> Doc 1 score=0.434
  A: Based on: RAG uses retrieval to find relevant passages before generation.
- Q: How are vector databases used? -> Doc 2 score=0.546
  A: Based on: Vector databases support efficient similarity search over embeddings.
- Q: What does FAISS help with? -> Doc 5 score=0.360
  A: Based on: FAISS enables fast approximate nearest neighbor search at scale.
- Q: How can retrieval be optimized? -> Doc 1 score=0.243
  A: Based on: RAG uses retrieval to find relevant passages before generation.
