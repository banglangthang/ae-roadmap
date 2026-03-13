from litellm import cost_per_token, token_counter
from rich.console import Console
from rich.prompt import Prompt

from command.change_model_command import ChangeModelCommand
from command.command_registry import CommandRegistry
from command.list_conversations_command import ListConversationCommand
from command.load_conversation import LoadConversationCommand
from command.mode_command import ModeCommand
from command.quit_command import QuitCommand
from command.save_conversation_command import SaveConversationCommand
from context import AppContext
from exceptions import ProviderURLNotFoundException
from factory.provider_factory import ProviderFactory
from history import History

APP_CONTEXT = AppContext(
    history=History(),
    console=Console(),
    provider="openai",
    model="qwen3-coder-flash",
)
USER = "user"
ASSISTANT = "assistant"
CommandRegistry.register("/quit", QuitCommand)
CommandRegistry.register("/mode", ModeCommand)
CommandRegistry.register("/save", SaveConversationCommand)
CommandRegistry.register("/list", ListConversationCommand)
CommandRegistry.register("/load", LoadConversationCommand)
CommandRegistry.register("/model", ChangeModelCommand)


def main():
    while True:
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
                APP_CONTEXT.history.add_message(USER, message)
                chat_client = ProviderFactory.get_provider(
                    APP_CONTEXT, provider=APP_CONTEXT.provider
                )
                input_token = token_counter(
                    model=APP_CONTEXT.model, messages=APP_CONTEXT.history.get_messages()
                )
                response = chat_client.chat(
                    messages=APP_CONTEXT.history.get_messages(), model=APP_CONTEXT.model
                )
                APP_CONTEXT.history.add_message(ASSISTANT, response)
                output_token = token_counter(
                    model=APP_CONTEXT.model,
                    messages=[{"role": "system", "content": response}],
                )
                input_cost, output_cost = cost_per_token(
                    model="gpt-4o",
                    prompt_tokens=input_token,
                    completion_tokens=output_token,
                )
                APP_CONTEXT.console.print(
                    f"[yellow]Tokens:{input_token + output_token}, Cost: ${input_token * input_cost + output_token * output_cost}[yellow]"
                )

        except ProviderURLNotFoundException as e:
            APP_CONTEXT.console.print(f"[red]{e}[red]")
            APP_CONTEXT.console.print(f"[red]{e.status_code}[red]")
            break
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
