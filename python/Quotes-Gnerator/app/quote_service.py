import json
import random
import sys
from pathlib import Path

QUOTES_PATH = Path(__file__).resolve().parent.parent / "data" / "quotes.json"


def validate_quotes(quotes):
    if not isinstance(quotes, list):
        raise ValueError("quotes.json must contain a list")
    if not quotes:
        raise ValueError("quotes.json has no quotes")

    for index, item in enumerate(quotes):
        if not isinstance(item, dict):
            raise ValueError(f"Entry {index} must be an object, got {type(item).__name__}")  # noqa: TRY004
        for key in ("quote", "author"):
            if key not in item:
                raise ValueError(f"Entry {index} is missing '{key}'")
            value = item[key]
            if not isinstance(value, str):
                raise ValueError(f"Entry {index}: '{key}' must be a string")
            if not value.strip():
                raise ValueError(f"Entry {index}: '{key}' must not be empty")


def load_quotes(path=QUOTES_PATH):
    try:
        with open(path, "r", encoding="utf-8") as file:
            quotes = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File missing: {path}") from None
    except json.JSONDecodeError as e:
        raise ValueError(f"{Path(path).name} is not valid JSON (line {e.lineno}): {e.msg}") from e

    validate_quotes(quotes)
    return quotes


def generate_quote(quotes):
    return random.choice(quotes)


def main():
    try:
        quotes = load_quotes()
    except (FileNotFoundError, ValueError) as e:
        print(e)
        sys.exit(1)

    data = generate_quote(quotes)
    quote = data["quote"]
    author = data["author"]

    print("---------------The quote of the day is----------------")
    print(quote)
    print("----------By the Author---------")
    print(author)


if __name__ == "__main__":
    main()