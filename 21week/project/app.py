from flask import Flask, render_template, request
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from prompt_filter import filter_prompt
from src.Implementation1.similarity import cosine_similarity
from src.Implementation2.tfidf_search import tfidf_search
from src.Implementation3.embedding_similarity import embedding_similarity_matrix
from src.Implementation4.embedding_search import embedding_search
from src.Implementation5.gradient_descent_demo import run_gradient_demo
from src.Implementation6.embedding_failure_analysis import find_failure_cases

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "dataset.txt")
docs = open(DATA_PATH, encoding="utf-8").read().splitlines()

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_vecs = model.encode(docs)

def cosine_vec(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form["query"]
        run, reason = filter_prompt(q)
        if run:
            cosine_result = cosine_similarity(q, "example text")
            tfidf_results = tfidf_search(q)
            embedding_matrix = embedding_similarity_matrix()
            embedding_results = embedding_search(q)
            loss_curve = run_gradient_demo()
            failure_cases = find_failure_cases(q)
        else:
            cosine_result = None
            tfidf_results = None
            embedding_matrix = None
            embedding_results = None
            loss_curve = None
            failure_cases = None

        return render_template(
            "index.html",
            query=q,
            cosine_result=cosine_result,
            tfidf_results=tfidf_results,
            embedding_matrix=embedding_matrix,
            embedding_results=embedding_results,
            loss_curve=loss_curve,
            failure_cases=failure_cases,
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
