from typing import Type

from command.command import Command


class CommandRegistry:
    commands: dict[str, Type[Command]] = {}

    @classmethod
    def register(cls, command_name: str, command_class: Type[Command]):
        cls.commands[f"{command_name}"] = command_class

    @classmethod
    def get_command(cls, command_name: str) -> Type[Command] | None:
        return cls.commands.get(command_name)
