from os.path import dirname, join
from queue import Empty

from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, override=True)


client = OpenAI(
    base_url="http://localhost:1222/v1",
)
console = Console()


def chat(messages: list):
    stream = client.chat.completions.create(
        model="gpt-4o",
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
