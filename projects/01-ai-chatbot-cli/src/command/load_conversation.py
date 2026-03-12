import json

from rich.prompt import Prompt

from command.command import Command
from context import AppContext
from exceptions import FileNotFoundException


class LoadConversation(Command):
    def execute(self, context: AppContext) -> None:
        try:
            conversation_id = Prompt.ask(
                "[green]-------------Input Conversation Id[/green]"
            )
            with open(
                "src/conversations.json", "r", encoding="utf-8"
            ) as conversation_file:
                conversations = json.load(conversation_file)
                if conversation_id in conversations:
                    console = context.console
                    console.clear()
                    messages = conversations[conversation_id]
                    for message in conversations[conversation_id]:
                        if message["role"] == "user":
                            console.print(
                                "[green]User Input[/green]"
                                + ":"
                                + f" {message['content']}"
                            )
                        if message["role"] == "assistant":
                            console.print(
                                "[green]Chat Bot [/green]"
                                + ":"
                                + f" {message['content']}"
                            )
                    context.history.messages = messages
                    context.history.current_history_id = conversation_id
                else:
                    print("Conversation not found")
        except FileNotFoundError as _:
            raise FileNotFoundException("Conversation File Not Found")
