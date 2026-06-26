import numpy as np

math_words = ["add", "sum", "plus", "minus", "divide", "multiply", "integral", "derivative"]
coding_words = ["python", "code", "function", "loop", "variable", "class", "debug"]


def extract_features(text: str):
    length = len(text)
    math_count = sum(w in text.lower() for w in math_words)
    coding_count = sum(w in text.lower() for w in coding_words)
    return [length, math_count, coding_count]


def drop_feature(X: np.ndarray, idx: int):
    return np.delete(X, idx, axis=1)
