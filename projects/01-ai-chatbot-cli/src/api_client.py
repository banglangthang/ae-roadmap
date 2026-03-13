from http import HTTPStatus
from os.path import dirname, join

from dotenv import load_dotenv
from openai import AuthenticationError as OpenAIAuthenticationError
from openai import NotFoundError as OpenAINotFoundError
from openai import OpenAI
from openai import RateLimitError as OpenAIRateLimitError
from rich.console import Console

from exceptions import (
    AuthenticationException,
    ProviderURLNotFoundException,
    RateLimitException,
)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, override=True)


client = OpenAI(
    base_url="http://localhost:8317/v111",
)
console = Console()


def chat(messages: list):
    try:
        stream = client.chat.completions.create(
            model="qwen3-coder-flash",
            messages=messages,
            stream=True,
        )
        response = []
        console.print("Chatbot: ", style="green", end="")
        for chunk in stream:
            if len(chunk.choices) > 0 and chunk.choices[0].delta.content is not None:
                response.append(chunk.choices[0].delta.content)
                console.print(chunk.choices[0].delta.content, end="")
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
