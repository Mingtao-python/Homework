import json, os, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))

try:
    import faiss
except:
    faiss = None

def cos_sim_matrix(M, q):
    q = np.array(q, dtype=float)
    M = np.array(M, dtype=float)
    q /= np.linalg.norm(q) + 1e-12
    M /= np.linalg.norm(M, axis=1, keepdims=True) + 1e-12
    return M @ q

def search_faiss(v, q, k):
    idx = faiss.IndexFlatIP(len(v[0]))
    idx.add(np.array(v, dtype='float32'))
    scores, ids = idx.search(np.array([q], dtype='float32'), k)
    return [{'id': int(i), 'score': float(s)} for s, i in zip(scores[0], ids[0])]

def search_fallback(v, q, k):
    scores = cos_sim_matrix(v, q)
    order = np.argsort(scores)[::-1][:k]
    return [{'id': int(i + 1), 'score': float(scores[i])} for i in order]

def main():
    docs = [
        {"id": 1, "text": "FAISS is used for fast vector search.", "vector": [0.95, 0.10, 0.20], "source": "research_paper_1"},
        {"id": 2, "text": "Approximate nearest neighbor methods trade precision for speed.", "vector": [0.80, 0.25, 0.10], "source": "textbook"},
        {"id": 3, "text": "Indexing allows batch retrieval over many embeddings.", "vector": [0.20, 0.85, 0.30], "source": "technical_doc"},
        {"id": 4, "text": "Vector databases support semantic retrieval.", "vector": [0.40, 0.70, 0.80], "source": "blog_post"},
        {"id": 5, "text": "Top-K search returns the most relevant candidates.", "vector": [0.70, 0.20, 0.60], "source": "tutorial"},
        {"id": 6, "text": "Hashing techniques reduce search complexity significantly.", "vector": [0.75, 0.15, 0.65], "source": "research_paper_2"},
        {"id": 7, "text": "Quantization compresses vectors for efficient storage.", "vector": [0.65, 0.35, 0.55], "source": "technical_doc"},
        {"id": 8, "text": "Product quantization enables billion-scale retrieval.", "vector": [0.55, 0.45, 0.50], "source": "research_paper_3"},
    ]
    q, ks = [0.90, 0.20, 0.15], [1, 3, 5]
    v = [d['vector'] for d in docs]
    results = {k: (search_faiss(v, q, k) if faiss else search_fallback(v, q, k)) for k in ks}
    
    plt.figure(figsize=(10, 5))
    plt.bar([str(k) for k in ks], [len(results[k]) for k in ks], color=['#E45756', '#72B7B2', '#4E79A7'])
    plt.ylabel('Returned items')
    plt.xlabel('Top-K parameter')
    plt.title('Top-K comparison analysis')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()

    json.dump({'query': q, 'documents': docs, 'num_docs': len(docs), 'index_type': 'FAISS' if faiss else 'NumPy'}, open(os.path.join(ROOT, 'dataset.json'), 'w'), indent=2)
    json.dump({'query_vector': q, 'search_results': results, 'total_docs': len(docs)}, open(os.path.join(ROOT, 'results.json'), 'w'), indent=2)
    
    report = "# Implementation 2 Testing Report\n\n- Built a vector index with {} backend.\n- Compared Top-K values 1, 3, and 5 across {} documents.\n- Index type: {}\n\n## Result Summary\n".format('FAISS' if faiss else 'NumPy', len(docs), 'FAISS' if faiss else 'NumPy fallback')
    for k in ks:
        report += f"### Top-{k} (retrieved {len(results[k])} documents)\n"
        for item in results[k]:
            doc = next((d for d in docs if d['id'] == item['id']), None)
            report += f"- Doc {item['id']} ({doc['source'] if doc else 'unknown'}): score={item['score']:.3f}\n"
    open(os.path.join(ROOT, 'report.md'), 'w').write(report)
    print('Implementation 2 completed successfully.')

if __name__ == '__main__':
    main()
