import json
from pathlib import Path

from openai import OpenAI
import pyttsx3 # Text -> Audio conversion
import speech_recognition as sr # Audio -> Text conversion


# Import API KEY (secrets.json is in the parent directory)
with open(Path(__file__).resolve().parent.parent / "secrets.json") as f:
    secrets = json.load(f)

client = OpenAI(api_key=secrets["api_key"])
MODEL = secrets.get("model", "gpt-4o-mini")

# Function that accepts audio by microphone and convert into text
def listen():

    error = 0
    recognizer = sr.Recognizer() # Create a recognizer object

    # Set microphone as audio source
    with sr.Microphone() as source:
        print("Speak now:")
        audioMessage = recognizer.listen(source)

    # Convert Audio -> Text
    try:
        outputMessage = recognizer.recognize_google(audioMessage, language='it-IT') # Language set to italian, you can easily change it
    except (sr.UnknownValueError, sr.RequestError):
        outputMessage = "An error occurred!"
        error = 1

    print (outputMessage)
    return outputMessage, error

# Function that calls OpenAI service with a prompt and returns the response
def openaiCompletion(inputMessage):
    response = client.chat.completions.create(
        model = MODEL,
        messages = [{"role": "user", "content": inputMessage}],
        temperature = 1,
        max_tokens = 500, # MAX tokens for the answer: 1000 tokens are around 750 words
        frequency_penalty = 0.5,
        presence_penalty = 0
        )

    answer = response.choices[0].message.content
    print (answer)
    return answer

# Function that converts text into audio
def textToAudio(text):

    engine = pyttsx3.init() # Initialize Text -> Audio engine

    # Set the Text -> Audio engine properties
    engine.setProperty('rate', 200)  # Set the speaking rate (words per minute)
    engine.setProperty('volume', 1)  # Set the volume (0 to 1)

    engine.say(text)
    engine.runAndWait()


####### HERE STARTS THE MAIN APPLICATION #######

if __name__ == "__main__":
    inputMessage, error = listen() # User audio input

    if error == 0:
        try:
            message = openaiCompletion(inputMessage) # Call OpenAI services with user voice message
        except Exception as e:
            print(f"OpenAI error: {e}")
            message = "I can't answer"
    else:
        message = "I didn't understand"

    textToAudio(message) # Text -> Audio the response from OpenAI
