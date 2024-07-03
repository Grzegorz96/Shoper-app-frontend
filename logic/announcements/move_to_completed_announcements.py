import backend_requests
from tkinter import messagebox
from requests import codes
from utils import config_data


def move_to_completed_announcements(user_active_announcement_object, init_user_page_frame):
    """Function responsible for ending the announcement. The announcement flag will change from active to completed."""
    # Calling the function sending a request to end the announcement.
    response_for_end_of_announcement\
        = backend_requests.request_to_complete_the_announcement(user_active_announcement_object.announcement_id)

    # If the returned response has a status of 200, then display a success message and refresh the page.
    if response_for_end_of_announcement.status_code == codes.ok:
        messagebox.showinfo(f"Pomyślnie zakończono ogłoszenie.",
                            f"{config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_active_announcement_object.title}\" zostało przeniesione do zakończonych.")
        init_user_page_frame()

    # If the returned response has a status other than 200, then display an error message.
    else:
        messagebox.showerror("Błąd podczas zakańczania ogłoszenia.",
                             f"Nie udalo sie zakończyć Twojego ogłoszenia "
                             f"\"{user_active_announcement_object.title}\", spróbuj później.")
