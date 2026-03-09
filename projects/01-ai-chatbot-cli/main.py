import os
from os.path import dirname, join

from dotenv import load_dotenv
from openai import OpenAI, base_url

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, override=True)


client = OpenAI(
    base_url="http://localhost:8317/v1",
)


def main():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain how to set a custom base URL with the OpenAI Python SDK.",
            }
        ],
        model="qwen3-coder-flash",  # Use a model available at your specified base URL
    )
    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    main()
