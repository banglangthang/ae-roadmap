from rich.prompt import Prompt

from api_client import chat
from history import History

history = History()
USER = "user"
ASSISTANT = "assistant"


def main():
    while True:
        message: str = Prompt.ask("[green]User Input[/green]")
        if message == "/quit":
            break
        history.add_message(USER, message)
        response = chat(messages=history.get_messages())
        history.add_message(ASSISTANT, response)


if __name__ == "__main__":
    main()
