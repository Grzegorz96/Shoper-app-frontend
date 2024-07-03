import backend_requests
from tkinter import messagebox
from requests import codes
from utils import config_data


def move_to_deleted_announcements(user_completed_announcement_object, init_user_page_frame):
    """Function responsible for deleting a completed announcement. The announcement flag will change from completed to
     deleted."""
    # Calling the function sending a request to remove a given announcement.
    response_for_delete_of_announcement\
        = backend_requests.request_to_delete_the_announcement(user_completed_announcement_object.announcement_id)

    # If the returned response has a status of 200, then display a success message and refresh the page.
    if response_for_delete_of_announcement.status_code == codes.ok:
        messagebox.showinfo(f"Pomyślnie usunięto ogłoszenie.",
                            f"{config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_completed_announcement_object.title}\" zostało usunięte.")
        init_user_page_frame()

    # If the returned response has a status other than 200, then display an error message.
    else:
        messagebox.showerror("Błąd podczas usuwania ogłoszenia.",
                             f"Nie udalo sie usunąć Twojego ogłoszenia "
                             f"\"{user_completed_announcement_object.title}\", spróbuj później.")
