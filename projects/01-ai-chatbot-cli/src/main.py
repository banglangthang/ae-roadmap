from rich.prompt import Prompt

from api_client import chat

messages = []


def main():
    while True:
        message: str = Prompt.ask("[green]User Input[/green]")
        if message == "/quit":
            break
        chat(message=message)


if __name__ == "__main__":
    main()
