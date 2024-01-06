from typing import Literal

from openai import OpenAI

from STT.ISTT import ISTT


def get_OAI_STT(model: Literal["whisper-1"],
                audio_file_path="recorded.wav", api_key=""):
    oai = OpenAI(api_key=api_key)
    print("TRANSCRIBING")
    audio_file = open(audio_file_path, "rb")
    transcript = oai.audio.transcriptions.create(
        model=model,
        file=audio_file,
        response_format="text",
    )
    print("TRANSCRIBED")
    return transcript
