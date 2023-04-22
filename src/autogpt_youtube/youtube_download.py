import yt_dlp as yt
from . import AutoGPT_YouTube
import os

plugin = AutoGPT_YouTube()

def download_youtube_video(url: str, output_file: str) -> str:
    """Download a youtube video to mp4 format.

    Args:
        url (str): The url of the video to download.
        output_file (str): The output path.

    Returns:
        str: status message
    """

    if output_file.endswith(".mp4") is False:
        output_file += ".mp4"

    outtmpl = output_file.removesuffix(".mp4")
    outtmpl = os.path.join(plugin.workspace_path, outtmpl)

    # download the video
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": outtmpl,
    }
    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"Downloaded the video from {url} to {output_file}"


def download_youtube_audio(url: str, output_file: str) -> str:
    """Download a youtube video to mp3 format.

    Args:
        url (str): The url of the video to download.
        output_file (str): The output path.

    Returns:
        str: status message
    """

    if output_file.endswith(".mp3") is False:
        output_file += ".mp3"

    outtmpl = output_file.removesuffix(".mp3")
    outtmpl = os.path.join(plugin.workspace_path, outtmpl)

    # download the video
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
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

    return f"Downloaded the audio from {url} to {output_file}"