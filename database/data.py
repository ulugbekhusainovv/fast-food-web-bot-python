import sqlite3

def create_users_table() -> None:
    con = sqlite3.connect("database/users.db")
    c = con.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            tg_id INT NOT NULL,
            phone TEXT,
            location TEXT,
            orders TEXT
        )
    """)
    con.commit()
    c.close()
    con.close()

create_users_table()

def check_user(tg_id: int) -> bool:
    con = sqlite3.connect("database/users.db")
    c = con.cursor()
    c.execute("SELECT tg_id FROM users WHERE tg_id=?", (tg_id,))
    rows = c.fetchall()
    con.close()
    if len(rows) > 0:
        return True
    return False