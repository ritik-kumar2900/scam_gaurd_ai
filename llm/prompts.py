from utils import load_file
from pathlib import Path


PROMPTS_DIR = Path(__file__).parent / "prompt"
def load_prompt(filepath: str) -> str:
    return load_file(PROMPTS_DIR/filepath)




PROMPT = load_prompt("react.md")

def generate_prompt(message: str) -> str:

    template = PROMPT
    return f"{template}\n\n userInput:{message.strip()}"