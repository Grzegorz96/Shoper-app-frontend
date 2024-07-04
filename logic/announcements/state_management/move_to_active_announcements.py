from tkinter import messagebox
from requests import codes
from utils import config_data
from services.api.announcements import request_to_restore_the_announcement


def move_to_active_announcements(user_completed_announcement_object, init_user_page_frame):
    """Function responsible for restoring the announcement. The announcement flag will change from completed to
    active."""
    # Calling a function sending a request to restore a given announcement to the active state.
    response_for_restore_of_announcement = request_to_restore_the_announcement(
        user_completed_announcement_object.announcement_id)

    # If the returned response has a status of 200, then display a success message and refresh the page.
    if response_for_restore_of_announcement.status_code == codes.ok:
        messagebox.showinfo("Pomyślnie aktywowano ogłoszenie.",
                            f"{config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_completed_announcement_object.title}\" zostało aktywowane.")
        init_user_page_frame()

    # If the returned response has a status other than 200, then display an error message.
    else:
        messagebox.showerror("Błąd podczas aktywowania ogłoszenia.",
                             f"Nie udalo sie aktywować Twojego ogłoszenia "
                             f"\"{user_completed_announcement_object.title}\", spróbuj później.")
        