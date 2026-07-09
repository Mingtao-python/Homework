import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "watchlist.json")


def load_watchlist():
    """Load watchlist from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
