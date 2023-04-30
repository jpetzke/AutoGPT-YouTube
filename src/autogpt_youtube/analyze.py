import speech_recognition as sr
from pydub import AudioSegment
from . import AutoGPT_YouTube

import os

plugin = AutoGPT_YouTube()

def get_audio_duration(audio_file: str) -> str:
    """
    Get the duration of an audio file in seconds.

    Args:
        audio_file (str): The path to the audio file (mp3 format)

    Returns:
        float: The duration of the audio file in seconds.
    """

    audio_file = os.path.join(plugin.workspace_path, audio_file)

    audio_file = AudioSegment.from_file(audio_file, format="mp3")
    return f"The duration of the file {audio_file} is {len(audio_file) / 1000} seconds."


def audio_to_text(audio_file: str) -> str:
    """
    Convert an audio file to text using SpeechRecognition and Pydub.

    Args:
        audio_file (str): The path to the audio file (mp3 format)

    Returns:
        str: The transcribed text.
    """

    audio_file = os.path.join(plugin.workspace_path, audio_file)


    r = sr.Recognizer()

    # Load audio file using Pydub
    audio_file = AudioSegment.from_file(audio_file, format="mp3")
    audio = audio_file.export(format="wav")
    print("Audio file loaded and converted to wav format.")

    # Convert audio to text using SpeechRecognition
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)
        print("Transcribing audio file using Google... This may take a while.")
        text = r.recognize_google(audio_data)

    return text



def calculate_engagement_rate(likes: int, comments: int, views: int) -> float:
    """
    Calculate the engagement rate of a YouTube video.

    Args:
        likes (int): The number of likes.
        comments (int): The number of comments.
        views (int): The number of views.

    Returns:
        float: The engagement rate.
    """

    return (likes + comments) / views