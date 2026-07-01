import requests, os
from src.info import URL, api_key

if not api_key:
    print("Error: GROQ_API_KEY environment variable is not set.")
    raise SystemExit(1)

messages = input("User: ")

try:
    r = requests.post(
        URL,
        json={"model": "llama-3.1-8b-instant", "messages": messages},
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30
    )
    r.raise_for_status()
    reply = r.json()["choices"][0]["message"]["content"]
except requests.exceptions.Timeout:
    print("Error: API request timeout. Please try again.")
except requests.exceptions.ConnectionError:
    print("Error: Failed to connect to API. Please check your internet connection.")
except requests.exceptions.HTTPError as e:
    print(f"Error: API returned status {e.response.status_code}.")
except (KeyError, ValueError):
    print("Error: Invalid API response format.")
except requests.exceptions.RequestException as e:
    print(f"Error: API request failed - {str(e)}")
except Exception as e:
    print(f"Error: Unexpected error - {str(e)}")
