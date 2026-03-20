import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def save_songs(mood, songs):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            mood VARCHAR(20),
            title VARCHAR(200),
            url VARCHAR(300),
            UNIQUE(title, mood)
        )
    """)

    for song in songs:
        try:
            cursor.execute(
                "INSERT INTO songs (mood, title, url) VALUES (%s, %s, %s)",
                (mood, song["title"], song["url"])
            )
        except:
            pass  # ignore duplicates

    conn.commit()
    cursor.close()
    conn.close()

def get_songs_from_db(mood):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT title, url FROM songs WHERE mood=%s",
        (mood,)
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result