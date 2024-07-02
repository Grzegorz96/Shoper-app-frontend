# Import the tkinter module.
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
# Import re module to validation.
from re import match
# Import classes
from classes import  Announcement, UserFavoriteAnnouncement, Message, Conversation
# Import global variables.
import config_data
# Import a module with the necessary functions to connect to the backend.
import backend_requests
# Import other modules.
from requests import codes
from PIL import Image, ImageTk
import os
from io import BytesIO
import zipfile
from helpers import convert_image_to_tkinter


def change_user_data(entry, label, hidden_password):
    """The function responsible for changing user data, validating the entered data, determining what the user wants
    to change, sending it to the backend and changing the value in the user object."""
    # Assigning the entered data to variables.
    value = entry.get()
    column = None
    attribute = None

    # If the given string is included in the imported label object, then the program validates the entered data for
    # this key. Overwrites the column and attribute variables.
    if "Imie:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", value):
            column = "first_name"
            attribute = "Imie:"
        else:
            messagebox.showwarning("Niepoprawne imię.", "Wprowadzono niepoprawne dane imienia.")

    # If the given string is included in the imported label object, then the program validates the entered data for
    # this key. Overwrites the column and attribute variables.
    elif "Nazwisko:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", value):
            column = "last_name"
            attribute = "Nazwisko:"
        else:
            messagebox.showwarning("Niepoprawne nazwisko.", "Wprowadzono niepoprawne dane nazwiska.")

    # If the given string is included in the imported label object, then the program validates the entered data for
    # this key. Overwrites the column and attribute variables.
    elif "Email:" in label["text"]:
        if match(
                "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+"
                "|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$",
                value):
            column = "email"
            attribute = "Email:"
        else:
            messagebox.showwarning("Niepoprawny email.", "Wprowadzono niepoprawne dane email.")

    # If the given string is included in the imported label object, then the program validates the entered data for
    # this key. Overwrites the column and attribute variables.
    elif "Hasło:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", value):
            column = "password"
            attribute = "Hasło:"
        else:
            messagebox.showwarning("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")

    # If the given string is included in the imported label object, overwrites the column and attribute variables.
    elif "Ulica:" in label["text"]:
        column = "street"
        attribute = "Ulica:"

    # If the given string is included in the imported label object, overwrites the column and attribute variables.
    elif "Kod pocztowy:" in label["text"]:
        column = "zip_code"
        attribute = "Kod pocztowy:"

    # If the given string is included in the imported label object, overwrites the column and attribute variables.
    elif "Miasto:" in label["text"]:
        column = "city"
        attribute = "Miasto:"

    # If it entered a block and created a column.
    if column:
        # Calling the function to send a user update request for a specific column with a validated value.
        response_for_updating_user = backend_requests.request_to_update_user_data(column, value)

        # If the status code is 200 then update the given field in the user object.
        if response_for_updating_user.status_code == codes.ok:
            if column == "first_name":
                config_data.logged_in_user_info.change_user_firstname(value)
            elif column == "last_name":
                config_data.logged_in_user_info.change_user_lastname(value)
            elif column == "email":
                config_data.logged_in_user_info.change_user_email(value)
            elif column == "password":
                config_data.logged_in_user_info.change_user_password(value)
            elif column == "street":
                config_data.logged_in_user_info.change_user_street(value)
            elif column == "zip_code":
                config_data.logged_in_user_info.change_user_zip_code(value)
            elif column == "city":
                config_data.logged_in_user_info.change_user_city(value)

            # Label update on the user's website.
            if column == "password" and hidden_password:
                label.config(text=f"{attribute} {'*'*len(value)}")
            else:
                label.config(text=f"{attribute} {value}")
            # Delete the entered text in the imported object.
            entry.delete(0, END)
            # Display success message.
            messagebox.showinfo("Pomyślnie zaktualizowano profil użytkownika.",
                                f"Twoj profil został zaktualizowany, {config_data.logged_in_user_info.first_name}.")

        # If response satus is 400.
        elif response_for_updating_user.status_code == codes.bad_request:
            # When the user wants to change the email address to one already in the database.
            if "email_error" in response_for_updating_user.json():
                messagebox.showwarning("Nie udało sie zaktualizować emaila.",
                                       "Podany email jest już zarejestrowany.")

            # If the user enters unvalidated data, it is impossible in this program because the frontend validates
            # everything.
            else:
                messagebox.showwarning("Nie udało sie zaktualizować użytkownika.",
                                       "Wprowadzono niepoprawne dane do aktualizacji użytkownika.")

        # If we receive a response with a status other than 200 or 400, display error message.
        else:
            messagebox.showerror("Błąd podczas aktualizacji użytkownika.",
                                 "Nie udało sie zaktualizować użytkownika, spróbuj później.")


