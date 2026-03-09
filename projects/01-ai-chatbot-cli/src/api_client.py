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


def chat(message: str):
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
        stream=True,
    )
    console.print("Chatbot: ", style="green", end="")
    for chunk in stream:
        if len(chunk.choices) > 0 and chunk.choices[0].delta.content is not None:
            console.print(chunk.choices[0].delta.content, end="")
    print("\n")


def main():
    chat("Hello, who are you? Which models are you using?")


if __name__ == "__main__":
    main()
