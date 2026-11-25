import json
from pathlib import Path

from openai import OpenAI

# Import API KEY (secrets.json sits next to this script)
with open(Path(__file__).resolve().parent / "secrets.json") as f:
    secrets = json.load(f)

client = OpenAI(api_key=secrets["api_key"])
MODEL = secrets.get("model", "gpt-4o-mini")

# Function to get the response
def get_response(messages: list) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=1.0,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a virtual assistant called Rachel and you speak Italian and English."}
    ]
    username = "Enry"
    try:
        while True:
            user_input = input("\n" + username + ": ")
            messages.append({"role": "user", "content": user_input})
            answer = get_response(messages=messages)
            print(f"Rachel: {answer}")
            messages.append({"role": "assistant", "content": answer})

    # Closing phrase, when the session will close the terminal show this sentence
    except (KeyboardInterrupt, EOFError):
        print("\nBye " + username + " see you next time!")
