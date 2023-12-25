import requests

from Thinkers.IThinker import IThinker


class OllamaThinker(IThinker):

    def __init__(self, model="llama2-uncensored"):
        super().__init__()
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def think(self, input_text):
        request = requests.post(self.url, json={
            "model": self.model,
            "prompt": input_text,
            "system": self.systemPrompt,
            "stream": False,
        })
        return request.json()["response"]
