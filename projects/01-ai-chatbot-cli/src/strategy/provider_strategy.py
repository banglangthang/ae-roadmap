import os
from abc import ABC, abstractmethod
from http import HTTPStatus
from os.path import dirname, join

from dotenv import load_dotenv
from openai import AuthenticationError as OpenAIAuthenticationError
from openai import NotFoundError as OpenAINotFoundError
from openai import OpenAI
from openai import RateLimitError as OpenAIRateLimitError

from context import AppContext
from exceptions import (
    AuthenticationException,
    ProviderURLNotFoundException,
    RateLimitException,
)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, override=True)


class ProviderStrategy(ABC):
    @abstractmethod
    def chat(self, messages: list, model: str) -> str:
        pass


class OpenAIProviderStrategy(ProviderStrategy):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OpenAIProviderStrategy, cls).__new__(cls)
        return cls._instance

    def __init__(
        self,
        context: AppContext,
        model: str = "qwen3-coder-flash",
    ) -> None:
        self.context = context
        self.url = os.environ.get("OPENAI_API_URL", "http://localhost:4141/v1")
        self.model = model
        self.client = OpenAI(base_url=self.url)

    def chat(self, messages: list, model: str) -> str:
        print(self.url)
        print(self.model)
        try:
            stream = self.client.chat.completions.create(
                model="qwen3-coder-flash",
                messages=messages,
                stream=True,
            )
            response = []
            self.context.console.print("Chatbot: ", style="green", end="")
            for chunk in stream:
                if (
                    len(chunk.choices) > 0
                    and chunk.choices[0].delta.content is not None
                ):
                    response.append(chunk.choices[0].delta.content)
                    self.context.console.print(chunk.choices[0].delta.content, end="")
            print("\n")
            return " ".join(response)
        except OpenAIAuthenticationError as e:
            raise AuthenticationException(
                message="OpenAPI authentication error",
                status_code=HTTPStatus.UNAUTHORIZED,
                original_error=e,
            )
        except OpenAINotFoundError as e:
            raise ProviderURLNotFoundException(
                message="OpenAI Provider URL not found",
                status_code=HTTPStatus.NOT_FOUND,
                original_error=e,
            )
        except OpenAIRateLimitError as e:
            raise RateLimitException(
                message="OpenAI Rate Limit Reached",
                status_code=HTTPStatus.TOO_MANY_REQUESTS,
                original_error=e,
            )


class CustomProviderStrategy(ProviderStrategy):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CustomProviderStrategy, cls).__new__(cls)
        return cls._instance

    def __init__(
        self,
        context: AppContext,
        model: str = "qwen3-coder-flash",
    ) -> None:
        self.context = context
        self.url = os.environ.get("CUSTOM_PROVIDER", "http://localhost:4141/v1")
        self.model = model
        self.client = OpenAI(base_url=self.url)

    def chat(self, messages: list, model: str) -> str:
        try:
            stream = self.client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
            )
            response = []
            self.context.console.print("Chatbot: ", style="green", end="")
            for chunk in stream:
                if (
                    len(chunk.choices) > 0
                    and chunk.choices[0].delta.content is not None
                ):
                    response.append(chunk.choices[0].delta.content)
                    self.context.console.print(chunk.choices[0].delta.content, end="")
            print("\n")
            return " ".join(response)
        except OpenAIAuthenticationError as e:
            raise AuthenticationException(
                message="OpenAPI authentication error",
                status_code=HTTPStatus.UNAUTHORIZED,
                original_error=e,
            )
        except OpenAINotFoundError as e:
            raise ProviderURLNotFoundException(
                message="OpenAI Provider URL not found",
                status_code=HTTPStatus.NOT_FOUND,
                original_error=e,
            )
        except OpenAIRateLimitError as e:
            raise RateLimitException(
                message="OpenAI Rate Limit Reached",
                status_code=HTTPStatus.TOO_MANY_REQUESTS,
                original_error=e,
            )
