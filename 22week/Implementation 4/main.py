import json, os, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = os.path.dirname(os.path.abspath(__file__))

DOCS = [
    "Semantic retrieval uses embeddings to find passages by meaning.",
    "Ranking orders candidates by relevance to the user query.",
    "A retrieval engine compares query vectors against document vectors.",
    "Keyword search is often less robust than semantic matching.",
    "Dense retrieval improves recall for paraphrased questions.",
    "Cross-encoders provide powerful ranking signals for reranking.",
    "Bi-encoders enable fast parallel encoding of documents and queries.",
    "Retrieval augmented generation combines search with language generation.",
    "Approximate nearest neighbors reduce latency for large-scale search.",
    "Lexical and semantic signals can be combined for hybrid retrieval.",
]

def semantic_search(docs, q, k=5):
    vec = TfidfVectorizer(stop_words='english')
    M = vec.fit_transform(docs + [q])
    scores = cosine_similarity(M[:-1], M[-1]).ravel()
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return [(idx, float(score)) for idx, score in ranked[:k]]

def main():
    q = "How does semantic retrieval work?"
    results = semantic_search(DOCS, q, k=5)
    
    plt.figure(figsize=(10, 5))
    plt.bar([f"Doc {i+1}" for i, _ in results], [s for _, s in results], color=['#76B7B2', '#E15759', '#4E79A7', '#F28E2B', '#59A14F'])
    plt.ylabel('Similarity score')
    plt.xlabel('Document')
    plt.title('Semantic retrieval ranking analysis (Top-5)')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()

    json.dump({'query': q, 'documents': DOCS, 'num_docs': len(DOCS), 'retrieval_method': 'TF-IDF'}, open(os.path.join(ROOT, 'dataset.json'), 'w'), indent=2)
    json.dump({'query': q, 'top_k': 5, 'semantic_results': [{'rank': i+1, 'doc_id': idx + 1, 'score': score, 'text': DOCS[idx][:60]} for i, (idx, score) in enumerate(results)], 'total_docs': len(DOCS)}, open(os.path.join(ROOT, 'results.json'), 'w'), indent=2)
    
    report = "# Implementation 4 Testing Report\n\n- Implemented embedding retrieval using TF-IDF vectors.\n- Ranked {} documents by cosine similarity.\n- Query: \"{}\"\n\n## Top Results (Top-5)\n".format(len(DOCS), q)
    for i, (idx, score) in enumerate(results):
        report += f"- Rank {i+1}: Document {idx + 1}: score={score:.3f}\n  Text: {DOCS[idx][:70]}...\n"
    open(os.path.join(ROOT, 'report.md'), 'w').write(report)
    print('Implementation 4 completed successfully.')

if __name__ == '__main__':
    main()
