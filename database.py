import sqlite3 as sqlite

DB_NAME = "tasks.db"


def get_connection():
    return sqlite.connect(DB_NAME)


def create_table():
    with get_connection() as con:
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT, 
                description TEXT, 
                start_datetime TEXT,
                due_datetime TEXT,
                complete INTEGER DEFAULT 0
            )
            """)
        con.commit()


def add_task(title, description, start_datetime, due_datetime):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(
            """
            INSERT INTO tasks (title, description, start_datetime, due_datetime, complete)
            VALUES  (?, ?, ?, ?, ?)
        """,
            (title, description, start_datetime, due_datetime, 0),
        )
        con.commit()


def get_tasks():
    with get_connection() as con:
        cur = con.cursor()

        cur.execute("""
        SELECT id, title, description, start_datetime, due_datetime, complete
        FROM tasks
        ORDER BY due_datetime
        """)

        return cur.fetchall()


def delete_task(task_id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(
            """
        DELETE FROM tasks WHERE id = ?
        """,
            (task_id,),
        )

        con.commit()


def update_task(task_id, title, description):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(
            """
            UPDATE tasks
            SET title = ?,
                description = ?
            WHERE id = ?
            """,
            (title, description, task_id),
        )
        con.commit()
