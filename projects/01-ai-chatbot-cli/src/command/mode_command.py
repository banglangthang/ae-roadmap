from rich.prompt import Prompt

from command.command import Command
from context import AppContext
from prompt import SYSTEM_PROMPT, get_system_prompt


class ModeCommand(Command):
    def execute(self, context: AppContext) -> None:
        print(f"Supported mode: {list(SYSTEM_PROMPT)}")
        mode: str = Prompt.ask("[green]-------------Choose Mode[/green]")
        system_prompt = get_system_prompt(mode)
        if mode:
            context.history.add_message("system", system_prompt)