def move_active_announcement_to_completed_announcements(user_active_announcement_object, init_user_page_frame):
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


def move_completed_announcement_to_active_announcements(user_completed_announcement_object, init_user_page_frame):
    """Function responsible for restoring the announcement. The announcement flag will change from completed to
    active."""
    # Calling a function sending a request to restore a given announcement to the active state.
    response_for_restore_of_announcement\
        = backend_requests.request_to_restore_the_announcement(user_completed_announcement_object.announcement_id)

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


def delete_from_completed_announcements(user_completed_announcement_object, init_user_page_frame):
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


def download_announcements(page, first_init, search_engine, search_location=None, current_var_category=None):
    """Function responsible for downloading announcements on the home page. When the user calls the function from
     search_engine, the user specifies the parameters with which he wants to download announcements."""
    # If the function was called from search_engine, the program will assign the imported values to the variables.
    if search_engine:
        content_to_search = search_engine.get()
        location = search_location.get()
        category_id = config_data.categories.index(current_var_category.get()) + 1 if (
                current_var_category.get() in config_data.categories) else ""

        # Calling a function sending a request to download a message with specific additional parameters.
        response_for_getting_announcements = backend_requests.request_to_get_announcements(search_engine, page,
                                                                                           content_to_search, location,
                                                                                           category_id)

    # If the function is called not from search_engine, announcements will be downloaded without additional parameters.
    else:
        response_for_getting_announcements = backend_requests.request_to_get_announcements(search_engine, page)

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


def download_user_favorite_announcements(active_flag, page, per_page):
    """Function responsible for downloading announcements belonging to the user, creating a list of announcements
    objects and returning this list."""
    # Calling the function sending a request to download the user's announcements.
    response_for_getting_user_favorite_announcements = backend_requests.request_to_get_user_favorite_announcements(
        active_flag, page, per_page)

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


def add_announcement_to_favorite(announcement_object):
    """Function responsible for adding announcements to favorites."""
    # Checking if the user is logged in.
    if config_data.is_user_logged_in:

        # Calling the function sending a request to add the announcement to the user's favorites.
        response_for_adding_to_favorite\
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


def delete_announcement_from_favorite(user_fav_announcement_object, init_favorite_page_frame):
    response_for_deleting_announcement_from_favorite\
        = backend_requests.request_to_delete_announcement_from_favorite(user_fav_announcement_object.
                                                                        favorite_announcement_id)

    if response_for_deleting_announcement_from_favorite.status_code == codes.ok:
        messagebox.showinfo("Pomyślnie usunięto z ulubionych.",
                            f"Ogłoszenie \"{user_fav_announcement_object.title}\" zostało usunięte z ulubionych.")
        init_favorite_page_frame()

    else:
        messagebox.showerror("Błąd podczas usuwania z ulubionych.",
                             "Nie udalo sie usunąć z ulubionych.")


def download_messages(announcement_object=None, conversation_object=None):
    """Function responsible for retrieving user's messages using conversation id or announcement id."""
    # If the user has imported a conversation object, the program sends a request with the conversation_id parameter.
    if conversation_object:
        response_for_getting_messages\
            = backend_requests.request_to_get_messages(conversation_id=conversation_object.conversation_id)

    # If the user has not imported the conversation id, it means that he has imported the announcement id,
    # the program will send a request with the announcement_id parameter.
    else:
        response_for_getting_messages\
            = backend_requests.request_to_get_messages(announcement_id=announcement_object.announcement_id)

    # If the returned response has a status of 200, the program will create list of message objects for the downloaded
    # conversation.
    if response_for_getting_messages.status_code == codes.ok:

        list_of_messages_objects = []
        for message in response_for_getting_messages.json()["result"]:
            message_object = Message(
                message["conversation_id"],
                message["message_id"],
                message["customer_flag"],
                message["content"],
                message["post_date"],
                message["user_id"],
                message["first_name"]
            )
            list_of_messages_objects.append(message_object)

        # Return a list of message objects
        return list_of_messages_objects

    # If the returned response has a status of 200, the program will display an error message and return empty list.
    else:
        messagebox.showerror("Błąd podczas wczytywania wiadomości.",
                             "Nie udalo sie wczytać wiadomości, spróbuj później.")
        return []


