import streamlit as st

st.set_page_config(page_title="MoodZen", page_icon="🎵")

st.title("🎵 MoodZen - Mood-Based Song Suggestion App")
st.write("Welcome to MoodZen! Please select your mood:")

mood = st.selectbox("Choose your mood", ["Happy", "Sad", "Relaxed", "Energetic"])

songs = {
    "Happy": ["Happy - Pharrell Williams", "Best Day Of My Life - American Authors"],
    "Sad": ["Someone Like You - Adele", "Let Her Go - Passenger"],
    "Relaxed": ["Weightless - Marconi Union", "Bloom - The Paper Kites"],
    "Energetic": ["Can't Stop - Red Hot Chili Peppers", "Stronger - Kanye West"]
}

if mood:
    st.subheader(f"🎧 Songs for your {mood} mood:")
    for song in songs[mood]:
        st.write(f"- {song}")
