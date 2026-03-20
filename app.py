from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from api_service import fetch_songs_from_api

st.set_page_config(page_title="MoodZen 3.0", page_icon="🎵")

st.title("🎵 MoodZen 3.0")
st.write("Select your mood and get songs from YouTube 🎧")

mood = st.radio(
    "enter your mood",
    ["Happy", "Sad", "Relaxed", "Energetic"]
)

if mood:
    st.info(f"Fetching songs for mood: {mood}")

    with st.spinner("Fetching songs..."):
        songs = fetch_songs_from_api(mood)

    if songs:
        st.subheader("🎶 Recommended Songs")
        for song in songs:
            st.markdown(f"- [{song['title']}]({song['url']})")
    else:
        st.error("Failed to fetch songs 😢")