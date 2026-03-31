from tkinter import Frame, Label, Button, messagebox


class UI:
    def __init__(self, root, user_service):
        self._root = root
        self._user_service = user_service
        self._main_view = None

    def start(self):
        self._show_main_view()

    def _clear_view(self):
        if self._main_view:
            self._main_view.destroy()

    def _show_main_view(self):
        self._clear_view()

        self._main_view = Frame(self._root, padx=24, pady=24)
        self._main_view.pack(fill="both", expand=True)

        title = Label(self._main_view, text="Dear Diary", font=("Helvetica", 20, "bold"))
        title.pack(pady=(0, 24))

        login_button = Button(
            self._main_view,
            text="Login",
            width=20,
            command=self._open_login,
        )
        login_button.pack(pady=6)

        signup_button = Button(
            self._main_view,
            text="Sign up",
            width=20,
            command=self._open_signup,
        )
        signup_button.pack(pady=6)

        about_button = Button(
            self._main_view,
            text="About",
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
