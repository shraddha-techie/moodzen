import streamlit as st

# Page config
st.set_page_config(page_title="MoodZen", page_icon="🎵", layout="centered")

# Background color using Markdown + HTML
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #1a237e, #ff69b4);  /* dark blue to pink */
    }

    .song-card {
        background-color: #ffe0f0;  /* soft pink */
        color: #000000;             /* text black */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
        margin-bottom: 12px;
        font-size: 18px;
        font-weight: bold;
    }
    .song-card a {
        text-decoration: none;
        color: #000000;
    }
    .song-card a:hover {
        color: #d81b60;  /* hover effect pink */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header banner
st.markdown("## 🎵 MoodZen - Mood-Based Song Suggestion App")
st.write("Welcome to MoodZen! Please select your mood:")

# Mood selection
mood = st.radio("Choose your mood", ["Happy", "Sad", "Relaxed", "Energetic"])

# Songs dictionary with links
songs = {
    "Happy": [
        ("Happy - Pharrell Williams", "https://youtu.be/ZbZSe6N_BXs"),
        ("Best Day Of My Life - American Authors", "https://youtu.be/Y66j_BUCBMY")
    ],
    "Sad": [
        ("Someone Like You - Adele", "https://youtu.be/hLQl3WQQoQ0"),
        ("Let Her Go - Passenger", "https://youtu.be/RBumgq5yVrA")
    ],
    "Relaxed": [
        ("Weightless - Marconi Union", "https://youtu.be/UfcAVejslrU"),
        ("Bloom - The Paper Kites", "https://youtu.be/8inJtTG_DuU")
    ],
    "Energetic": [
        ("Can't Stop - Red Hot Chili Peppers", "https://youtu.be/8DyziWtkfBw"),
        ("Stronger - Kanye West", "https://youtu.be/3m8LxZ5kUJo")
    ]
}

# Display clickable song cards
if mood:
    st.subheader(f"🎧 Songs for your {mood} mood:")
    for song, link in songs[mood]:
        st.markdown(
            f'<div class="song-card">🎶 <a href="{link}" target="_blank">{song}</a></div>',
            unsafe_allow_html=True
        )
