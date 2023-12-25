class ISTT():
    def __init__(self, audio_file_path="recorded.wav"):
        self.audio_file_path = audio_file_path

    def get_speech_to_text(self):
        """
        This function will convert the .wav file into text
        :return: The text
        """
        raise NotImplementedError("This function is not implemented yet")
