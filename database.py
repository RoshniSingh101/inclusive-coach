import sqlite3
from datetime import datetime

def init_db():
    """Creates the database and table if they don't exist."""
    conn = sqlite3.connect("coach_history.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            transcript TEXT,
            feedback TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_session(transcript, feedback):
    """Saves a new coaching session to the database."""
    conn = sqlite3.connect("coach_history.db")
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO sessions (timestamp, transcript, feedback) VALUES (?, ?, ?)",
        (timestamp, transcript, feedback)
    )
    conn.commit()
    conn.close()

def get_all_sessions():
    """Retrieves all past sessions, newest first."""
    conn = sqlite3.connect("coach_history.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, transcript, feedback FROM sessions ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows