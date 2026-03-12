from rich.console import Console
from rich.prompt import Prompt

from api_client import chat
from command.command_registry import CommandRegistry
from command.list_conversations_command import ListConversationCommand
from command.load_conversation import LoadConversation
from command.mode_command import ModeCommand
from command.quit_command import QuitCommand
from command.save_conversation_command import SaveConversationCommand
from context import AppContext
from exceptions import ProviderURLNotFound
from history import History

APP_CONTEXT = AppContext(history=History(), console=Console())
USER = "user"
ASSISTANT = "assistant"
CommandRegistry.register("/quit", QuitCommand)
CommandRegistry.register("/mode", ModeCommand)
CommandRegistry.register("/save", SaveConversationCommand)
CommandRegistry.register("/list", ListConversationCommand)
CommandRegistry.register("/load", LoadConversation)


def main():
    while True:
        history = APP_CONTEXT.history
        console = APP_CONTEXT.console
        try:
            message: str = Prompt.ask("[green]User Input[/green]")
            if message.startswith("/"):
                if message in CommandRegistry.commands:
                    command = CommandRegistry.get_command(message)
                    if command is not None:
                        command().execute(APP_CONTEXT)
                else:
                    print(f"Command '{message}' not found")
            else:
                history.add_message(USER, message)
                response = chat(messages=history.get_messages())
                history.add_message(ASSISTANT, response)
        except ProviderURLNotFound as e:
            console.print(f"[red]{e}[red]")
            console.print(f"[red]{e.status_code}[red]")
            break
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
