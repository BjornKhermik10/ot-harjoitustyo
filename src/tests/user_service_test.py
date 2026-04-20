from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from data.database import Database, initialize_database
from repositories.entry_repository import EntryRepository
from repositories.user_repository import UserRepository
from services.user_service import UserService


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

def test_user_cannot_register_login_with_empty_username_and_or_password():
    service = UserService()

    assert not service.register("", "123lol")
    assert not service.login("", "123lol")
    assert not service.register("Björn", "")
    assert not service.login("Björn", "")
    assert not service.register("", "")
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


def test_user_can_store_and_read_entries():
    service = UserService()

    assert service.register("Björn", "123lol")
    assert service.add_entry("Björn", "Prompt", "Today was awesome")

    entries = service.get_entries_for_user("Björn")
    assert len(entries) == 1
    assert entries[0]["prompt"] == "Prompt"
    assert entries[0]["content"] == "Today was awesome"


def test_data_persists_when_using_file_database(tmp_path):
    db_path = tmp_path / "app.db"

    db_1 = Database(db_path)
    conn_1 = db_1.get_connection()
    initialize_database(conn_1)
    service_1 = UserService(UserRepository(conn_1), EntryRepository(conn_1))

    assert service_1.register("Björn", "123lol")
    assert service_1.add_entry("Björn", "Prompt", "working?")

    db_2 = Database(db_path)
    conn_2 = db_2.get_connection()
    initialize_database(conn_2)
    service_2 = UserService(UserRepository(conn_2), EntryRepository(conn_2))

    assert service_2.login("Björn", "123lol")
    entries = service_2.get_entries_for_user("Björn")
    assert len(entries) == 1
    assert entries[0]["content"] == "working?"

def test_user_can_delete_entries():
    service = UserService()

    assert service.register("Björn", "123lol")
    assert service.add_entry("Björn", "Prompt", "Today was awesome")
    assert service.add_entry("Björn", "Prompt2", "gonnadeletethis")

    entries = service.get_entries_for_user("Björn")
    entry_id = entries[1]["id"]
    assert service.delete_entry_for_user("Björn", entry_id)

    assert len(service.get_entries_for_user("Björn")) == 1

def test_user_cannot_delete_entry_of_another_user():
    service = UserService()

    assert service.register("Björn", "123lol")
    assert service.register("Kalle", "1234lol")
    assert service.add_entry("Björn", "Prompt", "Today was awesome")

    entries = service.get_entries_for_user("Björn")
    entry_id = entries[0]["id"]
    assert not service.delete_entry_for_user("Kalle", entry_id)
    assert len(service.get_entries_for_user("Björn")) == 1

def test_signup_view_validation():
    service = UserService()

    assert not service.register("", "123lol")
    assert not service.register("Björn", "")
    assert not service.register(" ", "123lol")
    assert not service.register("Björn", " ")