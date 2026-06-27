import streamlit as st
from src.get_answers.load_answers import ask_ai
from src.check.data.info import SYSTEM_PROMPT
from src.check.ifallowed import allowed
from src.check.isok import is_safe
from src.analysis.save_user_logs import save_log
from src.analysis.analysis import classify_question
import os

os.chdir(os.path.dirname(__file__))

st.title("AI Step-by-Step Solver v1")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

question = st.text_area("Enter your question")

if st.button("Solve"):
    mode = classify_question(question)
    if not allowed(question):
        st.warning("Your question contains disallowed characters.")
        save_log(question, mode, "blocked", is_attack=True)
    elif not is_safe(question):
        st.warning("Your question contains strong override commands.")
        save_log(question, mode, "blocked", is_attack=True)
    else:
        st.session_state["messages"].append(
            {"role": "user", "content": question}
        )
        answer = ask_ai(st.session_state["messages"])
        st.session_state["messages"].append(
            {"role": "assistant", "content": answer}
        )

        save_log(question, mode, "success", is_attack=False)

if st.button("Clear Conversation"):
    st.session_state["messages"] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
pairs = []
msgs = st.session_state["messages"]
i = 1
while i < len(msgs):
    if msgs[i]["role"] == "user":
        user_msg = msgs[i]["content"]
        ai_msg = msgs[i+1]["content"] if i+1 < len(msgs) and msgs[i+1]["role"] == "assistant" else ""
        pairs.append((user_msg, ai_msg))
        i += 2
    else:
        i += 1

for user_msg, ai_msg in reversed(pairs):
    user_text = user_msg.replace("\n", "  \n")
    ai_text = ai_msg.replace("\n", "  \n")

    st.markdown(f"**You:**  \n{user_text}")
    st.markdown(f"**AI:**  \n{ai_text}")
    st.markdown("---")
