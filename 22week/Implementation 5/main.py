import json, os, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = os.path.dirname(os.path.abspath(__file__))

DOCS = [
    "RAG uses retrieval to find relevant passages before generation.",
    "Vector databases support efficient similarity search over embeddings.",
    "Transformers generate fluent text from context-rich prompts.",
    "Chunk optimization balances context length and retrieval precision.",
    "FAISS enables fast approximate nearest neighbor search at scale.",
    "Multi-stage retrieval refines candidates through ranking pipelines.",
    "Knowledge graphs augment retrieval with structured information.",
    "Query understanding improves retrieval by clarifying intent.",
]
QS = [
    "What does RAG combine?",
    "How are vector databases used?",
    "What does FAISS help with?",
    "How can retrieval be optimized?",
]

def main():
    vec = TfidfVectorizer(stop_words='english')
    M = vec.fit_transform(DOCS)
    results = []
    for q in QS:
        qv = vec.transform([q])
        scores = cosine_similarity(qv, M).ravel()
        top3 = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:3]
        top_idx = top3[0][0]
        results.append({'question': q, 'top_doc_id': top_idx + 1, 'score': float(scores[top_idx]), 'context': DOCS[top_idx], 'answer': f"Based on: {DOCS[top_idx]}", 'alternatives': [{'doc_id': i+1, 'score': float(s)} for i, s in top3[1:]]})
    
    plt.figure(figsize=(10, 5))
    plt.bar([f"Q{i+1}" for i in range(len(results))], [r['score'] for r in results], color=['#2F4B7C', '#FFA600', '#D45087', '#59A14F'])
    plt.ylabel('Similarity')
    plt.xlabel('Question')
    plt.title('Mini RAG retrieval scores analysis')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()

    json.dump({'documents': DOCS, 'questions': QS, 'retrieval_method': 'TF-IDF', 'num_docs': len(DOCS)}, open(os.path.join(ROOT, 'dataset.json'), 'w'), indent=2)
    json.dump(results, open(os.path.join(ROOT, 'results.json'), 'w'), indent=2)
    
    report = "# Implementation 5 Testing Report\n\n- Built a mini RAG pipeline with document retrieval and answer generation.\n- Used TF-IDF retrieval to select context and produced grounded answers.\n- Processed {} questions across {} documents.\n\n## Query Results\n".format(len(QS), len(DOCS))
    for r in results:
        report += f"- Q: {r['question']} -> Doc {r['top_doc_id']} score={r['score']:.3f}\n  A: {r['answer']}\n"
    open(os.path.join(ROOT, 'report.md'), 'w').write(report)
    print('Implementation 5 completed successfully.')

if __name__ == '__main__':
    main()
