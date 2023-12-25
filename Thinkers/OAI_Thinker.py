from typing import Literal

from openai import OpenAI

from Thinkers.IThinker import IThinker


class OpenThinker(IThinker):
    def __init__(self, api_key, model: Literal[
        "gpt-4-1106-preview", "gpt-4-vision-preview", "gpt-4", "gpt-4-0314", "gpt-4-0613", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-0613", "gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-3.5-turbo-0301", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-16k-0613"] = "gpt-3.5-turbo"):
        super().__init__()
        self.OAI = OpenAI(api_key=api_key)
        self.model = model

    def think(self, input_text):
        response = self.OAI.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system", "content": self.systemPrompt
                },
                {
                    "role": "user", "content": input_text
                }
            ],
        )
        return response.choices[0].message["content"]
