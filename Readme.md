# PYTHON-GPT - YOUR PERSONAL ASSISTANT

Chatbot Article [https://enricolacchin.com/chatgpt-python/]
Voice Assistant Article [https://enricolacchin.com/voice-assistant-python/] 

## How to get an API Key
1. Go on [https://platform.openai.com/]
2. Log-in
3. Navigate to [this](https://platform.openai.com/account/api-keys) url
4. Create a new API Key
5. Paste you API Key in the [secrets.json][./secrets_nokey.json] file

## Chatbot
### Requirements
* Import openai libraries

```
pip install openai
```

### Features
* Easy command line interface.
* Text generation using OpenAI's GPT-3.5 language model.

## Usage
To run the script, just execute the following command:

```
python assistant.py
```

You will be prompted to write a text and the assistant will respond with a written answer

## Voice Assistant
### Requirements
* Python 3.6 or later
* Import openai, pyttsx3 and SpeechRecognition libraries 

```
pip install openai
pip install pyttsx3
pip install SpeechRecognition
```

### Features
* Easy command line interface.
* Text generation using OpenAI's GPT-3 language model.
* Text to Audio conversion using the pyttsx3 library.
* Audio to Text conversion using Google API.

### Usage
To run the script, just execute the following command:

```
python voiceAssistant.py
```

You will be prompted to speak and the assistant will respond with a written answer that is spoken out loud.

### Possible Errors
* *AttributeError: Could not find PyAudio; check installation*
Solution on OSx (with homebrew installed):

```
brew install portaudio
pip install PyAudio
```

For more details see [this](https://stackoverflow.com/questions/47121382/could-not-find-pyaudio-check-installation-in-mac) thread on StackOverflow

### Limitations
* The quality of the speech recognition and response is dependent on the quality of the user's microphone and the OpenAI language model.
* The script is currently configured to work only with Italian language, but can be adapted for other languages (edit **line 28** of [voiceAssistant.py](./voiceAssistant/voiceAssistant.py)).
  
## Notes
* Make sure you have a valid OpenAI API key before running the program.
* Make sure the required libraries are installed
* Full [OpenAI](https://openai.com) docu: [here](https://platform.openai.com/docs/guides/chat)

