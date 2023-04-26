
from . import AutoGPT_YouTube
import requests

plugin = AutoGPT_YouTube()

def search_youtube(query: str, max_results: int = 10) -> list:
    """Search for a query on youtube.

    Args:
        query (str): The query to search for.
        max_results (int, optional): The maximum number of results to return. Defaults to 10.

    Returns:
        list: The search results.
    """
    
    # perform the search
    api_key = plugin.yt_api_key

    # get the search results
    search_results = requests.get(
        f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={max_results}&q={query}&key={api_key}"
    ).json()

    # convert the title, description and video url to a list of dictionaries
    results = []
    for result in search_results["items"]:
        try:
            results.append(
                {
                    "title": result["snippet"]["title"],
                    "channel": result["snippet"]["channelTitle"],
                    "description": result["snippet"]["description"],
                    "url": f"https://www.youtube.com/watch?v={result['id']['videoId']}",
                }
            )
        except KeyError:
            pass

    return results


def get_youtube_comments(url: str, max_results: int = 15) -> list:
    """Get the comments of a YouTube video.

    Args:
        url (str): The URL of the YouTube video.
        max_results (int, optional): The maximum number of results to return. Defaults to 10.

    Returns:
        list: The comments of the YouTube video.
    """
    # get the video id
    video_id = url.split("v=")[1]

    # get the api key
    api_key = plugin.yt_api_key

    # get the comments, max 100 (limited by API). These are not the top comments.
    search_results = requests.get(
        f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&videoId={video_id}&key={api_key}"
    ).json()

    # sort the comments by likes
    search_results["items"].sort(key=lambda x: x["snippet"]["topLevelComment"]["snippet"]["likeCount"], reverse=True)
    print(len(search_results["items"]))

    # get the top max_results comments
    search_results["items"] = search_results["items"][:max_results]

    # convert the author, date, text and likes to a list of dictionaries
    results = []
    for result in search_results["items"]:
        try:
            results.append(
                {
                    "author": result["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                    "date": result["snippet"]["topLevelComment"]["snippet"]["publishedAt"],
                    "text": result["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
                    "likes": result["snippet"]["topLevelComment"]["snippet"]["likeCount"],
                }
            )
        except KeyError:
            pass

    return results