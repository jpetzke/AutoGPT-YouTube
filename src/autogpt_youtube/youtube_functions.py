import youtube_transcript_api


def get_youtube_transcript(url: str) -> str:
    """Get the transcript of a YouTube video.

    Args:
        url (str): The URL of the YouTube video.

    Returns:
        str: The transcript of the YouTube video.
    """
    # get the video id
    video_id = url.split("v=")[1]

    # get the transcript
    transcript = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id)

    # convert the transcript to a string
    transcript = "\n".join([line["text"] for line in transcript])

    return transcript

