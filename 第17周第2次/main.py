from src.info import texts, labels
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import joblib

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.3, random_state=100
)

for k in [1, 3, 5, 15, 25, 50]:
    print(f"\n===== K = {k} =====")
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print("Accuracy:", acc)

best_model = KNeighborsClassifier(n_neighbors=3)
best_model.fit(X_train, y_train)

joblib.dump(best_model, "text_knn.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nBest model saved.")

def classify(text):
    if text is None or text.strip() == "":
        return "Invalid Input: empty text"

    if len(text) > 200:
        return "Invalid Input: text too long"

    non_ascii = sum(1 for c in text if ord(c) > 127)
    if non_ascii / len(text) > 0.4:
        return "Invalid Input: unreadable text"

    words = text.lower().split()
    for w in set(words):
        if words.count(w) >= 10:
            return "Invalid Input: repeated spam input"

    vec = vectorizer.transform([text])
    return best_model.predict(vec)[0]

if __name__ == "__main__":
    print(classify(""))
    print(classify("a" * 500))
    print(classify("啊啊啊啊啊啊啊啊啊啊"))
    print(classify("hello " * 20))
    print(classify("how to write python"))