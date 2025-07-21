import os
import warnings
import logging
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger('langchain').setLevel(logging.ERROR)

import json
import requests
from utils import retrieve_context
from colorama import Fore, Style

# Send prompt to Ollama
def ensure_model_loaded(model_name="phi"):
    import requests
    _ = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model_name, "prompt": "Hello", "stream": False}
    )

def generate_answer(context, user_query):
    prompt = f"""You are a technical assistant for Computer Science interview prep. The context is in JSON format — extract only the useful meaning and answer the question clearly in plain English.
    Do not respond in JSON format.
    If the context doesn’t help, say “I don’t know.”
    Context:{context}
    Question:{user_query}
    """
    ensure_model_loaded()
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model":"phi", "prompt": prompt, "stream": True},
            stream=True,
        )
        response.raise_for_status()

        output = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                output += data.get("response", "")

        return output.strip()

    except Exception as e:
        return f"[Ollama API Error] {str(e)}\nRaw: {response.text if 'response' in locals() else ''}"

def print_welcome():
    print(Fore.CYAN + "="*50)
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to PrepPal CLI -- Your Offline Interview Buddy")
    print(Fore.CYAN + "-"*50)
    print(Fore.GREEN + "🧠 Ask anything about core CS subjects!")
    print(Fore.GREEN + "📚 Subjects include OOP, DBMS, and System Design")
    print(Fore.CYAN + "-"*50)
    print(Fore.MAGENTA + "📌 Type 'exit' or 'quit' to close the tool")
    print(Fore.CYAN + "="*50)

def print_user_input(user_input):
    print(Fore.GREEN + f"\nYou: {user_input}")

def print_model_output(answer):
    print(Fore.WHITE + f"\nPrepPal: {answer}\n")

def main():
    print_welcome()
    print('\n')
    while True:
        try:
            user_input = input(Fore.GREEN + "You: ")
            if user_input.lower() in {"exit", "quit"}:
                print("Exiting PrepPal. See you again!")
                break
            if not user_input:
                continue
            context = retrieve_context(user_input)
            answer = generate_answer(context, user_input)
            print_model_output(answer)
        except KeyboardInterrupt:
            print("\nInterrupted. Goodbye!")
            break

if __name__ == "__main__":
    main()