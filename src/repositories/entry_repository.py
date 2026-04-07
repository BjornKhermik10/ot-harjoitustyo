"""Entry repository for diary entry persistence."""


class EntryRepository:
    """Encapsulates SQL operations related to diary entries."""

    def __init__(self, connection):
        self._connection = connection

    def create(self, user_id, prompt, content):
        """Stores a diary entry for a user."""
        self._connection.execute(
            "INSERT INTO entries (user_id, prompt, content) VALUES (?, ?, ?)",
            (user_id, prompt, content),
        )
        self._connection.commit()

    def find_for_user(self, user_id):
        """Returns all diary entries for a user, newest first."""
        cursor = self._connection.execute(
            """
            SELECT id, prompt, content, created_at
            FROM entries
            WHERE user_id = ?
            ORDER BY datetime(created_at) DESC, id DESC
            """,
            (user_id,),
        )
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
