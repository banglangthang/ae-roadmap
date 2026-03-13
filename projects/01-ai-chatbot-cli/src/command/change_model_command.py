import json

from rich.prompt import Prompt

from command.command import Command
from context import AppContext
from exceptions import FileNotFoundException


class ChangeModelCommand(Command):
    def execute(self, context: AppContext):
        console = context.console
        try:
            with open("src/config.json", "r", encoding="utf-8") as config_file:
                config = json.load(config_file)
                providers = config.get("providers")
                if len(list(providers.keys())) > 0:
                    for key, values in providers.items():
                        console.print(f"[purple]{key}[purple]")
                        for k, _ in values.get("models").items():
                            console.print(f"[orange]-{k}[orange]")
                    provider = Prompt.ask("[green]Choose provider[green]")
                    model = Prompt.ask("[green]Choose model[green]")
                    context.provider = provider
                    context.model = model
                else:
                    print("nothing")

        except FileNotFoundError as _:
            raise FileNotFoundException("Conversation File Not Found")
