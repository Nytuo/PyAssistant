# PyAssistant

## Disclaimer

This is just a little project I have made to pass time, not intended to be in production.    
The use of Python is due to the ease of use for AI stuff like Whisper or Bark.

## Naming

Py : Python    
Assistant : Well it's an assistant, so...

PyAssitant = P IA ssistant: So yes it does use AI (IA in french) to work

## Goal

The goal of this program is to have a fully functional AI to talk to that can respond to you.

## How it works

STT -> LLM -> TTS

This program takes a microphone input (the default one of your computer).    
Transcribe it to text (using Whisper from OpenAI (either local or online version).    
Then the text is sended to either an online OpenAI model (GPT-3 or GPT-4) or to a local Ollama model.    
Finally, the outputed text is then used to generate a voice (TTS) using either Bark (Local) or OpenAI TSS (online)     

## Steps

- To install the correct dependencies using PIP (look for each on their own repositories)
- To have a good GPU (optinal, for local models)
- To have an OpenAI secret key and some money on it (optional, for online use)
- To have Ollama and the wanted model installed (optional, for local model)
- To edit the .env file (rename the .env.sample) to customize it as you wish
- To edit the script in the function called "jarvis" to edit the STT / Thinker (LLM) / TTS to either online or offline use (maybe I'll make it available on the .env one day)
- To launch the script and optinally Ollama and press CTRL+SHIFT+H and start talking (in the limit of the amount of time you have set on the .env file).

## What's next

- Refactoring
- Make Bark works better (IDK but the output is wierd compared to what OpenAI or IILabs are doing)
- Make a GUI like an overlay to ease-of-use
