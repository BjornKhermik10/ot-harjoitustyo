"""This file is responsible for the main user interface and what happens when you click a button."""

from pathlib import Path
from tkinter import Frame, Label, Button, Entry, PhotoImage, messagebox

class UI:
    def __init__(self, root, user_service):
        """Initializes the UI with the root window and user service."""
        self._root = root
        self._user_service = user_service
        self._main_view = None
        self.logo = None
        self._view_padx = 40
        self._view_pady = 24

    def start(self):
        """Starts the UI by showing the main view."""
        self._root.geometry("960x640")
        self._root.minsize(960, 640)
        self._show_main_view()

    def _clear_view(self):
        """Clears the current view by destroying the main view frame."""
        if self._main_view:
            self._main_view.destroy()

    def _show_main_view(self):
        """Shows the main view with options to login, sign up, or view about information."""
        self._clear_view()

        self._main_view = Frame(self._root, padx=self._view_padx, pady=self._view_pady)
        self._main_view.pack(fill="both", expand=True)

        title = Label(self._main_view, text="DEAR DIARY", font=("Arial", 38, "bold"))
        title.pack(pady=(0, 48))

        logo_path = Path(__file__).parent / "assets" / "logo.png"
        if self.logo is None:
            self.logo = PhotoImage(file=str(logo_path))

        logo_label = Label(self._main_view, image=self.logo)
        logo_label.pack(pady=(0, 24))

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

    def _open_signup(self):
        """Opens the sign up view and registers a new user."""
        self._clear_view()

        self._main_view = Frame(self._root, padx=self._view_padx, pady=self._view_pady)
        self._main_view.pack(fill="both", expand=True)

        title = Label(self._main_view, text="SIGN UP", font=("Arial", 40, "bold"))
        title.pack(pady=(0, 36))

        username_label = Label(self._main_view, text="Username", font=("Arial", 16))
        username_label.pack(anchor="w")
        username_entry = Entry(self._main_view, font=("Arial", 16), width=24)
        username_entry.pack(pady=(0, 18))

        password_label = Label(self._main_view, text="Password", font=("Arial", 16))
        password_label.pack(anchor="w")
        password_entry = Entry(self._main_view, font=("Arial", 16), width=24, show="*")
        password_entry.pack(pady=(0, 24))

        error_label = Label(self._main_view, text="", fg="red", font=("Arial", 12))
        error_label.pack(pady=(0, 10))

        def handle_signup():
            username = username_entry.get().strip()
            password = password_entry.get().strip()

            if not username or not password:
                error_label.config(text="Username and password are required.")
                return

            if self._user_service.register(username, password):
                messagebox.showinfo("Sign up", "Account created successfully.")
                self._open_login()
            else:
                error_label.config(text="Username already exists.")

        signup_button = Button(
            self._main_view,
            text="Create account",
            font=("Arial", 16),
            width=20,
            command=handle_signup,
        )
        signup_button.pack(pady=6)

        back_button = Button(
            self._main_view,
            text="Back",
            font=("Arial", 16),
            width=20,
            command=self._show_main_view,
        )
        back_button.pack(pady=6)

    def _open_login(self):
        """Opens the login view and authenticates the user."""
        self._clear_view()

        self._main_view = Frame(self._root, padx=self._view_padx, pady=self._view_pady)
        self._main_view.pack(fill="both", expand=True)

        title = Label(self._main_view, text="LOGIN", font=("Arial", 40, "bold"))
        title.pack(pady=(0, 36))

        username_label = Label(self._main_view, text="Username", font=("Arial", 16))
        username_label.pack(anchor="w")
        username_entry = Entry(self._main_view, font=("Arial", 16), width=24)
        username_entry.pack(pady=(0, 18))

        password_label = Label(self._main_view, text="Password", font=("Arial", 16))
        password_label.pack(anchor="w")
        password_entry = Entry(self._main_view, font=("Arial", 16), width=24, show="*")
        password_entry.pack(pady=(0, 24))

        error_label = Label(self._main_view, text="", fg="red", font=("Arial", 12))
        error_label.pack(pady=(0, 10))

        def handle_login():
            """Handles the login logic by checking the entered credentials."""
            username = username_entry.get().strip()
            password = password_entry.get().strip()

            if not username or not password:
                error_label.config(text="Username and password are required.")
                return

            if self._user_service.login(username, password):
                self._show_logged_in_view(username)
            else:
                error_label.config(text="Invalid username or password.")

        login_button = Button(
            self._main_view,
            text="Login",
            font=("Arial", 16),
            width=20,
            command=handle_login,
        )
        login_button.pack(pady=6)

        back_button = Button(
            self._main_view,
            text="Back",
            font=("Arial", 16),
            width=20,
            command=self._show_main_view,
        )
        back_button.pack(pady=6)

    def _show_logged_in_view(self, username):
        """Shows the success view after a successful login."""
        self._clear_view()

        self._main_view = Frame(self._root, padx=self._view_padx, pady=self._view_pady)
        self._main_view.pack(fill="both", expand=True)

        title = Label(self._main_view, text="You got logged in", font=("Arial", 34, "bold"))
        title.pack(pady=(0, 24))

        subtitle = Label(
            self._main_view,
            text=f"Welcome, {username}. This will become the default user home view later.",
            font=("Arial", 16),
            wraplength=560,
            justify="center",
        )
        subtitle.pack(pady=(0, 24))

        continue_button = Button(
            self._main_view,
            text="Continue",
            font=("Arial", 16),
            width=20,
            command=self._show_main_view,
        )
        continue_button.pack(pady=6)

    def _open_about(self):
        """Shows information about the application."""
        messagebox.showinfo(
            "About",
            "Dear Diary helps you keep your diary entries organized and inspires you with daily prompts.",
        )
