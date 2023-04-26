import youtube_transcript_api
import nltk


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

    # check if the transcript has more than 2500 tokens
    tokenized_text = nltk.tokenize.word_tokenize(transcript)

    MAX_TOKENS = 2500

    if len(tokenized_text) <= MAX_TOKENS:
        return transcript

    # save the transcript to a file in the folder auto_gpt_workspace and name it with the pattern: youtube_transcript_{video_id}.txt
    file_name = f"youtube_transcript_{video_id}.txt"

    with open(file_name, "w") as f:
        f.write(transcript)

    return f"Transcript saved to {file_name}"

