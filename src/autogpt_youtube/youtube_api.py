import os
import google.auth
from googleapiclient.discovery import build

from .functions import convert_ISO8601_to_seconds
from .analyze import calculate_engagement_rate

# Get the API key from environment variable
API_KEY = os.environ.get("YOUTUBE_API_KEY")

# Build the YouTube API client
youtube = build("youtube", "v3", developerKey=API_KEY)

def search_youtube(query: str, max_results: int = 10) -> list:
    """Search for a query on youtube.

    Args:
        query (str): The query to search for.
        max_results (int, optional): The maximum number of results to return. Defaults to 10.

    Returns:
        list: The search results.
    """
    # Call the search.list method to retrieve search results
    search_response = youtube.search().list(
        q=query,
        type="video",
        part="id,snippet",
        maxResults=max_results
    ).execute()

    # Convert the search results to a list of dictionaries
    results = []
    for search_result in search_response.get("items", []):
        try:
            results.append(
                {
                    "title": search_result["snippet"]["title"],
                    "channel": search_result["snippet"]["channelTitle"],
                    "url": f"https://www.youtube.com/watch?v={search_result['id']['videoId']}"
                }
            )
        except KeyError:
            pass

    return results


def get_youtube_comments(url: str, max_results: int = 15) -> list:
    """Get the comments of a YouTube video.

    Args:
        url (str): The URL of the YouTube video.
        max_results (int, optional): The maximum number of results to return. Defaults to 15.

    Returns:
        list: The comments of the YouTube video.
    """
    # Get the video ID from the video URL
    video_id = url.split("v=")[1]

    # Retrieve the comments for the video
    comments = []
    next_page_token = ''
    next_page_counter = 0

    MAX_NEXT_PAGES = 100

    while True:
        next_page_counter += 1
        if next_page_counter > MAX_NEXT_PAGES:
            break

        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=next_page_token
        )
        response = request.execute()
        
        # Add the comments to the list
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                'author': comment['authorDisplayName'],
                'date': comment['publishedAt'],
                'comment': comment['textDisplay'],
                'likes': comment['likeCount'],
            })
            
        # Check if there are more comments to retrieve
        if 'nextPageToken' in response:
            next_page_token = response['nextPageToken']
        else:
            break
    
    # sort the list of comments
    best_comments = sorted(comments, key=lambda k: k['likes'], reverse=True)

    return best_comments[:max_results]



def get_youtube_video_info(url: str):
    """Get the information of a YouTube video.

    Args:
        url (str): The URL of the YouTube video.

    Returns:
        dict: The information of the YouTube video.
    """
    # Get the video ID from the video URL
    video_id = url.split("v=")[1]

    # Retrieve the comments for the video
    video_info = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    ).execute()

    # Convert the search results to a list of dictionaries
    results = []
    for video in video_info.get("items", []):
        try:

            # convert video duration from ISO 8601 format to seconds
            duration = convert_ISO8601_to_seconds(video["contentDetails"]["duration"])

            # calculate the engagement rate
            engagement_rate = calculate_engagement_rate(
                likes=int(video["statistics"]["likeCount"]),
                comments=int(video["statistics"]["commentCount"]),
                views=int(video["statistics"]["viewCount"]),
            )


            results.append(
                {
                    "published_at": video["snippet"]["publishedAt"],
                    "channel_id": video["snippet"]["channelId"],
                    "title": video["snippet"]["title"],
                    "description": video["snippet"]["description"],
                    "thumbnail": video["snippet"]["thumbnails"]["high"]["url"],
                    "channel_title": video["snippet"]["channelTitle"],
                    "tags": video["snippet"]["tags"],
                    "duration": duration,
                    "view_count": video["statistics"]["viewCount"],
                    "like_count": video["statistics"]["likeCount"],
                    "comment_count": video["statistics"]["commentCount"],
                    "engagement_rate": engagement_rate,
                }
            )
        except KeyError:
            pass
    if results[0] == None:
        return None
    else:
        return results[0]