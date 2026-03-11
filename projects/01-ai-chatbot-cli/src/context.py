from dataclasses import dataclass

from rich.console import Console

from history import History


@dataclass
class AppContext:
    history: History
    console: Console
