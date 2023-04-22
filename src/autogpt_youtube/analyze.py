import speech_recognition as sr
from pydub import AudioSegment


def get_audio_duration(audio_file_path: str) -> str:
    """
    Get the duration of an audio file in seconds.

    Args:
        audio_file_path (str): The path to the audio file (mp3 format)

    Returns:
        float: The duration of the audio file in seconds.
    """

    audio_file = AudioSegment.from_file(audio_file_path, format="mp3")
    return f"The duration of the file {audio_file_path} is {len(audio_file) / 1000} seconds."


def audio_to_text(audio_file_path: str) -> str:
    """
    Convert an audio file to text using SpeechRecognition and Pydub.

    Args:
        audio_file_path (str): The path to the audio file (mp3 format)

    Returns:
        str: The transcribed text.
    """


    r = sr.Recognizer()

    # Load audio file using Pydub
    audio_file = AudioSegment.from_file(audio_file_path, format="mp3")
    audio = audio_file.export(format="wav")
    print("Audio file loaded and converted to wav format.")

    # Convert audio to text using SpeechRecognition
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)
        print("Transcribing audio file using Google... This may take a while.")
        text = r.recognize_google(audio_data)

    return text