def send_message(list_of_message_objects, message_entry, refresh_messages, is_user_customer, announcement_object=None):
    """Function responsible for sending the entered message text to the database."""
    # Validation of entered data.
    if message_entry.get() != "":
        if message_entry.get() != "Napisz wiadomość...":

            # If validation is successful, the program checks whether the imported message list contains any objects,
            # if so it will retrieve the conversation id from the object and send the request.
            if list_of_message_objects:
                conversation_id = list_of_message_objects[0].conversation_id
                response_for_sending_message = backend_requests.request_to_send_message(message_entry.get(),
                                                                                        is_user_customer,
                                                                                        conversation_id=conversation_id)

            # If the user does not yet have a message for a given announcement, a request will be sent with the given
            # announcement_id to first create conversations for a given announcement and then create a message for the
            # conversation.
            else:
                announcement_id = announcement_object.announcement_id
                response_for_sending_message = backend_requests.request_to_send_message(message_entry.get(),
                                                                                        is_user_customer,
                                                                                        announcement_id=announcement_id)

            # If the returned response has a status of 201, the program will clear message_entry object and will trigger
            # the message refresh function.
            if response_for_sending_message.status_code == codes.created:
                message_entry.delete(0, END)
                refresh_messages()

            # If the returned response has a status of 201, the program will display an error message.
            else:
                messagebox.showerror("Błąd podczas wysyłania wiadomości.",
                                     "Nie udalo sie wysłać wiadomości, spróbuj później.")

        # Validation failure message.
        else:
            messagebox.showwarning("Błądna wiadomość.", "Aby wysłać, najpierw napisz wiadomość.")

    # Validation failure message.
    else:
        messagebox.showwarning("Błędna wiadomość.", "Nie możesz wysłać pustej wiadomości.")


def download_conversations(customer_flag, page):
    """Function responsible for downloading user conversations, specifying the customer_flag and page parameters.
    The function can download conversations for the user as a customer and as a seller."""
    # Calling the function sending a request to download the conversation.
    response_for_getting_conversations = backend_requests.request_to_get_conversations(customer_flag, page)

    # If the returned response has a status of 200, the program will create list of conversation objects.
    if response_for_getting_conversations.status_code == codes.ok:

        list_of_conversations = []
        for conversation in response_for_getting_conversations.json()["result"]:
            conv_object = Conversation(
                conversation["conversation_id"],
                conversation["announcement_id"],
                conversation["title"],
                conversation["first_name"]
            )
            list_of_conversations.append(conv_object)

        # Return list of conversations.
        return list_of_conversations

    # If the returned response has a status of 200, the program will display an error message and return an empty list.
    else:
        messagebox.showerror("Błąd podczas wczytywania konwersacji.",
                             "Nie udalo sie wczytać konwersacji, spróbuj później.")
        return []


def download_photos_to_announcement(announcement_id, to_edit, px, py):
    """A function that downloads photos for a given announcement."""
    list_of_photos = []
    error_with_getting_photos = False
    main_photo_filename = None

    try:
        # Calling the function sending a request to download photos for a given announcement.
        response = backend_requests.request_to_get_images(announcement_id)
        # If the returned response has a status of 200, the program will create a list of photo objects.
        if response.status_code == codes.ok:
            # If the response contains the 'X-Main-Photo' header, the program will assign the value to the variable.
            if 'X-Main-Photo' in response.headers:
                main_photo_filename = response.headers['X-Main-Photo']

            # Create a BytesIO buffer from the response content (ZIP file).
            zip_buffer = BytesIO(response.content)

            # Open the ZIP file for reading.
            with zipfile.ZipFile(zip_buffer, 'r') as zip_file:
                # Iterate through each file in the ZIP archive.
                for file_name in zip_file.namelist():
                    # Open the file within the ZIP archive.
                    with zip_file.open(file_name) as file:
                        # Read the file content into a BytesIO object.
                        img_data = BytesIO(file.read())
                        # Open the image using PIL.
                        image = Image.open(img_data)
                        # Resize the image to the specified dimensions, maintaining aspect ratio.
                        image.thumbnail((px, py), resample=Image.LANCZOS)
                        # Convert the image to a format suitable for use with Tkinter.
                        photo = ImageTk.PhotoImage(image)
                        # If editing is enabled, append a tuple with photo, filename, and main photo flag.
                        if to_edit:
                            list_of_photos.append((photo, file_name, main_photo_filename == file_name))
                        else:
                            # Otherwise, just append the photo.
                            list_of_photos.append(photo)

        else:
            # If the response status is not OK, set error flag and show error message.
            error_with_getting_photos = True
            messagebox.showerror("Błąd podczas wczytywania zdjęć.",
                                 "Nie udało się wczytać zdjęć lub ich części, spróbuj później.")

    except (zipfile.BadZipFile, IOError, FileNotFoundError, OSError, ValueError, KeyError, EOFError):
        # If an error occurs while downloading photos, the program will display an error message.
        error_with_getting_photos = True
        messagebox.showerror("Błąd podczas wczytywania zdjęć.",
                             "Nie udało się wczytać zdjęć lub ich części, spróbuj później.")

    # Return the list of photos and the error flag.
    return list_of_photos, error_with_getting_photos


