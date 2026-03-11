from abc import ABC, abstractmethod

from context import AppContext


class Command(ABC):
    @abstractmethod
    def execute(self, context: AppContext) -> None:
        pass
