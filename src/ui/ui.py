"""This file is responsible for the main user interface and what happens when you click a button."""

from pathlib import Path
from tkinter import Text, Tk, Frame, Label, Entry, PhotoImage, messagebox
import customtkinter as ctk

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
    # generoitu koodi alkaa, sain ton _create_centered_group idean tekoälyltä
    def _create_centered_group(self):
        """Creates a centered container for grouping page widgets."""
        content = Frame(self._main_view, bg="#FEFBE7")
        content.place(relx=0.5, rely=0.5, anchor="center")
        return content
    # generoitu koodi loppuu
    def _show_main_view(self):
        """Shows the main view with options to login, sign up, or view about information."""
        self._clear_view()
        # generoitu koodi alkaa, sain siis ton _view_padx ja pady idean tekoälyltä
        self._main_view = Frame(
            self._root, padx=self._view_padx, pady=self._view_pady, bg="#FEFBE7")
        self._main_view.pack(fill="both", expand=True)
        # generoitu koodi loppuu

        content = self._create_centered_group()

        title = ctk.CTkLabel(content, text="DEAR DIARY",
                     font=("Arial", 38, "bold"),
                     text_color="#0F0099")
        title.pack(pady=(0, 48))

        # generoitu koodi alkaa, sain ton logo toteutus-idean tekoälyltä
        logo_path = Path(__file__).parent / "assets" / "logo.png"
        if self.logo is None:
            self.logo = PhotoImage(master=self._root, file=str(logo_path))
        logo_label = Label(content, image=self.logo, bg="#FEFBE7", highlightthickness=0)
        logo_label.pack(pady=(0, 24))
        # generoitu koodi loppuu

        login_button = ctk.CTkButton(
            content,
            text="LOGIN",
            text_color="#FFFFFF",
            corner_radius=8,    
            fg_color="#0F0099",
            hover_color="#171151",
            font=("Arial", 20, "bold"),
            width=220,
            command=self._open_login,
        )
        login_button.pack(pady=6)

        signup_button = ctk.CTkButton(
            content,
            text="SIGN UP",
            text_color="#FFFFFF",
            corner_radius=8,
            fg_color="#0F0099",
            hover_color="#171151",
            font=("Arial", 20, "bold"),
            width=220,
            command=self._open_signup,
        )
        signup_button.pack(pady=6)

        about_button = ctk.CTkButton(
            content,
            text="ABOUT",
            text_color="#FFFFFF",
            corner_radius=8,
            fg_color="#0F0099",
            hover_color="#171151",
            font=("Arial", 20, "bold"),
            width=220,
            command=self._open_about,
        )
        about_button.pack(pady=6)

    def _open_signup(self):
        """Opens the sign up view and registers a new user."""
        self._clear_view()

        self._main_view = Frame(
            self._root, padx=self._view_padx, pady=self._view_pady, bg="#FEFBE7")
        self._main_view.pack(fill="both", expand=True)

        content = self._create_centered_group()

        title = ctk.CTkLabel(
            content,
            text="SIGN UP",
            font=("Arial", 40, "bold"),
            text_color="#0F0099",
            fg_color="transparent",
            )
        title.pack(pady=(0, 36))

        form_frame = Frame(content, bg="#FEFBE7")
        form_frame.pack(pady=(0, 24))

        username_row = Frame(form_frame, bg="#FEFBE7")
        username_row.pack(pady=(0, 12))
        username_label = Label(
            username_row, text="Username", font=("Arial", 16), bg="#FEFBE7")
        username_label.pack(side="left")
        username_entry = Entry(username_row, font=("Arial", 16), width=24)
        username_entry.pack(side="left", padx=(12, 0))

        password_row = Frame(form_frame, bg="#FEFBE7")
        password_row.pack()
        password_label = Label(
            password_row, text="Password", font=("Arial", 16), bg="#FEFBE7")
        password_label.pack(side="left")
        password_entry = Entry(password_row, font=(
            "Arial", 16), width=24, show="*")
        password_entry.pack(side="left", padx=(12, 0))

        error_label = Label(content, text="",
                            fg="red", font=("Arial", 12), bg="#FEFBE7")
        error_label.pack(pady=(0, 10))

        def handle_signup():
            username = username_entry.get().strip()
            password = password_entry.get().strip()

            if not username or not password:
                error_label.config(text="Username and password are required.")
                return

            if self._user_service.register(username, password):
                messagebox.showinfo("Sign up", "Account created successfully.")
                self._show_main_view()
            else:
                error_label.config(text="Username already exists.")

        signup_button = ctk.CTkButton(
            content,
            text="CREATE ACCOUNT",
            text_color="#FFFFFF",
            corner_radius=8,
            fg_color="#0F0099",
            hover_color="#171151",
            font=("Arial", 16, "bold"),
            width=220,
            command=handle_signup,
        )
        signup_button.pack(pady=6)

        back_button = ctk.CTkButton(
            content,
            text="BACK",
            text_color="#FFFFFF",
            corner_radius=8,
            fg_color="#646466",
            hover_color="#3A3A3A",
            font=("Arial", 16, "bold"),
            width=220,
            command=self._show_main_view,
        )
        back_button.pack(pady=6)

    def _open_login(self):
        """Opens the login view and authenticates the user."""
        self._clear_view()

        self._main_view = Frame(
            self._root, padx=self._view_padx, pady=self._view_pady, bg="#FEFBE7")
        self._main_view.pack(fill="both", expand=True)

        content = self._create_centered_group()

        title = ctk.CTkLabel(
            content,
            text="LOGIN",
            font=("Arial", 40, "bold"),
            text_color="#0F0099",
            fg_color="transparent",
            )
        title.pack(pady=(0, 36))

        form_frame = Frame(content, bg="#FEFBE7")
        form_frame.pack(pady=(0, 24))

        username_row = Frame(form_frame, bg="#FEFBE7")
        username_row.pack(pady=(0, 12))
        username_label = Label(
            username_row, text="Username", font=("Arial", 16), bg="#FEFBE7")
        username_label.pack(side="left")
        username_entry = Entry(username_row, font=("Arial", 16), width=24)
        username_entry.pack(side="left", padx=(12, 0))

        password_row = Frame(form_frame, bg="#FEFBE7")
        password_row.pack()
        password_label = Label(
            password_row, text="Password", font=("Arial", 16), bg="#FEFBE7")
        password_label.pack(side="left")
        password_entry = Entry(password_row, font=(
            "Arial", 16), width=24, show="*")
        password_entry.pack(side="left", padx=(12, 0))

        error_label = Label(content, text="",
                            fg="red", font=("Arial", 12), bg="#FEFBE7")
        error_label.pack(pady=(0, 10))

        def handle_login():
            """Handles the login logic by checking the entered credentials."""
            username = username_entry.get().strip()
            password = password_entry.get().strip()

            if not username or not password:
                error_label.config(text="Username and password are required.")
                return

            if self._user_service.login(username, password):
                self._open_logged_in_view(username)
            else:
                error_label.config(text="Invalid username or password.")

        login_button = ctk.CTkButton(
            content,
            text="LOGIN",
            text_color="#FFFFFF",
            corner_radius=8,
            fg_color="#0F0099",
            hover_color="#171151",
            font=("Arial", 16, "bold"),
            width=220,
            command=handle_login,
        )
        login_button.pack(pady=6)

        back_button = ctk.CTkButton(
            content,
            text="BACK",
            text_color="#FFFFFF",
            corner_radius=8,
            fg_color="#646466",
            hover_color="#3A3A3A",
            font=("Arial", 16, "bold"),
            width=220,
            command=self._show_main_view,
        )
        back_button.pack(pady=6)

    def _open_logged_in_view(self, username):
        """Shows the logged-in view after a successful login."""
        self._clear_view()

        self._main_view = Frame(
            self._root, padx=self._view_padx, pady=self._view_pady, bg="#FEFBE7")
        self._main_view.pack(fill="both", expand=True)

        content = self._create_centered_group()

        title = ctk.CTkLabel(content, text="DEAR DIARY",
                     font=("Arial", 38, "bold"),
                     text_color="#0F0099")
        title.pack(pady=(0, 48))

        # generoitu koodi alkaa, sain ton logo toteutus-idean tekoälyltä
        logo_path = Path(__file__).parent / "assets" / "logo.png"
        if self.logo is None:
            self.logo = PhotoImage(master=self._root, file=str(logo_path))
        logo_label = Label(content, image=self.logo, bg="#FEFBE7", highlightthickness=0)
        logo_label.pack(pady=(0, 24))
        # generoitu koodi loppuu

        my_entries_button = ctk.CTkButton(
            content,
            text="My Entries",
            text_color="#FFFFFF",
            corner_radius=8,    
            fg_color="#0F0099",
            hover_color="#171151",
            font=("Arial", 20, "bold"),
            width=220,
            command=self._open_my_entries,
        )
        my_entries_button.pack(pady=6)

        daily_prompt = ctk.CTkButton(
            content,
            text="Daily Prompt",
            text_color="#FFFFFF",
            corner_radius=8,
            fg_color="#0F0099",
            hover_color="#171151",
            font=("Arial", 20, "bold"),
            width=220,
            command=self._open_daily_prompt,
        )
        daily_prompt.pack(pady=6)

    def _open_my_entries(self, username):
        """Shows my-entries view"""
        self._clear_view()

        self._main_view = Frame(
            self._root, padx=self._view_padx, pady=self._view_pady, bg="#FEFBE7")
        self._main_view.pack(fill="both", expand=True)

        content = self._create_centered_group()

        form_frame = Frame(content, bg="#FEFBE7")
        form_frame.pack(pady=(0, 5))

        username_row = Frame(form_frame, bg="#FEFBE7")
        username_row.pack(pady=(0, 12))
        username_label = Label(
            username_row, text="Username", font=("Arial", 16), bg="#FEFBE7")
        username_label.pack(side="left")
        username_entry = Entry(username_row, font=("Arial", 16), width=24)
        username_entry.pack(side="left", padx=(12, 0))

    def _open_daily_prompt(self, username):
            """Shows daily prompt view"""
            self._clear_view()

            self._main_view = Frame(
                self._root, padx=self._view_padx, pady=self._view_pady, bg="#FEFBE7")
            self._main_view.pack(fill="both", expand=True)

            content = self._create_centered_group()

            title = ctk.CTkLabel(content, text="DAILY PROMPT",
                                font=("Arial", 38, "bold"),
                                text_color="#0F0099")
            title.pack(pady=(0, 20))

            guidance_box = ctk.CTkLabel(
                content,
                text="What made today a better day?",
                fg_color="#FFF9C4",
                text_color="#5D4037",
                corner_radius=6,
                padx=15,
                pady=10
            )
            guidance_box.pack(pady=(0, 15))

            form_frame = Frame(content, bg="#FEFBE7")
            form_frame.pack(pady=(0, 5))

            daily_prompt_row = Frame(form_frame, bg="#FEFBE7")
            daily_prompt_row.pack(pady=(0, 0))
            
            daily_prompt_label = ctk.CTkLabel(
                daily_prompt_row, text="Start Writing:", font=("Arial", 12, "bold"), text_color="#0F0099")
            daily_prompt_label.pack(side="top", anchor="w")
            
            daily_prompt_entry = Text(daily_prompt_row, font=("Arial", 16), width=30, height=12, padx=20, pady=6, spacing3=6)
            daily_prompt_entry.pack(side="top")

            button_row = Frame(content, bg="#FEFBE7")
            button_row.pack(fill="x", pady=(10, 0))

            preview_submission = ctk.CTkButton(
                button_row,
                text="Preview",
                text_color="#FFFFFF",
                corner_radius=8,
                fg_color="#0F0099",
                hover_color="#171151",
                font=("Arial", 20, "bold"),
                width=150,
                command=self._open_preview_submission,
            )
            preview_submission.pack(side="right")

            back_to_logged_in_view = ctk.CTkButton(
                button_row,
                text="Back",
                text_color="#FFFFFF",
                corner_radius=8,
                fg_color="#646466",
                hover_color="#3A3A3A",
                font=("Arial", 20, "bold"),
                width=150,
                command=self._open_logged_in_view,
            )
            back_to_logged_in_view.pack(side="left")
    
    def _open_preview_submission(self):
        """Shows information about the application."""
        messagebox.showinfo(
            "About",
            "Dear Diary helps you keep your diary entries organized and inspires you with daily prompts."
        )
    def _open_about(self):
        """Shows information about the application."""
        messagebox.showinfo(
            "About",
            "Dear Diary helps you keep your diary entries organized and inspires you with daily prompts."
        )
