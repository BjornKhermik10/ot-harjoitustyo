"""This file is responsible for managing user-related operations."""

from hashlib import sha256

from data.database import Database, initialize_database
from repositories.entry_repository import EntryRepository
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository=None, entry_repository=None):
        """Initializes service with optional repositories."""
        if user_repository and entry_repository:
            self._user_repository = user_repository
            self._entry_repository = entry_repository
            return

        database = Database()
        connection = database.get_connection()
        initialize_database(connection)
        self._user_repository = UserRepository(connection)
        self._entry_repository = EntryRepository(connection)

    @staticmethod
    def _hash_password(password):
        """Returns a simple SHA-256 hash string for the password."""
        return sha256(password.encode("utf-8")).hexdigest()

    @staticmethod
    def _verify_password(password, password_hash):
        """Checks whether the hash of the input matches stored hash."""
        return UserService._hash_password(password) == password_hash

    def register(self, username: str, password: str) -> bool:
        """Registers a user. Returns False when input is invalid or already used."""
        username = username.strip()
        password = password.strip()

        if not username or not password:
            return False

        if self._user_repository.find_by_username(username):
            return False

        password_hash = self._hash_password(password)
        return self._user_repository.create(username, password_hash)

    def login(self, username: str, password: str) -> bool:
        """Checks whether credentials match a persisted user."""
        username = username.strip()
        password = password.strip()

        if not username or not password:
            return False

        user = self._user_repository.find_by_username(username)
        if not user:
            return False
        return self._verify_password(password, user["password_hash"])

    def add_entry(self, username: str, prompt: str, content: str) -> bool:
        """Adds a diary entry for a user and returns success status."""
        username = username.strip()
        prompt = prompt.strip()
        content = content.strip()

        if not username or not prompt or not content:
            return False

        user = self._user_repository.find_by_username(username)
        if not user:
            return False

        self._entry_repository.create(user["id"], prompt, content)
        return True

    def get_entries_for_user(self, username: str):
        """Returns diary entries for one user, newest first."""
        username = username.strip()
        if not username:
            return []

        user = self._user_repository.find_by_username(username)
        if not user:
            return []

        return self._entry_repository.find_for_user(user["id"])

    def delete_entry_for_user(self, username: str, entry_id: int) -> bool:
        """Deletes one diary entry for a user and returns success"""
        username = username.strip()
        if not username:
            return False

        user = self._user_repository.find_by_username(username)
        if not user:
            return False

        return self._entry_repository.delete_for_user(entry_id, user["id"])
