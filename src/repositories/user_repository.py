"""User repository for database operations."""

from sqlite3 import IntegrityError


class UserRepository:
    """Encapsulates SQL operations related to users."""

    def __init__(self, connection):
        self._connection = connection

    def create(self, username, password_hash):
        """Creates a user row and returns True when successful."""
        try:
            self._connection.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash),
            )
            self._connection.commit()
            return True
        except IntegrityError:
            return False

    def find_by_username(self, username):
        """Returns a user row as dict, or None if not found."""
        cursor = self._connection.execute(
            "SELECT id, username, password_hash FROM users WHERE username = ?",
            (username,),
        )
        row = cursor.fetchone()
        return dict(row) if row else None
