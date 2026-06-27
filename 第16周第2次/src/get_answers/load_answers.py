import requests
from src.check.data.info import URL, API_KEY
def ask_ai(messages):
    r = requests.post(
        URL,
        json={"model": "llama-3.1-8b-instant", "messages": messages},
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    reply = r.json()["choices"][0]["message"]["content"]
    return reply