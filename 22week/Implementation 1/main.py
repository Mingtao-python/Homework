import json, os, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))

def cosine_sim(a, b):
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return float(np.dot(a, b) / denom) if denom else 0.0

def search_topk(docs, q, k=3):
    scores = [(cosine_sim(doc["vector"], q), doc) for doc in docs]
    return sorted(scores, reverse=True)[:k]

def main():
    docs = [
        {"id": 1, "text": "Vector databases store embeddings for fast similarity search.", "vector": [0.9, 0.1, 0.2], "category": "database"},
        {"id": 2, "text": "FAISS supports efficient nearest-neighbor indexing.", "vector": [0.8, 0.3, 0.1], "category": "indexing"},
        {"id": 3, "text": "Chunking improves retrieval quality for long documents.", "vector": [0.1, 0.8, 0.3], "category": "preprocessing"},
        {"id": 4, "text": "Semantic search ranks passages by meaning rather than keywords.", "vector": [0.2, 0.7, 0.8], "category": "retrieval"},
        {"id": 5, "text": "RAG combines retrieval and generation for grounded answers.", "vector": [0.3, 0.2, 0.9], "category": "generation"},
        {"id": 6, "text": "Embedding models convert text into numerical vectors.", "vector": [0.4, 0.6, 0.5], "category": "embedding"},
        {"id": 7, "text": "Transformer architectures dominate modern NLP tasks.", "vector": [0.7, 0.4, 0.3], "category": "architecture"},
        {"id": 8, "text": "Attention mechanisms enable models to focus on relevant tokens.", "vector": [0.6, 0.5, 0.4], "category": "mechanism"},
        {"id": 9, "text": "Fine-tuning adapts pre-trained models to specific tasks.", "vector": [0.5, 0.3, 0.7], "category": "training"},
        {"id": 10, "text": "Dense retrieval outperforms sparse keyword-based methods.", "vector": [0.65, 0.45, 0.35], "category": "comparison"},
    ]
    q, results = [0.85, 0.25, 0.15], search_topk(docs, [0.85, 0.25, 0.15], 5)
    
    scores, labels = [s[0] for s in results], [f"Doc {s[1]['id']}" for s in results]
    plt.figure(figsize=(10, 5))
    plt.bar(labels, scores, color=['#4C78A8', '#F58518', '#54A24B', '#E15759', '#72B7B2'])
    plt.ylabel('Cosine similarity')
    plt.xlabel('Document')
    plt.title('Top-K retrieval results (Top-5)')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()

    json.dump({'query_vector': q, 'documents': docs, 'num_docs': len(docs), 'vector_dim': len(q)}, open(os.path.join(ROOT, 'dataset.json'), 'w'), indent=2)
    json.dump([{'score': s, 'id': d['id'], 'text': d['text'], 'category': d['category']} for s, d in results], open(os.path.join(ROOT, 'results.json'), 'w'), indent=2)
    
    report = "# Implementation 1 Testing Report\n\n- Built a simple vector database using cosine similarity.\n- Stored 10 document vectors with metadata and executed a Top-K search.\n- Total documents: {}\n- Vector dimension: {}\n\n## Result Summary\n".format(len(docs), len(q))
    for s, d in results:
        report += f"- Document {d['id']} ({d['category']}): {d['text'][:50]}... (score={s:.3f})\n"
    open(os.path.join(ROOT, 'report.md'), 'w').write(report)
    print('Implementation 1 completed successfully.')

if __name__ == '__main__':
    main()
