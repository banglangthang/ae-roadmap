import json

from command.command import Command
from context import AppContext
from exceptions import FileNotFoundException


class ListConversationCommand(Command):
    def execute(self, context: AppContext) -> None:
        try:
            with open(
                "src/conversations.json", "r", encoding="utf-8"
            ) as conversation_file:
                conversations = json.load(conversation_file)
                for key, _ in conversations.items():
                    print(key)
        except FileNotFoundError as _:
            raise FileNotFoundException("Conversation File Not Found")
