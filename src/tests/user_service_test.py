from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from services.user_service import UserService


def test_user_can_register_and_login():
    """Tests that a user can register and then login successfully."""
    service = UserService()

    assert service.register("alice", "secret123")
    assert service.login("alice", "secret123")
