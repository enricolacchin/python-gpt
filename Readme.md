# PYTHON-GPT | YOUR PERSONAL ASSISTANT

A command-line chatbot and a voice assistant built on the OpenAI API.

## How to get an API Key
1. Go on [platform.openai.com](https://platform.openai.com/)
2. Log-in
3. Navigate to [this](https://platform.openai.com/api-keys) url
4. Create a new API Key
5. Copy [secrets_nokey.json](./secrets_nokey.json) to `secrets.json` (same folder) and paste your API key in it:

```
cp secrets_nokey.json secrets.json
```

`secrets.json` is listed in `.gitignore`, so your key is never committed. You can also change the `model` field (default: `gpt-4o-mini`).

## Installation
```
pip install -r requirements.txt
```
(on macOS, install `portaudio` first for the voice assistant: see *Possible Errors* below)

## :robot: Chatbot
### Requirements
* Python 3.8 or later
* `openai` 1.x

### Features
* Easy command line interface.
* Text generation using OpenAI's chat models (`gpt-4o-mini` by default).

### Usage
To run the script, just execute the following command:

```
python chatbot.py
```

You will be prompted to write a text and the assistant will respond with a written answer

## 	:speaking_head: Voice Assistant
### Requirements
* Python 3.8 or later
* `openai` 1.x, `pyttsx3`, `SpeechRecognition` and `PyAudio`

### Features
* Easy command line interface.
* Text generation using OpenAI's chat models (`gpt-4o-mini` by default).
* Text to Audio conversion using the pyttsx3 library.
* Audio to Text conversion using Google API.

### Usage
To run the script, just execute the following command:

```
python voiceAssistant/voiceAssistant.py
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
* The script is currently configured to work only with Italian language, but can be adapted for other languages (edit the `language='it-IT'` argument in `listen()` in [voiceAssistant.py](./voiceAssistant/voiceAssistant.py)).
  
## Notes
* Make sure you have a valid OpenAI API key before running the program.
* Make sure the required libraries are installed
* Full [OpenAI](https://openai.com) docs: [here](https://platform.openai.com/docs/guides/text-generation)

