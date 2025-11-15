chat_history = []

def add_user_message(msg):
    chat_history.append({"role": "user", "content": msg})

def add_ai_message(msg):
    chat_history.append({"role": "assistant", "content": msg})

def clear_history():
    chat_history.clear()

def save_history():
    with open("filename", "w", encoding="utf-8") as f:
        for msg in chat_history:
            f.write(f"{msg['role'].upper()}: {msg['content']}\n")

def get_history():
    return chat_history.copy()

