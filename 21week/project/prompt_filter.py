def filter_prompt(p):
    if len(p) > 300:
        return False, "Input too long"
    bad = ["ignore", "override", "bypass"]
    if any(w in p.lower() for w in bad):
        return False, "Unsafe prompt detected"
    if len(p) < 5:
        return False, "Input too short"
    return True, p