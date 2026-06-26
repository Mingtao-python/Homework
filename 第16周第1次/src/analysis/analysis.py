def classify_question(text):
    text = text.lower()
    if "solve" in text or "equation" in text:
        return "Math"
    if "python" in text or "code" in text:
        return "Coding"
    if "grammar" in text or "sentence" in text:
        return "English"
    return "General"