from .chat_manager import *
from .ai_client import send_to_model

def generate_response(user_input, system_prompt):
    add_user_message(user_input)

    messages = [{"role": "system", "content": system_prompt}] + get_history()
    
    ai_text = send_to_model(messages)

    add_ai_message(ai_text)

    return ai_text

    