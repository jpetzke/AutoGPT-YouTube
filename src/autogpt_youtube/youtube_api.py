
from . import AutoGPTYouTube
import requests

plugin = AutoGPTYouTube()

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
        results.append(
            {
                "title": result["snippet"]["title"],
                "description": result["snippet"]["description"],
                "url": f"https://www.youtube.com/watch?v={result['id']['videoId']}",
            }
        )

    return results


