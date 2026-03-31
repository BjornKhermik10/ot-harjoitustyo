"""This file is responsible for the main user interface and what happens when you click a button."""

from tkinter import Frame, Label, Button, messagebox


class UI:
    def __init__(self, root, user_service):
        """Initializes the UI with the root window and user service."""
        self._root = root
        self._user_service = user_service
        self._main_view = None

    def start(self):
        """Starts the UI by showing the main view."""
        self._show_main_view()

    def _clear_view(self):
        """Clears the current view by destroying the main view frame."""
        if self._main_view:
            self._main_view.destroy()

    def _show_main_view(self):
        """Shows the main view with options to login, sign up, or view about information."""
        self._clear_view()

        self._main_view = Frame(self._root, padx=350, pady=150)
        self._main_view.pack(fill="both", expand=True)

        title = Label(self._main_view, text="DEAR DIARY", font=("Arial", 50, "bold"))
        title.pack(pady=(0, 128))

        login_button = Button(
            self._main_view,
            text="Login",
            font=("Arial", 20),
            width=20,
            command=self._open_login,
        )
        login_button.pack(pady=6)

        signup_button = Button(
            self._main_view,
            text="Sign up",
            font=("Arial", 20),
            width=20,
            command=self._open_signup,
        )
        signup_button.pack(pady=6)

        about_button = Button(
            self._main_view,
            text="About",
            font=("Arial", 20),
            width=20,
            command=self._open_about,
        )
        about_button.pack(pady=6)

    def _open_login(self):
        messagebox.showinfo("Login", "Here will be login view.")

    def _open_signup(self):
        messagebox.showinfo("Sign up", "Here will be sign up view.")

    def _open_about(self):
        messagebox.showinfo(
            "About",
            "Dear Diary helps you keep your diary entries organized and inspires you with daily prompts.",
        )
