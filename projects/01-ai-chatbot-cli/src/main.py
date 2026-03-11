from rich.console import Console
from rich.prompt import Prompt

from api_client import chat
from command.command_registry import CommandRegistry
from command.mode_command import ModeCommand
from command.quit_command import QuitCommand
from context import AppContext
from history import History

APP_CONTEXT = AppContext(history=History(), console=Console())
USER = "user"
ASSISTANT = "assistant"
CommandRegistry.register("/quit", QuitCommand)
CommandRegistry.register("/mode", ModeCommand)


def main():
    while True:
        message: str = Prompt.ask("[green]User Input[/green]")
        if message.startswith("/"):
            if message in CommandRegistry.commands:
                command = CommandRegistry.get_command(message)
                if command is not None:
                    command().execute(APP_CONTEXT)
            else:
                print(f"Command '{message}' not found")
        else:
            history = APP_CONTEXT.history
            history.add_message(USER, message)
            response = chat(messages=history.get_messages())
            history.add_message(ASSISTANT, response)


if __name__ == "__main__":
    main()
