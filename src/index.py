from tkinter import Tk
from pathlib import Path

from data.database import Database, initialize_database
from repositories.entry_repository import EntryRepository
from repositories.user_repository import UserRepository
from ui.ui import UI
from services.user_service import UserService
import customtkinter as ctk


def main():
    window = Tk()
    window.title("Dear Diary")

    db_path = Path(__file__).parent / "data" / "app.db"
    database = Database(db_path)
    connection = database.get_connection()
    initialize_database(connection)

    user_repository = UserRepository(connection)
    entry_repository = EntryRepository(connection)
    user_service = UserService(user_repository, entry_repository)
    ui_view = UI(window, user_service)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
