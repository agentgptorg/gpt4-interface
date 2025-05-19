import sys
from getpass import getpass
from gpt4_interface import GPT4Interface

def main():
    print("=== AgentGPT: GPT-4 Interface CLI ===")
    api_key = getpass("Enter your OpenAI API Key: ")
    agent = GPT4Interface(api_key)
    while True:
        try:
            prompt = input("\nAsk GPT-4 (or type 'exit'): ")
            if prompt.lower() in ("exit", "quit"): break
            response = agent.ask(prompt)
            print("\nResponse:\n", response)
        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except Exception as e:
            print("[Error]", e)

if __name__ == "__main__":
    main() 