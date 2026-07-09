# AI helper security
## Section 1
### 1.1 what is the security structure?
attack.py
src
|-isok.py
|-ifallowed.py
|-strangethings.py
|-info.py
### 1.2 What it these files doing?
They work together to filter out bad input and prevent prompt injection attacks, ensuring the AI helper operates securely and reliably.

---

## Section 2
### 2.1 What does ifallowed.py do?
ifallowed.py contains the allowed() function, which checks if the input text contains any disallowed characters or patterns. It returns True if the input is clean and False if it contains potentially harmful content checked by the character filter.
### 2.2 What does isok.py do?
isok.py contains the is_safe() function, which checks if the input text contains any strong override commands that could be used for prompt injection attacks. It returns True if the input is safe and False if it contains potentially harmful commands checked by AI safety rules.
### 2.3 What does attack.py do?
attack.py contains a list of test inputs that include various types of attacks, such as prompt injection and character-based attacks. It runs each input through the allowed() and is_safe() functions to determine if they are blocked or allowed, and prints the results.
### 2.4 What does info.py do?
info.py contains system prompts that define the behavior of the AI helper. These prompts guide the AI on how to respond to user inputs, ensuring it provides helpful and relevant answers while adhering to safety guidelines.

---

## Section 3
## Conclusion
The security structure of the AI helper is designed to protect against malicious inputs and ensure safe interactions. By implementing character filtering and prompt injection detection, the system can effectively block harmful content while allowing legitimate queries to be processed. This layered approach enhances the overall security and reliability of the AI helper.