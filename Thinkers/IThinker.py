class IThinker:
    def __init__(self):
        self.systemPrompt = "You are JARVIS (Just A Rather Very Intelligent System), you are helping me (Arnaud) in my "
        "daily tasks such as programming and other things. You can call me 'Arnaud', just 'Arnaud', "
        "not 'Dear Arnaud'. Respond in the language that will follow this."

    def think(self, input_text):
        """
        This function will think about the text and return a response
        :param input_text: The text
        :return: The response
        """
        raise NotImplementedError("This method is not implemented yet.")
