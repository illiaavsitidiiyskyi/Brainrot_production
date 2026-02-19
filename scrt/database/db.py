import sqlite3

def connect():
    conn = sqlite3.connect("residents.db")
    return conn



def create_tables():
    conn = connect()
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
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO residents (name) VALUES (?)",
        (name,)
    )

    conn.commit()
    conn.close()





def get_all_residents():
    conn = connect()
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



