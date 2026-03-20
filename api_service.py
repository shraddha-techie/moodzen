import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_songs_from_api(mood):
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": f"{mood} songs",
        "type": "video",
        "maxResults": 5,
        "key": API_KEY
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code != 200:
            return []

        data = response.json()
        songs = []

        for item in data.get("items", []):
            title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            songs.append({
                "title": title,
                "url": video_url
            })

        return songs

    except Exception as e:
        print("Error:", e)
        return []