def loading_images():
    """The function is launched when the program starts from the main.py module. The function is responsible for loading
    static graphic files and assigning them to the global dictionary."""
    # The program tries to load photos from your computer.
    try:
        config_data.images["arrows"] = [ImageTk.PhotoImage(Image.open("./assets/images/left.png").resize((50, 50))),
                                        ImageTk.PhotoImage(Image.open("./assets/images/right.png").resize((50, 50)))]
    # If an error occurs while loading, the program will assign the value None to the dictionary keys.
    except FileNotFoundError:
        config_data.images["arrows"] = [None, None]
        
    try:
        config_data.images["camera_icon"] = ImageTk.PhotoImage(Image.open(
            "./assets/images/camera_icon.png").resize((50, 50)))
    except FileNotFoundError:
        config_data.images["camera_icon"] = None


def config_buttons(actual_page, button_previous, button_next, collection, function, list_of_objects, objects_on_page):
    """The function responsible for configuring buttons for switching pages in the program."""
    # If the imported page number is greater than 1, the program updates the page back function.
    if 1 < actual_page:
        button_previous.config(command=lambda: function(actual_page - 1, list_of_objects))
    # Otherwise, it will update the button functions by assigning None.
    else:
        button_previous.config(command=lambda: None)

    # If the length of the retrieved object collection is equal to the number of objects displayed on the page,
    # the program updates the next page function.
    if len(collection) == objects_on_page:
        button_next.config(command=lambda: function(actual_page + 1, list_of_objects))
    # Otherwise, it will update the button functions by assigning None.
    else:
        button_next.config(command=lambda: None)


def create_buttons(page, x1, x2):
    """The function responsible for creating page change button objects for given page objects and returning them to
    the function."""
    # Creating buttons for a specific page and a specific x value.
    button_previous = Button(page, text="Poprzednia", font=("Arial", 8), borderwidth=0, bg="#D3D3D3")
    button_previous.place(x=x1, y=600, width=60, height=32)
    button_next = Button(page, text="Następna", font=("Arial", 8), borderwidth=0, bg="#D3D3D3")
    button_next.place(x=x2, y=600, width=60, height=32)

    # Returning button objects.
    return button_previous, button_next


