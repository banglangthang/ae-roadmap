from this import s

from rich.prompt import Prompt

from api_client import chat
from history import History
from prompt import get_system_prompt

history = History()
USER = "user"
ASSISTANT = "assistant"


def main():
    while True:
        message: str = Prompt.ask("[green]User Input[/green]")
        if message == "/quit":
            break
        elif message == "/mode":
            mode: str = Prompt.ask("[green]Choose Mode[/green]")
            system_prompt = get_system_prompt(mode)
            history.add_message("system", system_prompt)
        else:
            history.add_message(USER, message)
            response = chat(messages=history.get_messages())
            history.add_message(ASSISTANT, response)


if __name__ == "__main__":
    main()
