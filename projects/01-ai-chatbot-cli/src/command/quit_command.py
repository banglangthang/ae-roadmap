from command.command import Command
from context import AppContext


class QuitCommand(Command):
    def execute(self, context: AppContext) -> None:
        raise SystemExit()
