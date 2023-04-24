import json
import openai

# Import API KEY 
with open("secrets.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_key"]

openai.api_key = api_key

# Funtion to get the response
def get_response(messages:list):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages,
        temperature = 1.0 
    )
    return response.choices[0].message


if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a virtual assistant called Rachel and you speak Italian and English."}
    ]
    try:
        while True:
            username = "Enry" 
            user_input = input("\n" + username + ": ")
            messages.append({"role": "user", "content": user_input})
            new_message = get_response(messages=messages)
            print(f"Rachel: {new_message['content']}")
            messages.append(new_message)
            
    # Closing phrase, when the session will close the terminal show this sentence
    except KeyboardInterrupt:
        print("\nBye " + username + " see you next time!") 