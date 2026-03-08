import requests

def fetch_songs_from_api(mood):
    """
    API से songs fetch करता है
    अभी demo data return कर रहे हैं
    """

    keyword = f"{mood} songs"

    # DEMO response (later YouTube/Spotify)
    demo_songs = [
        {
            "title": f"{keyword} - Song 1",
            "url": "https://www.youtube.com"
        },
        {
            "title": f"{keyword} - Song 2",
            "url": "https://www.youtube.com"
        },
        {
            "title": f"{keyword} - Song 3",
            "url": "https://www.youtube.com"
        }
    ]

    return demo_songs
