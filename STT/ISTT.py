from typing import Literal

from STT.OAI_STT import get_OAI_STT
from STT.W_STT import get_W_STT


class ISTT():
    def __init__(self, audio_file_path="recorded.wav"):
        self.audio_file_path = audio_file_path
        self.api_key = None
        self.model = None
        self.function = None

    def model(self, model: Literal["whisper-1", "tiny", "base", "small", "medium", "large"]):
        """
        This function will use the model
        :param model: The model to use
        :return: self
        """
        if model in ["whisper-1"] or model in ["tiny", "base", "small", "medium", "large"]:
            self.model = model
            match model:
                case "whisper-1":
                    self.function = get_OAI_STT
                case _ if model in ["tiny", "base", "small", "medium", "large"]:
                    self.function = get_W_STT
                case _:
                    raise ValueError("The model is not valid.")

        return self

    def using(self, api_key: str):
        """
        This function will use the api key
        :param api_key: The api key to use
        :return: self
        """
        self.api_key = api_key
        return self

    def get_speech_to_text(self):
        """
        This function will convert the .wav file into text
        :return: The text
        """
        return self.function(model=self.model, audio_file_path=self.audio_file_path, api_key=self.api_key if self.api_key else None)


