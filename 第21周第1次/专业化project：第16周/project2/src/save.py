import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "watchlist.json")


def save_watchlist(watchlist):
    """Save watchlist to JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(watchlist, f, indent=2)
