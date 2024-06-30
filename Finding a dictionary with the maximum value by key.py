import json

FILENAME = "input.json"


def task() -> dict:
    with open(FILENAME) as file:
        data = json.load(file)
    return max(data, key=lambda p: p["score"])


if __name__ == "__main__":
    print(task())
