import json

with open("src/system_prompts.json", "r") as f:
    SYSTEM_PROMPT = json.load(f)


def get_system_prompt(mode: str) -> str:
    match mode:
        case "assistant":
            return SYSTEM_PROMPT.get("assistant").get("system_prompt")
        case "coder":
            return SYSTEM_PROMPT.get("coder").get("system_prompt")
        case "teacher":
            return SYSTEM_PROMPT.get("teacher").get("system_prompt")
        case "creative":
            return SYSTEM_PROMPT.get("creative").get("system_prompt")
        case _:
            print(f"Mode {mode} not supported")
            return ""
