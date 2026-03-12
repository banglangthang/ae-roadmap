import json
import uuid

from command.command import Command
from context import AppContext
from exceptions import FileNotFoundException


class SaveConversationCommand(Command):
    def execute(self, context: AppContext) -> None:
        try:
            id = context.history.current_history_id
            if not id:
                id = str(uuid.uuid4())

            with open(
                "src/conversations.json", "r", encoding="utf-8"
            ) as conversation_file:
                conversation_data = json.load(conversation_file)

            history = context.history
            messages = history.get_messages()
            with open("src/conversations.json", "w") as conversation_file:
                conversation_data[f"{id}"] = messages
                json.dump(conversation_data, conversation_file, indent=4)
        except FileNotFoundError as _:
            raise FileNotFoundException("Conversation File Not Found")
