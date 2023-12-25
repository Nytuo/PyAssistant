from typing import Literal

import whisper

from STT.ISTT import ISTT


class W_STT(ISTT):
    def __init__(self, model: Literal["tiny", "base", "small", "medium", "large"] = "small",
                 audio_file_path="recorded.wav"):
        super().__init__(audio_file_path)
        self.model = model

    def get_speech_to_text(self):
        print("TRANSCRIBING")
        model = whisper.load_model(self.model)
        result = model.transcribe(self.audio_file_path)
        print("TRANSCRIBED")
        return result["text"]
