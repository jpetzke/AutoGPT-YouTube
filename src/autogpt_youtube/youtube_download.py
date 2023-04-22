import yt_dlp as yt
from . import AutoGPT_YouTube
import os

plugin = AutoGPT_YouTube()

def download_youtube_video(url: str, output: str) -> str:
    """Download a youtube video to mp4 format.

    Args:
        url (str): The url of the video to download.
        output (str): The output path.

    Returns:
        str: status message
    """

    # Switch to auto_gpt_workspace
    os.chdir(plugin.workspace_path)

    output = output.removesuffix(".mp4")

    # download the video
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": output,
    }
    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"Downloaded the video from {url} to {output}"


def download_youtube_audio(url: str, output: str) -> str:
    """Download a youtube video to mp3 format.

    Args:
        url (str): The url of the video to download.
        output (str): The output path.

    Returns:
        str: status message
    """

    # Switch to auto_gpt_workspace
    os.chdir(plugin.workspace_path)

    output = output.removesuffix(".mp3")

    # download the video
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"Downloaded the audio from {url} to {output}"