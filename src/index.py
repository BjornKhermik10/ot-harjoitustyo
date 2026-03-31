from tkinter import Tk
from ui.ui import UI
from services.user_service import UserService

def main():
    window = Tk()
    window.title("Dear Diary")

    user_service = UserService()
    ui_view = UI(window, user_service)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()