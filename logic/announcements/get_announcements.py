from tkinter import messagebox
from requests import codes
from utils import constants
from models.announcement import Announcement
from utils.formating import convert_image_to_tkinter
from services.api.announcements import request_to_get_announcements


def get_announcements(page, first_init, search_engine, search_location=None, current_var_category=None):
    """Function responsible for downloading announcements on the home page. When the user calls the function from
     search_engine, the user specifies the parameters with which he wants to download announcements."""
    # If the function was called from search_engine, the program will assign the imported values to the variables.
    if search_engine:
        content_to_search = search_engine.get()
        location = search_location.get()
        category_id = constants.categories.index(current_var_category.get()) + 1 if (
                current_var_category.get() in constants.categories) else ""

        # Calling a function sending a request to download a message with specific additional parameters.
        response_for_getting_announcements = request_to_get_announcements(search_engine, page, content_to_search,
                                                                          location, category_id)

    # If the function is called not from search_engine, announcements will be downloaded without additional parameters.
    else:
        response_for_getting_announcements = request_to_get_announcements(search_engine, page)

    # # If the returned response has a status of 200, the program will create a list of announcements objects from the
    # downloaded data.
    if response_for_getting_announcements.status_code == codes.ok:

        # If any announcements are downloaded, the program creates a list of objects.
        if response_for_getting_announcements.json()["result"]:

            # Creating a list of announcement objects.
            list_of_objects_announcements = []

            # Iterate through the list of announcements in the response.
            for announcement in response_for_getting_announcements.json()["result"]:
                # If the main photo exists, convert it to a format suitable for Tkinter.
                if announcement["main_photo"]:
                    announcement["main_photo"] = convert_image_to_tkinter(announcement["main_photo"])

                # Create an instance of Announcement with the data from the response.
                announcement_object = Announcement(
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

                # Append the created object to the list.
                list_of_objects_announcements.append(announcement_object)

            # Returning a list of announcement objects.
            return list_of_objects_announcements

        # If an empty list is returned, it means that no announcements were found for the given parameters.
        # Calling the function with first_init means that the user is searching for announcements for the first time
        # (not from pagination) and should be informed about their absence. Calling the function without first_init is
        # calling the function from pagination, so there is no need to inform the user.
        else:
            if first_init:
                messagebox.showwarning("Nie znaleźliśmy żadnych ogłoszeń.",
                                       "Przykro nam, nie znaleźliśmy wyników dla Twoich kryteriów wyszukiwania.")
            return []

    # If the returned response has a status other than 200, then display an error message and return an empty list.
    else:
        messagebox.showerror("Błąd podczas wczytywania ogłoszeń.",
                             "Nie udalo sie pobrać ogłoszeń, spróbuj ponownie później.")
        return []
