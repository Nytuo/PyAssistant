from TTS.ITTS import ITTS
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav


class BARK_TTS(ITTS):
    def __init__(self, model="v2/en_speaker_2", output_file="output.mp3"):
        super().__init__(output_file)
        self.model = model

    def get_text_to_speech(self, input_text):
        preload_models()
        print("GENERATING AUDIO")
        audio_array = generate_audio(input_text, history_prompt=self.model)
        write_wav(self.output_file, SAMPLE_RATE, audio_array)
        return self.output_file
