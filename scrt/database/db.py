import sqlite3

DB_NAME = "residents.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS residents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            debt INTEGER DEFAULT 0,
            status TEXT DEFAULT 'normal',
            risk_score INTEGER DEFAULT 0
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


if __name__ == "__main__":
    create_tables()
    add_resident("Nazar")
    add_resident("Artem")
    add_resident("Illya")

    print(get_all_residents())



def get_resident_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM residents WHERE name = ?",
        (name,)
    )

    result = cursor.fetchone()
    conn.close()
    return result



print(get_resident_by_name("Illya"))