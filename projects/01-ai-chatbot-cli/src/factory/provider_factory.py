from context import AppContext
from strategy.provider_strategy import (
    CustomProviderStrategy,
    OpenAIProviderStrategy,
    ProviderStrategy,
)


class ProviderFactory:
    @staticmethod
    def get_provider(context: AppContext, provider: str) -> ProviderStrategy:
        match provider:
            case "openai":
                return OpenAIProviderStrategy(context=context)
            case "custom":
                return CustomProviderStrategy(context=context)
            case _:
                return OpenAIProviderStrategy(context=context)
