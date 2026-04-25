"""Entry repository for diary entry persistence."""


class EntryRepository:
    """Encapsulates SQL operations related to diary entries."""

    def __init__(self, connection):
        """Initialize repository with a database connection."""
        self._connection = connection

    def create(self, user_id, prompt, content, title=None):
        """Stores a diary entry for a user."""
        self._connection.execute(
            "INSERT INTO entries (user_id, prompt, content, title) VALUES (?, ?, ?, ?)",
            (user_id, prompt, content, title),
        )
        self._connection.commit()

    def find_for_user(self, user_id):
        """Returns all diary entries for a user, newest first."""
        cursor = self._connection.execute(
            """
            SELECT id, prompt, content, title, created_at
            FROM entries
            WHERE user_id = ?
            ORDER BY datetime(created_at) DESC, id DESC
            """,
            (user_id,),
        )
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    def delete_for_user(self, entry_id, user_id):
        """Deletes one entry owned by a user. Returns True when deleted."""
        cursor = self._connection.execute(
            "DELETE FROM entries WHERE id = ? AND user_id = ?",
            (entry_id, user_id),
        )
        self._connection.commit()
        return cursor.rowcount > 0
