from typing import Literal

import whisper

from STT.ISTT import ISTT


def get_W_STT(model: Literal["tiny", "base", "small", "medium", "large"], audio_file_path="recorded.wav"):
    print("TRANSCRIBING")
    model = whisper.load_model(model)
    result = model.transcribe(audio_file_path)
    print("TRANSCRIBED")
    return result["text"]
