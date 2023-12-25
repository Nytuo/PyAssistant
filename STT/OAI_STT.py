from typing import Literal

from openai import OpenAI

from STT.ISTT import ISTT


class OAI_STT(ISTT):
    def __init__(self, api_key, model: Literal["whisper-1"] = "whisper-1", audio_file_path="recorded.wav"):
        super().__init__(audio_file_path)
        self.model = model
        self.oai = OpenAI(api_key=api_key)

    def get_speech_to_text(self):
        print("TRANSCRIBING")
        audio_file = open(self.audio_file_path, "rb")
        transcript = self.oai.audio.transcriptions.create(
            model=self.model,
            file=audio_file,
            response_format="text",
        )
        print("TRANSCRIBED")
        return transcript
