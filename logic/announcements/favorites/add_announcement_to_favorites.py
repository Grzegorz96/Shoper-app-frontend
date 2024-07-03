import backend_requests
from utils import config_data
from tkinter import messagebox
from requests import codes


def add_announcement_to_favorites(announcement_object):
    """Function responsible for adding announcements to favorites."""
    # Checking if the user is logged in.
    if config_data.is_user_logged_in:

        # Calling the function sending a request to add the announcement to the user's favorites.
        response_for_adding_to_favorite \
            = backend_requests.request_to_add_announcement_to_favorite(announcement_object.announcement_id)

        # If the returned response has a status of 201, the program will display a success message.
        if response_for_adding_to_favorite.status_code == codes.created:
            messagebox.showinfo("Pomyślnie dodano do ulubionych.",
                                f"Ogłoszenie \"{announcement_object.title}\" zostało dodane do ulubionych.")

        # If the returned response has a status of 400, The program will display a message that the ad has already been
        # liked by the user.
        elif response_for_adding_to_favorite.status_code == codes.bad_request:
            messagebox.showwarning(
                f"{config_data.logged_in_user_info.first_name}, wybrane ogłoszenie znajduję sie już w ulubionych.",
                f"Ogłoszenie \"{announcement_object.title}\" znajduje się na Twojej liście ulubionych.")

        # If the returned response has a status other than 201 and 400, the program will display an error message.
        else:
            messagebox.showerror("Błąd podczas dodawania do ulubionych.",
                                 "Nie udalo sie dodać do ulubionych, spróbuj później.")

    # User not logged in message.
    else:
        messagebox.showwarning("Nie jesteś zalogowany.",
                               "Aby dodać ogłoszenie do ulubionych musisz sie zalogować.")