def select_photo(list_of_photo_button_objects, page):
    """The function responsible for selecting a graphic file from the user's computer, displaying it and assigning
    appropriate values to the PhotoButton object."""
    # Assigning the path of the file that was selected by the user. The program allows you to select JPG files.
    filename = filedialog.askopenfilename(
        title="Wybierz plik",
        filetypes=(
            ("Pliki graficzne", "*.jpg;*.jpeg;*.png;"),
            ("Pliki JPG", "*.jpg"),
            ("Pliki JPEG", "*.jpeg"),
            ("Pliki PNG", "*.png")
        )
    )

    # If the user selects a file, the program will try to open it and assign it to a variable.
    if filename:
        # Checking whether the selected file is not larger than 10MB.
        if os.path.getsize(filename) > 10 * 1024 * 1024:
            messagebox.showwarning("Zbyt duży plik.", "Plik który chcesz dodać jest zbyt duży,"
                                                      " maksymalny rozmiar pliku to 10MB.")
            return

        try:
            # Opening and converting the selected file.
            image = Image.open(filename)
            image.thumbnail((115, 75), resample=Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

        # If such a file is missing, an error will be displayed and the function will terminate.
        except FileNotFoundError:
            messagebox.showwarning("Błąd podczas otwierania pliku.",
                                   "Plik który chcesz otworzyć nie istnieje.")
            return

        # If the file is opened and assigned correctly, the program will check whether it can add a photo to the
        # PhotoButton object.
        else:
            available_image_button = False
            for button_object in list_of_photo_button_objects:
                if not button_object.photo_to_upload:
                    available_image_button = True
                    button_object.button.config(image=photo, state="normal")
                    button_object.photo_to_display = photo
                    button_object.photo_to_upload = filename
                    # Creating a button object for deleting a photo with parameters of the PhotoButton object and
                    # deleted_photos.
                    delete_button = Button(page, text="Usuń zdjęcie", font=("Arial", 8), borderwidth=0, bg="#D3D3D3",
                                           command=lambda: delete_photo(button_object))
                    delete_button.place(x=button_object.position_x+25, y=button_object.position_y+75)
                    button_object.button_delete = delete_button

                    # Loop break.
                    break

            # If the loop did not find any free buttons, an appropriate message will be displayed.
            if not available_image_button:
                messagebox.showwarning("Brak możliwości dodania kolejnego zdjęcia.",
                                       "Twój limit dodanych zdjęć został osiągnięty.")


def delete_photo(button_object, deleted_photos=None):
    """Function responsible for removing a photo from the PhotoButton object and restoring the initial values
    to the PhotoButton object."""
    # If the function is called with the deleted_photos parameter, which is a list, then the program additionally
    # clears the necessary fields of the object and adds the photo to the list.
    if isinstance(deleted_photos, list):
        if button_object.photo_from_main:
            button_object.photo_from_main = False
            deleted_photos.append((button_object.photo_to_upload, True))
        elif button_object.photo_from_media:
            deleted_photos.append((button_object.photo_to_upload, False))
            button_object.photo_from_media = False

    # Clearing the remaining fields.
    button_object.button.config(image=config_data.images["camera_icon"], state="disabled")
    button_object.photo_to_display = None
    button_object.photo_to_upload = None
    # If the photo being deleted was the main photo, change additional fields.
    if button_object.main_photo:
        button_object.main_photo = False
        button_object.button.config(borderwidth=0)
    # Destruction and removal of the delete button object from the field.
    if button_object.button_delete:
        button_object.button_delete.destroy()
        button_object.button_delete = None


def set_main_photo(selected_button_object, list_of_photo_button_objects):
    """The function responsible for setting a photo as the main one. It accepts parameters of the selected button
    and lists of all buttons."""
    # It will loop through each button and check if any are set as the main photo, if so it will remove them.
    for button_object in list_of_photo_button_objects:
        if button_object.main_photo:
            button_object.main_photo = False
            button_object.button.config(borderwidth=0)

    # Assigning the photo as the main one to the selected button.
    selected_button_object.main_photo = True
    selected_button_object.button.config(borderwidth=4)


def init_label_objects_of_announcement(page, announcement_object, x1, x2, x3, y1, y2, y3, list_of_objects):
    """Function responsible for the initialization of label objects on switched announcement pages. It accepts the
    position parameters of the created objects, the announcement object, the page object and the list of objects to be
    deleted."""
    # Init photo_label and adding it to the list of objects.
    photo_label = Label(page, bg="#D3D3D3", image=announcement_object.main_photo)
    photo_label.place(x=x1, y=y1, width=115, height=67)
    list_of_objects.append(photo_label)

    # Init category_label and adding it to the list of objects.
    category_label = Label(page, text=announcement_object.name_category, anchor=W, font=("Arial", 8), bg="#D3D3D3")
    category_label.place(x=x2, y=y1, width=114, height=13)
    list_of_objects.append(category_label)

    # Init location_label and adding it to the list of objects.
    location_label = Label(page, text=announcement_object.location, anchor=W, font=("Arial", 8), bg="#D3D3D3")
    location_label.place(x=x2, y=y2, width=114, height=13)
    list_of_objects.append(location_label)

    # Init price_label and adding it to the list of objects.
    price_label = Label(page, text=f"{announcement_object.price} ZŁ", anchor=E, font=("Arial", 10), bg="#D3D3D3")
    price_label.place(x=x3, y=y1, width=114, height=13)
    list_of_objects.append(price_label)

    # Init state_label and adding it to the list of objects.
    state_label = Label(page, text=announcement_object.state, anchor=E, font=("Arial", 8), bg="#D3D3D3")
    state_label.place(x=x3, y=y2, width=114, height=13)
    list_of_objects.append(state_label)

    # Init date_label and adding it to the list of objects.
    date_label = Label(page, text=f"Dodano: {announcement_object.creation_date}", anchor=W, font=("Arial", 8),
                       bg="#D3D3D3")
    date_label.place(x=x2, y=y3, width=231, height=13)
    list_of_objects.append(date_label)
