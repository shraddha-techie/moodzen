import streamlit as st
from api_service import fetch_songs_from_api
from database import save_songs, get_songs_from_db

st.set_page_config(page_title="MoodZen 3.0.0", page_icon="🎵")

st.title("🎵 MoodZenn 3.0")
st.write("Select your mood and get fresh songs from the Internet 🎧")

mood = st.radio(
    "tell your mood",
    ["Happy", "Sad", "Relaxed", "Energetic","motivation"]
)

if mood:
    st.info(f"Fetching songs for mood: {mood}")

    songs = get_songs_from_db(mood)

    if not songs:
        st.warning("No songs in database. Fetching from API...")
        songs = fetch_songs_from_api(mood)
        save_songs(mood, songs)

    st.subheader("🎶 Recommended Songs")
    for song in songs:
        st.markdown(f"- [{song['title']}]({song['url']})")  # test pipeline run