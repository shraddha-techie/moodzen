import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="my-secret-pw",
        database="devops"
    )

def save_songs(mood, songs):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            mood VARCHAR(20),
            title VARCHAR(200),
            url VARCHAR(300)
        )
    """)

    for song in songs:
        cursor.execute(
            "INSERT INTO songs (mood, title, url) VALUES (%s, %s, %s)",
            (mood, song["title"], song["url"])
        )

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
