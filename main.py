# Importing the libs
import os
from dotenv import load_dotenv
import pyaudio
import wave
import pygame
import keyboard

from STT.ISTT import ISTT
from TTS.BARK_TTS import BARK_TTS
from TTS.OAI_TTS import OAI_TTS
from Thinkers.OllamaThinker import OllamaThinker
from Thinkers.OAI_Thinker import OpenThinker

# Loading the .env file and the OpenAI API
load_dotenv()


def get_microphone_to_audiofile():
    """
    This function will record your voice and save it into a .wav file
    :return: The .wav file name
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    output=True,
                    frames_per_buffer=1024)
    frames = []
    print("RECORDING")
    for i in range(int(44100 / 1024 * int(os.getenv("RECORD_LENGTH")))):
        data = stream.read(1024)
        frames.append(data)
    print("END OF RECORDING.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(os.getenv("RECORD_FILE_NAME"), "wb")
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b"".join(frames))
    wf.close()
    return os.getenv("RECORD_FILE_NAME")


def play_audio(audio_file):
    """
    This function will play the .mp3 file
    :param audio_file: The .mp3 file path
    """
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    print("PLAYING AUDIO")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    print("AUDIO PLAYED")


def jarvis(online_stt=False, online_tts=False, online_thinker=False):
    audiopath = get_microphone_to_audiofile()
    if not online_stt:
        transcript = ISTT(audio_file_path=audiopath).model(model=os.getenv("STT_OFF_MODEL")).get_speech_to_text()
    else:
        transcript = ISTT(audio_file_path=audiopath).model(model=os.getenv("STT_OFF_MODEL")).using(api_key=os.getenv("OPENAI_API_KEY")).get_speech_to_text()
    print("TRANSCRIPT: " + transcript)

    if not online_thinker:
        thinked = OllamaThinker(model=os.getenv("THINKER_OFF_MODEL")).think(transcript)
    else:
        thinked = OpenThinker(os.getenv("OPENAI_API_KEY"), model=os.getenv("THINKER_ON_MODEL")).think(transcript)
    print("GENERATED: " + thinked)

    if not online_tts:
        audio_output = BARK_TTS(model=os.getenv("TTS_OFF_VOICE"),
                                output_file=os.getenv("TTS_FILE_NAME")).get_text_to_speech(thinked)
    else:
        audio_output = OAI_TTS(os.getenv("OPENAI_API_KEY"), model=os.getenv("TTS_ON_MODEL"),
                               voice=os.getenv("TTS_ON_VOICE"),
                               output_file=os.getenv("TTS_FILE_NAME")).get_text_to_speech(thinked)

    play_audio(audio_output)


if __name__ == '__main__':
    print("JARVIS IS READY, PRESS CTRL+SHIFT+H TO ACTIVATE IT.")
    keyboard.add_hotkey(os.getenv("SHORTCUT_LISTEN"),
                        lambda: jarvis(online_stt=os.getenv("STT_ONLINE") == "1",
                                       online_tts=os.getenv("TTS_ONLINE") == "1",
                                       online_thinker=os.getenv("THINKER_ONLINE") == "1"))
    keyboard.add_hotkey(os.getenv("SHORTCUT_EXIT"), lambda: exit(0))
    keyboard.wait()
