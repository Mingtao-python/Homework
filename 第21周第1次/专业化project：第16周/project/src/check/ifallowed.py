from src.check.data.strangethings import list1, list2
def allowed(question):
    for item in list2:
        if item in question:
            return False
    for item in list1:
        if item in question:
            return False
    if len(question) > 1000:
        return False
    if len(question.strip()) == 0:
        return False
    return True