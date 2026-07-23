import numpy as np
from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "dataset.txt")
docs = open(DATA_PATH, encoding="utf-8").read().splitlines()
doc_vecs = model.encode(docs)


FAILURE_CASES = [
    {
        "case": "Ambiguous word: bank (river vs finance)",
        "reason": "Word embeddings may conflate multiple meanings",
        "improvement": "Use context-aware embeddings or domain-specific fine-tuning"
    },
    {
        "case": "Out-of-domain query",
        "reason": "Model trained on general text, struggles with specialized domains",
        "improvement": "Fine-tune model on domain-specific corpus"
    },
    {
        "case": "Very short text (1-2 words)",
        "reason": "Insufficient context for meaningful embeddings",
        "improvement": "Use query expansion or hybrid approaches"
    },
    {
        "case": "Noisy text (typos, mixed languages)",
        "reason": "Out-of-distribution inputs confuse embedding model",
        "improvement": "Apply text cleaning, normalization, or noise-resistant models"
    },
    {
        "case": "Rare words not in training data",
        "reason": "Low coverage for specialized vocabulary",
        "improvement": "Use subword tokenization (BPE) or increase training data"
    },
    {
        "case": "Sarcasm or irony",
        "reason": "Embeddings capture literal meaning, not semantic intent",
        "improvement": "Use larger models or context-aware approaches"
    },
    {
        "case": "Semantic drift over time",
        "reason": "Word meanings evolve, static embeddings become outdated",
        "improvement": "Regularly retrain or use dynamic embeddings"
    }
]


def embedding_failure_analysis(query=None):
    """
    Analyzes typical failure cases of embedding-based search.
    
    Args:
        query (str, optional): User query to analyze
        
    Returns:
        list: List of failure cases with reasons and improvements
    """
    return FAILURE_CASES
