"""Database utilities for persistent storage."""

from pathlib import Path
import sqlite3

class Database:
    """Handles SQLite connections and schema initialization."""

    def __init__(self, db_path=":memory:"):
        if db_path == ":memory:":
            self._db_path = db_path
        else:
            self._db_path = str(Path(db_path))
            Path(self._db_path).parent.mkdir(parents=True, exist_ok=True)

    def get_connection(self):
        """Returns a SQLite connection with row access by column name."""
        connection = sqlite3.connect(self._db_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection


def initialize_database(connection):
    """Creates required tables if they do not exist."""
    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            prompt TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
        """
    )
    connection.commit()
