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

def test_user_cannot_login_with_empty_username_and_or_password():
    service = UserService()

    assert not service.register("", "123lol")
    assert not service.register("Björn", "")
    assert not service.login("", "")

def test_register_strips_empty_trailing_and_leading_spaces():
    service = UserService()

    assert service.register(" Björn", "123lol")
    assert service.login("Björn", "123lol")

    assert service.register("Toinen ", "123lol")
    assert service.login("Toinen", "123lol")

    assert service.register("Kolmas nimi", "123lol")
    assert service.login("Kolmas nimi", "123lol")

def test_login_returns_false_for_nonexistent_user():
    service = UserService()

    assert not service.login("Björn", "123lol")

