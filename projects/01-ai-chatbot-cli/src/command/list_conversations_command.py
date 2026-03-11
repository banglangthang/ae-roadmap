import json

from command.command import Command
from context import AppContext


class ListConversationCommand(Command):
    def execute(self, context: AppContext) -> None:
        with open("src/conversations.json", "r", encoding="utf-8") as conversation_file:
            conversations = json.load(conversation_file)
            for key, _ in conversations.items():
                print(key)
