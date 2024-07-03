from tkinter import messagebox
from requests import codes
from models import Announcement
import backend_requests
from utils.formating import convert_image_to_tkinter


def get_user_announcements(active_flag, page):
    """The function is responsible for triggering a request to download the user's announcements, creating a list of
    objects for these announcements and returning them to the gui.py module. In the function parameters, the program
    specifies which page it wants to display and whether announcements are active or completed."""
    # Calling the user announcement request function.
    response_for_getting_user_announcements = backend_requests.request_to_get_user_announcements(active_flag, page)

    # If a response with status 200 is returned, then within the number of dictionaries in the list,
    # create announcement objects.
    if response_for_getting_user_announcements.status_code == codes.ok:

        # Creating a list of objects for user announcements.
        list_of_objects_user_announcements = []

        # Iterate through the list of announcements in the response.
        for announcement in response_for_getting_user_announcements.json()["result"]:
            if announcement["main_photo"]:
                # Convert the main photo to a tkinter image.
                announcement["main_photo"] = convert_image_to_tkinter(announcement["main_photo"])

            # Create an object for the announcement.
            user_announcement_object = Announcement(
                announcement["announcement_id"],
                announcement["first_name"],
                announcement["seller_id"],
                announcement["name_category"],
                announcement["category_id"],
                announcement["title"],
                announcement["description"],
                announcement["price"],
                announcement["location"],
                announcement["main_photo"],
                announcement["state"],
                announcement["creation_date"],
                announcement["mobile_number"]
            )

            # Add the created object to the list.
            list_of_objects_user_announcements.append(user_announcement_object)

        # Returning a list of objects.
        return list_of_objects_user_announcements

    # If you receive a response with a status other than 200, display an error message and return an empty list.
    else:
        messagebox.showerror("Błąd podczas wczytywania ogłoszeń.",
                             "Nie udalo sie wczytać Twoich ogłoszeń, spróbuj później.")
        return []
