from utils import config_data
from tkinter import messagebox


def logout_user(logout_button, user_name, init_shoper_page_frame):
    """The function responsible for logging out the user deletes the user object, changes the login flag to False,
    destroys the created message objects, destroys the logout button, initializes the main application page and
    displays an appropriate message."""
    # Deleting data from user object.
    config_data.logged_in_user_info = None

    # Destroying windows of messages.
    for window in config_data.list_of_active_windows:
        window.destroy()

    # Destroying button object, init main page of app and displaying message.
    config_data.list_of_active_windows.clear()
    logout_button.destroy()
    init_shoper_page_frame()
    messagebox.showinfo("Pomyślnie wylogowano.", f"Użytkownik {user_name} został pomyślnie wylogowany.")
