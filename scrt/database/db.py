import sqlite3

DB_NAME = "residents.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS residents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            debt REAL DEFAULT 0,
            status TEXT DEFAULT 'normal',
            risk_score INTEGER DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resident_id INTEGER,
            description TEXT,
            severity INTEGER,
            timestamp TEXT,
            FOREIGN KEY (resident_id) REFERENCES residents(id)
        )
    """)

    conn.commit()
    conn.close()


def add_resident(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO residents (name) VALUES (?)",
        (name,)
    )

    conn.commit()
    conn.close()


def get_all_residents():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM residents")
    residents = cursor.fetchall()

    conn.close()
    return residents
