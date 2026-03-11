import json
import uuid
from email import message

from command.command import Command
from context import AppContext


class SaveConversationCommand(Command):
    def execute(self, context: AppContext) -> None:
        with open("src/conversations.json", "r", encoding="utf-8") as conversation_file:
            conversation_data = json.load(conversation_file)

        history = context.history
        messages = history.get_messages()
        with open("src/conversations.json", "w") as conversation_file:
            conversation_data.append({"id": str(uuid.uuid4()), "messagges": messages})
            json.dump(conversation_data, conversation_file, indent=4)
