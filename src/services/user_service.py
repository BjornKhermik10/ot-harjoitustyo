"""This file is responsible for managing user-related operations."""

class UserService:
    def __init__(self):
        """Initializes the user service with an empty list of users."""
        self._users = []

    def register(self, username: str, password: str) -> bool:
        """Registers a user in memory. Returns False if username already exists."""
        if any(user["username"] == username for user in self._users):
            return False

        self._users.append({"username": username, "password": password})
        return True

    def login(self, username: str, password: str) -> bool:
        """Checks whether credentials match an in-memory user."""
        return any(
            user["username"] == username and user["password"] == password
            for user in self._users
        )
