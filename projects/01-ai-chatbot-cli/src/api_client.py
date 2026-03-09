from os.path import dirname, join

from dotenv import load_dotenv
from openai import OpenAI

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, override=True)


client = OpenAI(
    base_url="http://localhost:8317/v1",
)


def chat(message: str):
    stream = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": message,
            },
        ],
        stream=True,
    )

    for event in stream:
        print(event)


def main():
    chat("Hello, who are you? Which models are you using?")


if __name__ == "__main__":
    main()
