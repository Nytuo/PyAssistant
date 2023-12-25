from typing import Literal

from openai import OpenAI

from TTS.ITTS import ITTS


class OAI_TTS(ITTS):
    def __init__(self, api_key, model: Literal["tts-1", "tts-1-hd"] = "tts-1",
                 voice: Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"] = "onyx",
                 output_file="output.mp3"):
        super().__init__(output_file)
        self.oai = OpenAI(api_key=api_key)
        self.model = model
        self.voice = voice

    def get_text_to_speech(self, input_text):
        print("GENERATING AUDIO")
        responses = self.oai.audio.speech.create(
            model=self.model,
            voice=self.voice,
            input=input_text,
        )
        responses.stream_to_file(self.output_file)
        responses.close()
        print("AUDIO GENERATED")
        return self.output_file
