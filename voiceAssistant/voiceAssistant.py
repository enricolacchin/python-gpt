import sys
import json
import openai
import pyttsx3 # Text -> Audio conversion
import speech_recognition as sr # Audio -> Text conversion


# Import API KEY 
with open(sys.path[0] + '/../secrets.json') as f: # I used this function because the secrets.json file is in the parent directory
    secrets = json.load(f)
    api_key = secrets["api_key"]

openai.api_key = api_key

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
        outputMessage = recognizer.recognize_google(audioMessage, language='it-IT') # Language setted to italian, you can easily change it      
    except :
        outputMessage = "An error occurred!"
        error = 1

    print (outputMessage)    
    return outputMessage, error

# Function that calls OpenAI service with a prompt and returns the response
def openaiCompletion(inputMessage):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = inputMessage,
        temperature = 1,
        max_tokens = 500, # MAX token used for the functioncall 1000 token is around 750 words
        top_p = 1,
        best_of = 20,
        frequency_penalty = 0.5,
        presence_penalty = 0
        )
    
    print (response.choices[0].text)   
    return response.choices[0].text

# Function that converts text into audio
def textToAudio(text):
    
    engine = pyttsx3.init() # Initialize Text -> Audio engine

    # Set the Text -> Audio engine properties
    engine.setProperty('rate', 200)  # Set the speaking rate (words per minute)
    engine.setProperty('volume', 1)  # Set the volume (0 to 1)

    engine.say(text)
    engine.runAndWait()


####### HERE STARTS THE MAIN APPLICATION #######

inputMessage, error = listen() # User audio input

if error == 0:
    try:
        message = openaiCompletion(inputMessage) # Call OpenAI services with user voice message
    except:
        message = "I can't answer"
else: 
    message = "I didn't understand"

textToAudio(message) # Text -> Audio the response from OpenAI
