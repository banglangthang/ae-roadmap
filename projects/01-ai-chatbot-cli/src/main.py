from rich.prompt import Prompt

from api_client import chat

messages = []


def main():
    while True:
        message: str = Prompt.ask("[green]User Input[/green]")
        if message == "/quit":
            break
        messages.append({"role": "user", "content": message})
        response = chat(messages=messages)
        messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
