import requests
from src.check.data.info import URL, API_KEY, SYSTEM_PROMPT2

def is_safe(user_input):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT2},
        {"role": "user", "content": user_input}
    ]

    r = requests.post(
        URL,
        json={"model": "llama-3.1-8b-instant", "messages": messages},
        headers={"Authorization": f"Bearer {API_KEY}"}
    )

    reply = r.json()["choices"][0]["message"]["content"].strip().lower()
    return reply == "allowed"