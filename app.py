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

    .quote-box {
        background-color: #fff3e0;
        border-left: 5px solid #ff7043;
        padding: 15px;
        margin: 15px 0;
        font-style: italic;
        font-size: 18px;
        border-radius: 10px;
        color: #1a237e;

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

# Quotes for each mood
quotes = {
    "Happy": "😊 *Happiness is not something ready made. It comes from your own actions.*",
    "Sad": "💙 *Tough times never last, but tough people do.*",
    "Relaxed": "🌿 *Peace begins with a deep breath.*",
    "Energetic": "🔥 *The energy you put out is the energy you get back.*"
}

# Songs dictionary with links (added more songs for variety)
songs = {
    "Happy": [
        ("Happy - Pharrell Williams", "https://youtu.be/ZbZSe6N_BXs"),
        ("Best Day Of My Life - American Authors", "https://youtu.be/Y66j_BUCBMY"),
        ("Walking On Sunshine - Katrina & The Waves", "https://youtu.be/iPUmE-tne5U")
    ],
    "Sad": [
        ("Someone Like You - Adele", "https://youtu.be/hLQl3WQQoQ0"),
        ("Let Her Go - Passenger", "https://youtu.be/RBumgq5yVrA"),
        ("Fix You - Coldplay", "https://youtu.be/k4V3Mo61fJM")
    ],
    "Relaxed": [
        ("Weightless - Marconi Union", "https://youtu.be/UfcAVejslrU"),
        ("Bloom - The Paper Kites", "https://youtu.be/8inJtTG_DuU"),
        ("Better Together - Jack Johnson", "https://youtu.be/zzzzzz")
    ],
    "Energetic": [
        ("Can't Stop - Red Hot Chili Peppers", "https://youtu.be/8DyziWtkfBw"),
        ("Stronger - Kanye West", "https://youtu.be/3m8LxZ5kUJo"),
        ("Eye of the Tiger - Survivor", "https://youtu.be/btPJPFnesV4")
    ]
}

# Display
if mood:
    # Show mood-specific quote
    st.markdown(f'<div class="quote-box">{quotes[mood]}</div>', unsafe_allow_html=True)

    # Show songs
    st.subheader(f"🎧 Songs for your {mood} mood:")
    for song, link in songs[mood]:
        st.markdown(
            f'<div class="song-card">🎶 <a href="{link}" target="_blank">{song}</a></div>',
            unsafe_allow_html=True
        )
