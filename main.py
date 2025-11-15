from core.modes import *
from core.chat_manager import *
from core.engine import *
from ui.printer import call_banner
from core.ai_client import generate_stream_response


call_banner()

while True:
    user_input = input("Ask Anything: ")

    if user_input.startswith("/mode"):
        system_prompt = get_prompt_for_mode()

    elif user_input.startswith("/clear"):
        clear_history()

    elif user_input.startswith("/save"):
        save_history()

    elif user_input.lower() in ("exit","quit"):
        break

    else:
        add_user_message(user_input)
        messages = [{"role": "system", "content": system_prompt}] + get_history()
        generate_stream_response(messages)