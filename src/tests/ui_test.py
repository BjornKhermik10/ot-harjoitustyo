from pathlib import Path
import sys
from tkinter import TclError, Tk

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

import ui.ui as ui_module


class _FakeUserService:
    def __init__(self):
        self.delete_calls = []

    def get_entries_for_user(self, username):
        return [
            {
                "id": 123,
                "prompt": "Prompt",
                "content": "Diary content",
                "created_at": "2026-04-20 10:00:00",
            }
        ]

    def delete_entry_for_user(self, username, entry_id):
        self.delete_calls.append((username, entry_id))
        return True


def _find_widget_with_text(widget, text):
    for child in widget.winfo_children():
        try:
            if child.cget("text") == text:
                return child
        except (TclError, ValueError):
            pass

        found = _find_widget_with_text(child, text)
        if found is not None:
            return found

    return None


def test_open_my_entries_delete_button_deletes_and_refreshes(monkeypatch):
    try:
        root = Tk()
    except TclError:
        pytest.skip("Tk could not be initialized in this environment")

    root.withdraw()
    service = _FakeUserService()
    ui = ui_module.UI(root, service)
    ui._current_user = "kalle123"

    monkeypatch.setattr(ui_module.messagebox, "askyesno", lambda *_args, **_kwargs: True)

    ui._open_my_entries()
    delete_button = _find_widget_with_text(ui._main_view, "Delete")
    assert delete_button is not None

    refresh_calls = []
    ui._open_my_entries = lambda: refresh_calls.append(True)

    delete_button.invoke()

    assert service.delete_calls == [("kalle123", 123)]
    assert refresh_calls == [True]

    root.destroy()
