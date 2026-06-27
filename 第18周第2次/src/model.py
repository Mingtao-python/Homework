from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

from .features import extract_features, drop_feature
from .data import texts, labels


def build_dataset(texts_list, labels_list):
    X = np.array([extract_features(t) for t in texts_list])
    y = np.array(labels_list)
    return X, y


def train_and_get_model(test_size=0.3, random_state=42):
    X, y = build_dataset(texts, labels)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    baseline = model.score(X_test, y_test)
    return model, baseline, X, y


def ablation_scores(X, y, test_size=0.3, random_state=67):
    names = ["Length", "MathWords", "CodingWords"]
    results = {}
    for i, name in enumerate(names):
        X_drop = drop_feature(X, i)
        X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(X_drop, y, test_size=test_size, random_state=random_state)
        m = LogisticRegression()
        m.fit(X_train_d, y_train_d)
        results[name] = m.score(X_test_d, y_test_d)
    return results


def classify(text: str, model):
    if text is None or text.strip() == "":
        return "Invalid Input: empty"
    if len(text) > 200:
        return "Invalid Input: too long"
    non_ascii = sum(1 for c in text if ord(c) > 127)
    if non_ascii / len(text) > 0.4:
        return "Invalid Input: unreadable"
    words = text.lower().split()
    for w in set(words):
        if words.count(w) >= 10:
            return "Invalid Input: spam"
    f = np.array(extract_features(text)).reshape(1, -1)
    return model.predict(f)[0]


def predict_difficulty(text: str):
    length = len(text)
    if length < 20:
        return "Easy"
    if length < 60:
        return "Normal"
    return "Hard"
