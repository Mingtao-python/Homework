# Implementation 2 Testing Report

- Built a vector index with NumPy backend.
- Compared Top-K values 1, 3, and 5 across 8 documents.
- Index type: NumPy fallback

## Result Summary
### Top-1 (retrieved 1 documents)
- Doc 2 (textbook): score=0.996
### Top-3 (retrieved 3 documents)
- Doc 2 (textbook): score=0.996
- Doc 1 (research_paper_1): score=0.993
- Doc 5 (tutorial): score=0.862
### Top-5 (retrieved 5 documents)
- Doc 2 (textbook): score=0.996
- Doc 1 (research_paper_1): score=0.993
- Doc 5 (tutorial): score=0.862
- Doc 7 (technical_doc): score=0.858
- Doc 6 (research_paper_2): score=0.856
