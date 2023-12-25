class ITTS:
    def __init__(self, output_file="output.mp3"):
        self.output_file = output_file

    def get_text_to_speech(self, input_text):
        """
        This function will convert the text into a .mp3 file
        :param input_text: Text to be converted
        :return: The .mp3 file path
        """
        raise NotImplementedError("This function is not implemented yet.")
