class History:
    def __init__(self, messages: list = [], current_history_id: str = ""):
        self.messages = messages
        self.current_history_id = current_history_id

    def add_message(self, role: str, message: str):
        self.messages.append({"role": role, "content": message})

    def get_messages(self):
        return self.messages

    def delete_history(self):
        pass
