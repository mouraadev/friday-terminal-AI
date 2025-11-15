import os
from dotenv import load_dotenv
from together import Together
from ui.gradient import gradient_line
from ui.banner import start_color, end_color
from .chat_manager import add_ai_message


load_dotenv()

client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

def send_to_model(messages):
    try:
        return client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages= messages,
            temperature=0.7,
            max_tokens=3000,
            stream=True,          
        )
    
    except Exception as e:
        raise e 
    
def generate_stream_response(messages):
    response = send_to_model(messages)

    ai_message = ""

    print(gradient_line("F.R.I.D.A.Y: ", start_color(), end_color()), end="")

    for chunk in response:
        if not chunk.choices:
            continue

        delta = chunk.choices[0].delta

        if hasattr(delta, "content") and delta.content:
            print(delta.content, flush=True, end="")
            ai_message += delta.content

    print("\n")
    add_ai_message(ai_message)