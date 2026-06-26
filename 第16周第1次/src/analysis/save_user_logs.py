import os, json
from datetime import datetime
from data.info import LOG_PATH
def save_log(question, mode, result_type, is_attack=False):
    os.makedirs("data", exist_ok=True)

    record = {
        "time": str(datetime.now()),
        "question": question,
        "mode": mode,
        "result_type": result_type,
        "is_attack": is_attack
    }

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")