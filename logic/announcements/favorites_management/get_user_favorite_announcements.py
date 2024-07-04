from tkinter import messagebox
from requests import codes
from models.user_favorite_announcement import UserFavoriteAnnouncement
from utils.formating import convert_image_to_tkinter
from services.api.announcements import request_to_get_user_favorite_announcements


def get_user_favorite_announcements(active_flag, page, per_page):
    """Function responsible for downloading announcements belonging to the user, creating a list of announcements
    objects and returning this list."""
    # Calling the function sending a request to download the user's announcements.
    response_for_getting_user_favorite_announcements = request_to_get_user_favorite_announcements(active_flag, page,
                                                                                                  per_page)

    # If the returned response has a status of 200, the program will create a list of user's announcements objects from
    # the downloaded data.
    if response_for_getting_user_favorite_announcements.status_code == codes.ok:

        # Creating a list of user's favorite announcement objects.
        list_of_user_fav_announcement_objects = []

        # Iterate through the list of favorite announcements in the response.
        for favorite_announcement in response_for_getting_user_favorite_announcements.json()["result"]:
            if favorite_announcement["main_photo"]:
                # Convert the main photo to a format suitable for Tkinter if it exists.
                favorite_announcement["main_photo"] = convert_image_to_tkinter(favorite_announcement["main_photo"])

            # Create an instance of UserFavoriteAnnouncement with the data from the response.
            user_fav_announcement_object = UserFavoriteAnnouncement(
                favorite_announcement["favorite_announcement_id"],
                favorite_announcement["announcement_id"],
                favorite_announcement["first_name"],
                favorite_announcement["seller_id"],
                favorite_announcement["title"],
                favorite_announcement["description"],
                favorite_announcement["name_category"],
                favorite_announcement["price"],
                favorite_announcement["location"],
                favorite_announcement["main_photo"],
                favorite_announcement["state"],
                favorite_announcement["creation_date"],
                favorite_announcement["mobile_number"]
            )

            # Append the created object to the list
            list_of_user_fav_announcement_objects.append(user_fav_announcement_object)

        # Returning a list of user's announcement objects.
        return list_of_user_fav_announcement_objects

    # If the returned response has a status other than 200, then display an error message and return an empty list.
    else:
        messagebox.showerror("Błąd podczas wczytywania ulubionych ogłoszeń.",
                             "Nie udalo sie wczytać ulubionych ogłoszeń, spróbuj później.")
        return []
