from pathlib import Path
from services.user_service import UserService
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))


def test_user_can_register_and_login():
    service = UserService()

    assert service.register("Björn", "123lol")
    assert service.login("Björn", "123lol")

def test_user_cannot_register_with_already_taken_username():
    service = UserService()

    assert service.register("Björn", "123lol")
    assert not service.register("Björn", "456lol")

def test_user_cannot_login_with_wrong_password():
    service = UserService()

    assert service.register("Björn", "123lol")
    assert not service.login("Björn", "123lolwrong")

def test_user_cannot_login_with_empty_username():
    service = UserService()

    assert service.register("", "123lol")
