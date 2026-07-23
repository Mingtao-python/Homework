import json, os, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))

CORPUS = "Large language models use transformer architectures to understand context. Transformer layers capture long-range dependencies through attention mechanisms. Chunking breaks long documents into smaller units to improve retrieval accuracy. Vector databases store embeddings so semantic search can find similar content. RAG systems combine retrieval results with generation to answer user questions. An embedding model converts raw text into dense vectors for similarity comparison. Evaluation often measures whether retrieved chunks contain the expected answer. Smaller chunks may improve precision but can increase fragmentation. Larger chunks may improve context coverage but reduce focus. Choosing the right chunk size is a core retrieval optimization problem. Multi-hop reasoning requires tracking dependencies across multiple documents. Dense passage retrieval uses learned representations for semantic search. Sparse methods like BM25 remain competitive for keyword-heavy queries. Hybrid approaches combine dense and sparse signals for better recall. Query expansion increases coverage by reformulating questions. Reranking models refine initial retrieval results using cross-encoders. Contrastive learning improves embedding quality through hard negatives. Curriculum learning accelerates model training with progressive difficulty."

def chunk_txt(txt, sz):
    words = txt.split()
    return [' '.join(words[i:i+sz]) for i in range(0, len(words), sz)]

def evaluate(sz):
    chunks = chunk_txt(CORPUS, sz)
    q_terms = set("What is the effect of chunk size on retrieval accuracy?".lower().replace('?', '').split())
    scores = [len(q_terms & set(chunks[i].lower().split())) for i in range(len(chunks))]
    return {'chunk_size': sz, 'num_chunks': len(chunks), 'avg_chunk_len': sum(len(c.split()) for c in chunks) / len(chunks) if chunks else 0, 'max_overlap': max(scores) if scores else 0, 'accuracy': 1.0 if max(scores) > 0 else 0.0}

def main():
    sizes = [100, 300, 500]
    results = [evaluate(s) for s in sizes]
    
    plt.figure(figsize=(10, 5))
    plt.bar([str(r['chunk_size']) for r in results], [r['accuracy'] for r in results], color=['#4E79A7', '#F28E2B', '#59A14F'])
    plt.ylabel('Accuracy')
    plt.xlabel('Chunk Size')
    plt.title('Chunk size accuracy comparison analysis')
    plt.ylim(0, 1.1)
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()

    json.dump({'corpus_length': len(CORPUS.split()), 'corpus_preview': CORPUS[:200], 'chunk_sizes': sizes, 'results': results}, open(os.path.join(ROOT, 'dataset.json'), 'w'), indent=2)
    json.dump(results, open(os.path.join(ROOT, 'results.json'), 'w'), indent=2)
    
    report = "# Implementation 3 Testing Report\n\n- Compared chunk sizes 100, 300, and 500.\n- Measured retrieval accuracy using keyword overlap with a representative query.\n- Corpus contains {} words across {} sentences.\n\n## Summary\n".format(len(CORPUS.split()), len(CORPUS.split('.')))
    for r in results:
        report += f"- Chunk size {r['chunk_size']}: {r['num_chunks']} chunks, avg length {r['avg_chunk_len']:.1f} words, accuracy={r['accuracy']:.2f}\n"
    open(os.path.join(ROOT, 'report.md'), 'w').write(report)
    print('Implementation 3 completed successfully.')

if __name__ == '__main__':
    main()
