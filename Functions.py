# Import the tkinter module.
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
# Import re module to validation.
from re import match
# Import classes
from Classes import LoggedUser, Announcement, UserFavoriteAnnouncement, Message, Conversation
# Import global variables.
import Config_data
# Import a module with the necessary functions to connect to the backend.
import Backend_requests
# Import other modules.
from requests import codes
from PIL import Image, ImageTk
from datetime import datetime
import os.path


def register_user(first_name_entry, last_name_entry, email_entry, login_entry, password_entry, combobox_day_var,
                  combobox_day_birthday, combobox_month_var, combobox_month_birthday, combobox_year_var,
                  combobox_year_birthday, street_entry, zip_code_entry, city_entry):
    """The function responsible for frontend validation of the entered data - if the data is successfully validated,
    the function from the backend_request module will be called, which will send the entered data to the backend,
    depending on what status code is returned, the function will perform the appropriate actions and display the
    appropriate message."""
    # Validations of entered data.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", first_name_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", last_name_entry.get()):
            if match(
                    "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+"
                    "|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$", email_entry.get()):
                if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login_entry.get()):
                    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password_entry.get()):
                        if combobox_year_var.get() in combobox_year_birthday["values"] \
                                and combobox_month_var.get() in combobox_month_birthday["values"] \
                                and combobox_day_var.get() in combobox_day_birthday["values"]:

                            # If validation is successful, the data will be assigned to variables, which will then be
                            # placed as arguments to the request function.
                            first_name = first_name_entry.get()
                            last_name = last_name_entry.get()
                            email = email_entry.get()
                            login = login_entry.get()
                            password = password_entry.get()
                            date_of_birth = (f"{combobox_day_var.get()}-{combobox_month_var.get()}-"
                                             f"{combobox_year_var.get()}")
                            street = street_entry.get()
                            zip_code = zip_code_entry.get()
                            city = city_entry.get()
                            # Calling the user registration request function.
                            response_for_register_user = Backend_requests.request_to_register_user(first_name,
                                                                                                   last_name, email,
                                                                                                   login, password,
                                                                                                   date_of_birth,
                                                                                                   street, zip_code,
                                                                                                   city)

                            # If the returned response status is 201, the program will delete all entered data from
                            # the entry and combobox objects and display an appropriate message.
                            if response_for_register_user.status_code == codes.created:
                                first_name_entry.delete(0, END)
                                last_name_entry.delete(0, END)
                                email_entry.delete(0, END)
                                login_entry.delete(0, END)
                                password_entry.delete(0, END)
                                combobox_day_var.set("")
                                combobox_month_var.set("")
                                combobox_year_var.set("")
                                street_entry.delete(0, END)
                                zip_code_entry.delete(0, END)
                                city_entry.delete(0, END)
                                messagebox.showinfo("Pomyślna rejestracja konta.", "Możesz sie zalogować.")

                            # If the returned response status is 400, the program will display a message that
                            # registration is not possible due to existing users with the provided data.
                            elif response_for_register_user.status_code == codes.bad_request:
                                if "login_error" in response_for_register_user.json():
                                    messagebox.showwarning("Nie udało sie utworzyć konta.",
                                                           "Użytkownik o podanym loginie jest już zarejestowany.")
                                elif "email_error" in response_for_register_user.json():
                                    messagebox.showwarning("Nie udało sie utworzyć konta.",
                                                           "Użytkownik o podanym emailu jest już zarejestowany.")
                                else:
                                    messagebox.showwarning("Nie udało sie utworzyć konta.",
                                                           "Niepoprawne dane do rejestracji konta.")

                            # If a status other than 201 or 400 is returned, an error message will be displayed.
                            else:
                                messagebox.showerror("Nie udało sie utworzyć konta.",
                                                     "Wystąpił błąd podczas rejestracji, spróbuj ponownie później.")

                        # Incorrect date of birth message.
                        else:
                            messagebox.showwarning("Wybierz date urodzenia.", "Nie wybrano daty urodzenia.")

                    # Incorrect password message.
                    else:
                        messagebox.showwarning("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")

                # Incorrect login message.
                else:
                    messagebox.showwarning("Niepoprawny login.", "Wprowadzono niepoprawne dane loginu.")

            # Incorrect email message.
            else:
                messagebox.showwarning("Niepoprawny email.", "Wprowadzono niepoprawne dane email.")

        # Incorrect last_name message.
        else:
            messagebox.showwarning("Niepoprawne nazwisko.", "Wprowadzono niepoprawne dane nazwiska.")

    # Incorrect first_name message.
    else:
        messagebox.showwarning("Niepoprawne imię.", "Wprowadzono niepoprawne dane imienia.")


def login_user(entry_login_or_email, entry_password, top_panel_frame, init_shoper_page_frame, root):
    """The function responsible for logging in the user, validating the entered data, changing the global
    is_user_logged_in flag and creating a user object."""
    # Validations of entered data.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", entry_login_or_email.get()) or match(
            "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+"
            "|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$", entry_login_or_email.get()):

        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", entry_password.get()):
            login_or_email = entry_login_or_email.get()
            password = entry_password.get()

            # If validation is successful, the program will call the function of sending a user login request with
            # the provided data.
            response_for_login_user = Backend_requests.request_to_login_user(login_or_email, password)

            # If the returned status is 200, then the program destroys all previously created login windows, changes
            # the login flag to True, creates a user object with the data retrieved from the database, creates a logout
            # button and displays the appropriate message.
            if response_for_login_user.status_code == codes.ok:

                for window in Config_data.list_of_active_windows:
                    window.destroy()

                Config_data.list_of_active_windows.clear()
                Config_data.is_user_logged_in = True
                user_info = response_for_login_user.json()["result"]
                Config_data.logged_in_user_info = LoggedUser(
                    user_info["user_id"],
                    user_info["first_name"],
                    user_info["last_name"],
                    user_info["email"],
                    user_info["login"],
                    user_info["password"],
                    user_info["date_of_birth"],
                    user_info["street"],
                    user_info["zip_code"],
                    user_info["city"],
                    datetime.strptime(user_info["creation_account_date"], '%Y-%m-%d %H:%M:%S')
                )

                user_name = Config_data.logged_in_user_info.first_name
                logout_button = Button(top_panel_frame, text="Wyloguj", font=("Arial", 8), borderwidth=0,
                                       bg="#D3D3D3", command=lambda: logout_user(logout_button, user_name,
                                                                                 init_shoper_page_frame, root))
                logout_button.place(x=1197, y=60, height=18, width=56)
                messagebox.showinfo("Pomyślnie zalogowano.", f"Użytkownik {user_name} pomyślnie zalogowany.")

            # If it returns a status of 400, a message about the lack of a user in the database will be displayed.
            elif response_for_login_user.status_code == codes.bad_request:
                messagebox.showwarning("Nie ma takiego użytkownika.",
                                       "Użytkownik o podanych danych nie istnieje.")

            # If a status other than 200 or 400 is returned, an error message will be displayed.
            else:
                messagebox.showerror("Błąd podczas logowania.",
                                     "W chwili obecnej nie możemy Cię zalogować, spróbuj ponownie później.")

        # Incorrect password message.
        else:
            messagebox.showwarning("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")

    # Incorrect login or email message.
    else:
        messagebox.showwarning("Niepoprawny login lub email.",
                               "Wprowadzono niepoprawne dane loginu lub emaila.")


def logout_user(logout_button, user_name, init_shoper_page_frame, root):
    """The function responsible for logging out the user deletes the user object, changes the login flag to False,
    destroys the created message objects, destroys the logout button, initializes the main application page and
    displays an appropriate message."""
    # Changing global flag and deleting data from user object.
    Config_data.is_user_logged_in = False
    Config_data.logged_in_user_info = None

    # Destroying windows of messages.
    for window in Config_data.list_of_active_windows:
        window.destroy()

    # Destroying button object, init main page of app and displaying message.
    Config_data.list_of_active_windows.clear()
    logout_button.destroy()
    init_shoper_page_frame(root)
    messagebox.showinfo("Pomyślnie wylogowano.", f"Użytkownik {user_name} został pomyślnie wylogowany.")


def change_announcement_data(title_entry, location_entry, price_entry, description_text, announcement_object,
                             init_user_page_frame, root, current_var_state, select_state, mobile_number_entry,
                             list_of_photo_button_objects, deleted_photos):
    """The function responsible for validating the announcement data, calling the function that sends data to the
    backend, modifying multimedia files on the server and their paths in the database."""
    # Validations entered data.
    if match("^.{10,45}$", title_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń ]{3,45}$", location_entry.get()):
            if match("^[0-9]{1,7}$", price_entry.get()):
                if current_var_state.get() in select_state["values"]:
                    if mobile_number_entry.get() == "" or match("^[+]?[0-9]{6,14}$", mobile_number_entry.get()):
                        if (len(description_text.get("1.0", "end-1c")) >= 80 and len(
                                description_text.get("1.0", "end-1c")) <= 400):

                            # If validation is successful, the data is assigned to the variables.
                            title = title_entry.get()
                            location = location_entry.get()
                            price = int(price_entry.get())
                            state = current_var_state.get()
                            description = description_text.get("1.0", "end-1c")

                            if mobile_number_entry.get() == "":
                                mobile_number = None
                            else:
                                mobile_number = mobile_number_entry.get()

                            # Calling the function to send a request to change the announcement for the given arguments.
                            response_for_updating_announcement \
                                = Backend_requests.request_to_update_the_announcement(title, description, price,
                                                                                      location, announcement_object.
                                                                                      announcement_id, state,
                                                                                      mobile_number)

                            # If the function returns a response with status 200, the attached photos will be added.
                            if response_for_updating_announcement.status_code == codes.ok:
                                # Assigning variables thanks to which the program knows when to enter certain blocks
                                # of code.
                                error_with_updating_photos = False
                                committed_operation_on_main_photo = False

                                # Deleting all selected photos from list, if the returned status is not other than
                                # 200 then the error_with_updating_photos flag will change its value to True.
                                for path, main_photo_flag in deleted_photos:
                                    response_for_deleting_photo = Backend_requests.request_to_delete_photo(
                                        path, main_photo_flag)
                                    if response_for_deleting_photo.status_code != codes.ok:
                                        error_with_updating_photos = True

                                # If no error occurred while deleting photos from the server, the program will determine
                                # what to do with the main photo.
                                if not error_with_updating_photos:
                                    for main_photo_from_server in list_of_photo_button_objects:
                                        if main_photo_from_server.photo_from_main:
                                            committed_operation_on_main_photo = True
                                            if not main_photo_from_server.main_photo:
                                                for photo_button_with_main_photo in list_of_photo_button_objects:
                                                    if photo_button_with_main_photo.main_photo:
                                                        if photo_button_with_main_photo.photo_from_media:
                                                            response_for_switching_photos \
                                                                = Backend_requests.request_to_switch_photos(
                                                                    announcement_object.announcement_id,
                                                                    main_photo_from_server.photo_to_upload,
                                                                    photo_button_with_main_photo.photo_to_upload,
                                                                    1, 1)
                                                            if response_for_switching_photos.status_code != codes.ok:
                                                                error_with_updating_photos = True
                                                            break

                                                        else:
                                                            response_for_switching_photos \
                                                                = Backend_requests.request_to_switch_photos(
                                                                    announcement_object.announcement_id,
                                                                    main_photo_from_server.photo_to_upload,
                                                                    None, 1, 0)
                                                            if response_for_switching_photos.status_code == codes.ok:
                                                                response_for_uploading_photo\
                                                                    = Backend_requests.request_to_upload_photo(
                                                                        announcement_object.announcement_id, 1,
                                                                        photo_button_with_main_photo.photo_to_upload)
                                                                if response_for_uploading_photo.status != codes.created:
                                                                    error_with_updating_photos = True
                                                            else:
                                                                error_with_updating_photos = True
                                                            break
                                            break

                                # If there is a case that the main photo still needs to be modified and no error has
                                # occurred previously, the program will want to modify the main photo and check whether
                                # the user has manually selected any photo for the main photo.
                                if not committed_operation_on_main_photo and not error_with_updating_photos:
                                    for photo_button in list_of_photo_button_objects:
                                        if photo_button.main_photo:
                                            committed_operation_on_main_photo = True
                                            if photo_button.photo_from_media:
                                                response_for_switching_photos\
                                                    = Backend_requests.request_to_switch_photos(
                                                        announcement_object.announcement_id, None,
                                                        photo_button.photo_to_upload, 0, 1)
                                                if response_for_switching_photos.status_code != codes.ok:
                                                    error_with_updating_photos = True
                                            else:
                                                response_for_uploading_photo\
                                                    = Backend_requests.request_to_upload_photo(
                                                        announcement_object.announcement_id, 1,
                                                        photo_button.photo_to_upload)
                                                if response_for_uploading_photo.status != codes.created:
                                                    error_with_updating_photos = True
                                            break

                                # If the profile photo has not been changed, the program will set the main photo to the
                                # first one on the list.
                                if not committed_operation_on_main_photo and not error_with_updating_photos:
                                    for button in list_of_photo_button_objects:
                                        if button.photo_to_upload:
                                            if button.photo_from_media:
                                                response_for_switching_photos\
                                                    = Backend_requests.request_to_switch_photos(
                                                        announcement_object.announcement_id, None,
                                                        button.photo_to_upload, 0, 1)
                                                if response_for_switching_photos.status_code != codes.ok:
                                                    error_with_updating_photos = True
                                            else:
                                                response_for_uploading_photo\
                                                    = Backend_requests.request_to_upload_photo(
                                                        announcement_object.announcement_id, 1,
                                                        button.photo_to_upload)
                                                if response_for_uploading_photo.status == codes.created:
                                                    button.main_photo = 1
                                                else:
                                                    error_with_updating_photos = True
                                            break

                                # If there was no upload error anywhere, the program will add all new photos added by
                                # the user.
                                if not error_with_updating_photos:
                                    for selected_photo in list_of_photo_button_objects:
                                        if (selected_photo.photo_to_upload
                                                and not selected_photo.photo_from_main
                                                and not selected_photo.photo_from_media
                                                and not selected_photo.main_photo):
                                            response_for_uploading_photo = Backend_requests.request_to_upload_photo(
                                                announcement_object.announcement_id, 0, selected_photo.photo_to_upload)
                                            if response_for_uploading_photo.status != codes.created:
                                                error_with_updating_photos = True

                                # If all photo-changing operations were completed successfully, a message will be
                                # displayed and the user page will be initialized.
                                if not error_with_updating_photos:
                                    messagebox.showinfo(
                                        f"Pomyślnie zaktualizowano Twoje ogłoszenie,"
                                        f" {Config_data.logged_in_user_info.first_name}.",
                                        f"Twoje ogłoszenie \"{title}\" zostało zaktualizowane!")
                                    init_user_page_frame(root)

                                # If any error occurs while modifying the photo, an appropriate message will be
                                # displayed and the user's page will be initialized.
                                else:
                                    messagebox.showwarning("Wystąpił błąd podczas edycji zdjęć.",
                                                           "Ogłoszenie zostało pomyślnie zaktualizowane lecz "
                                                           "wystąpił błąd podczas edycji zdjęć, spróbuj później.")
                                    init_user_page_frame(root)

                            # If error 400 occurs while changing the data for the advertisement, a message about
                            # incorrect data will be displayed. In this case, such a message cannot be displayed
                            # because everything is validated in the program.
                            elif response_for_updating_announcement.status_code == codes.bad_request:
                                messagebox.showwarning("Nie udało sie zaktualizować ogłoszenia.",
                                                       "Wprowadzono niepoprawne dane do aktualizacji ogłoszenia.")

                            # If a response with a status other than 200 or 400 is returned, an error will be displayed.
                            else:
                                messagebox.showerror("Błąd podczas aktualizacji ogłoszenia.",
                                                     "Nie udało sie zaktualizować ogłoszenia, spróbuj później.")

                        # Incorrect description message.
                        else:
                            messagebox.showwarning("Błędny opis ogłoszenia.",
                                                   "Opis ogłoszenia powinien zawierać od 80 do 400 znaków.")

                    # Incorrect mobile number message.
                    else:
                        messagebox.showwarning("Błędny numer kontaktowy ogłoszenia.",
                                               "Podany numer kontaktowy zawiera inne znaki niż cyfry lub"
                                               " jego długość jest nieprawidłowa.")

                # Incorrect state of announcement message.
                else:
                    messagebox.showwarning("Błędny stan ogłoszenia.",
                                           "Nie wybrano stanu ogłoszenia.")

            # Incorrect price message.
            else:
                messagebox.showwarning("Błędna cena ogłoszenia.",
                                       "Cena ogłoszenia powinna zawierać tylko cyfry, maksymalna kwota "
                                       "ogłoszenia to 9 999 999 zł.")

        # Incorrect location message.
        else:
            messagebox.showwarning("Błędna lokalizacja ogłoszenia.",
                                   "Lokalizacja ogłoszenia powinna zawierać od 3 do 45 znaków, podaj jedynie "
                                   "miasto lub miejscowość.")

    # Incorrect title message.
    else:
        messagebox.showwarning("Błędny tytuł ogłoszenia.", "Tytuł ogłoszenia powinien zawierać od 10 do 45 znaków.")


def download_user_announcements(active_flag, page):
    """The function is responsible for triggering a request to download the user's announcements, creating a list of
    objects for these announcements and returning them to the GUI.py module. In the function parameters, the program
    specifies which page it wants to display and whether announcements are active or completed."""
    # Calling the user announcement request function.
    response_for_getting_user_announcements = Backend_requests.request_to_get_user_announcements(active_flag, page)

    # If a response with status 200 is returned, then within the number of dictionaries in the list,
    # create announcement objects.
    if response_for_getting_user_announcements.status_code == codes.ok:

        list_of_objects_user_announcements = []
        for announcement in response_for_getting_user_announcements.json()["result"]:
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

            # If the announcement has a main photo, the path to this photo will be downloaded. Using the path,
            # the program downloads the photo from the server and assigns it to the main_photo field of the object.
            if user_announcement_object.main_photo:
                response_for_getting_photo = Backend_requests.request_to_get_photo(user_announcement_object.main_photo)
                if response_for_getting_photo.status == codes.ok:
                    image = Image.open(response_for_getting_photo)
                    image.thumbnail((90, 67), resample=3)
                    main_photo = ImageTk.PhotoImage(image)
                    user_announcement_object.main_photo = main_photo
                else:
                    user_announcement_object.main_photo = None

            list_of_objects_user_announcements.append(user_announcement_object)

        # Returning a list of objects.
        return list_of_objects_user_announcements

    # If you receive a response with a status other than 200, display an error message and return an empty list.
    else:
        messagebox.showerror("Błąd podczas wczytywania ogłoszeń.",
                             "Nie udalo sie wczytać Twoich ogłoszeń, spróbuj później.")
        return []


def add_announcement(title_entry, location_entry, current_var_category, price_entry, description_text,
                     select_categories, list_of_photo_button_objects, select_state, current_var_state,
                     mobile_number_entry):
    """The function responsible for adding advertisements and photos, validates the entered data, sends it to
    the server and handles the response returned from the server."""
    # Validations entered data.
    if match("^.{10,45}$", title_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń ]{3,45}$", location_entry.get()):
            if current_var_category.get() in select_categories["values"]:
                if match("^[0-9]{1,7}$", price_entry.get()):
                    if current_var_state.get() in select_state["values"]:
                        if mobile_number_entry.get() == "" or match("^[+]?[0-9]{6,14}$", mobile_number_entry.get()):
                            if 80 <= len(description_text.get("1.0", "end-1c")) <= 400:

                                # If the validation passes correctly, the data will be assigned to the variables.
                                title = title_entry.get()
                                location = location_entry.get()
                                category_id = select_categories["values"].index(current_var_category.get()) + 1
                                state = current_var_state.get()
                                price = int(price_entry.get())
                                description = description_text.get("1.0", "end-1c")

                                if mobile_number_entry.get() == "":
                                    mobile_number = None
                                else:
                                    mobile_number = mobile_number_entry.get()

                                # Calling the function to send a request to add an advertisement to the server.
                                response_for_adding_announcement = Backend_requests.request_to_add_the_announcement(
                                    title, location, category_id, state, price, mobile_number, description)

                                # If the response is 201, the photos are added to the server.
                                if response_for_adding_announcement.status_code == codes.created:

                                    # Assigning the returned id of the created announcement to a variable.
                                    announcement_id \
                                        = response_for_adding_announcement.json()["result"]["announcement_id"]

                                    # Creating a flag and an empty list.
                                    error_with_uploading = False
                                    list_of_photo_button_objects_to_upload = []
                                    # Adding objects from the list_of_photo_button_objects to an empty list,
                                    # if the user has previously added a photo there.
                                    for button_object in list_of_photo_button_objects:
                                        if button_object.photo_to_upload:
                                            list_of_photo_button_objects_to_upload.append(button_object)

                                    # If any objects have been added to the list, the program checks whether the user
                                    # has manually selected the main photo.
                                    if list_of_photo_button_objects_to_upload:
                                        selected_main_photo = False
                                        for button_object in list_of_photo_button_objects_to_upload:
                                            if button_object.main_photo == 1:
                                                selected_main_photo = True

                                        # If you have not selected it, the program will do it automatically.
                                        if not selected_main_photo:
                                            list_of_photo_button_objects_to_upload[0].main_photo = 1

                                        # Sending photos to the server.
                                        for button_object in list_of_photo_button_objects_to_upload:
                                            response_for_uploading_photo = Backend_requests.request_to_upload_photo(
                                                announcement_id, button_object.main_photo,
                                                button_object.photo_to_upload)

                                            # If the status was not 201 then change the flag.
                                            if response_for_uploading_photo.status != codes.created:
                                                error_with_uploading = True

                                        # Clearing fields for modified objects.
                                        for button_object in list_of_photo_button_objects_to_upload:
                                            button_object.button.config(image=Config_data.images["camera_icon"],
                                                                        state="disabled")
                                            button_object.photo_to_display = None
                                            button_object.photo_to_upload = None

                                            if button_object.main_photo == 1:
                                                button_object.main_photo = 0
                                                button_object.button.config(borderwidth=0)

                                            if button_object.button_delete:
                                                button_object.button_delete.destroy()
                                                button_object.button_delete = None

                                    # Cleaning data entry objects.
                                    title_entry.delete(0, END)
                                    location_entry.delete(0, END)
                                    price_entry.delete(0, END)
                                    mobile_number_entry.delete(0, END)
                                    description_text.delete("1.0", END)
                                    current_var_category.set("")
                                    current_var_state.set("")

                                    # If there was an error sending photos, display a message.
                                    if error_with_uploading:
                                        messagebox.showwarning("Błąd podczas dodawania zdjęć.",
                                                               "Podczas dodawania zdjęć wystąpił błąd, spróbuj "
                                                               "ponownie dodać zdjęcia z poziomu edycji ogłoszenia.")

                                    # Display a success message.
                                    messagebox.showinfo("Pomyślnie dodano ogłoszenie.",
                                                        f"Twoje ogłoszenie \"{title}\" zostało dodane, możesz dodać "
                                                        f"kolejne ogłoszenia.")

                                # If the status 400 occurred when adding an advertisement, display a message about
                                # incorrect data.
                                elif response_for_adding_announcement.status_code == codes.bad_request:
                                    messagebox.showwarning("Nie udało sie dodać ogłoszenia.",
                                                           "Wprowadzono niepoprawne dane do utworzenia ogłoszenia.")

                                # If a status other than 201 and 400 occurred, display an error.
                                else:
                                    messagebox.showerror("Błąd podczas dodawania ogłoszenia.",
                                                         "Nie udało sie dodać ogłoszenia, spróbuj później.")

                            # Incorrect description message.
                            else:
                                messagebox.showwarning("Błędny opis ogłoszenia.",
                                                       "Opis ogłoszenia powinien zawierać od 80 do 400 znaków.")

                        # Incorrect mobile number message.
                        else:
                            messagebox.showwarning("Błędny numer kontaktowy ogłoszenia.",
                                                   "Podany numer kontaktowy zawiera inne znaki niż cyfry lub"
                                                   " jego długość jest nieprawidłowa.")

                    # Incorrect state of announcement message.
                    else:
                        messagebox.showwarning("Błędny stan ogłoszenia.",
                                               "Nie wybrano stanu ogłoszenia.")

                # Incorrect price message.
                else:
                    messagebox.showwarning("Błędna cena ogłoszenia.",
                                           "Cena ogłoszenia powinna zawierać tylko cyfry, maksymalna "
                                           "kwota ogłoszenia to 9 999 999 zł.")

            # Incorrect category message.
            else:
                messagebox.showwarning("Błędna kategoria ogłoszenia.", "Nie wybrano kategorii ogłoszenia.")

        # Incorrect location message.
        else:
            messagebox.showwarning("Błędna lokalizacja ogłoszenia.",
                                   "Lokalizacja ogłoszenia powinna zawierać od 3 do 45 znaków, podaj jedynie "
                                   "miasto lub miejscowość.")

    # Incorrect title message.
    else:
        messagebox.showwarning("Błędny tytuł ogłoszenia.",
                               "Tytuł ogłoszenia powinien zawierać od 10 do 45 znaków.")


def verify_login(login_entry):
    """Function responsible for checking in the database whether the given login is already taken and informing the
    user about the result of the operation."""
    # Validation entered data.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login_entry.get()):

        # If validation is successful, call a function to send a login verification request.
        response_for_login_verification = Backend_requests.request_to_verify_login(login_entry.get())

        # If response status is 200 then display the availability message.
        if response_for_login_verification.status_code == codes.ok:
            messagebox.showinfo("Podany login jest dostępny.",
                                f"Nie istnieje jeszcze użytkownik o loginie \"{login_entry.get()}\".")

        # If response status is 400 then display an unavailability message.
        elif response_for_login_verification.status_code == codes.bad_request:
            messagebox.showinfo("Podany login jest już zajęty.",
                                f"Istnieje zarejestrowany użytkownik o loginie \"{login_entry.get()}\".")

        # If response status is other than 200 and 400, display error message.
        else:
            messagebox.showerror("Błąd podczas weryfikacji loginu.",
                                 "Nie udało się zweryfikować loginu, spróbuj później.")

    # Incorrect login message.
    else:
        messagebox.showwarning("Niepoprawny login",
                               "Nie możesz użyć tego loginu do rejestracji. Sprawdź wzór loginu")


def verify_password(password_entry):
    """Function responsible for verifying the password entered by the user and informing him of the result."""
    # If the password entered by the user passes validation, display an acceptance message.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password_entry.get()):
        messagebox.showinfo("Poprawne hasło.", "Możesz użyć tego hasła do rejestracji.")

    # If the password entered by the user does not pass validation, display a message about non-acceptance.
    else:
        messagebox.showinfo("Niepoprawne hasło.",
                            "Nie możesz użyć tego hasła do rejestracji. Sprawdź wzór hasła.")


def show_pattern(arg):
    """A feature that displays login and password requirements to the user during registration."""
    # If the transmitted argument is equal to the login pattern string, then display a message.
    if arg == "Wzór loginu":
        messagebox.showinfo("Wymogi dotyczące loginu:",
                            "- musi zawierać minimum 5 znaków,\n- może zawierać wielkie oraz małe litery,"
                            "\n- może zawierać cyfry,\n- nie może zawierać znaków specjalnych.")

    # If the transmitted argument is equal to the password pattern string, then display a message.
    elif arg == "Wzór hasła":
        messagebox.showinfo("Wymogi dotyczące hasła:",
                            "- musi zawierać minimum 7 znaków,\n- może zawierać wielkie oraz małe litery,"
                            "\n- może zawierać cyfry,\n- może zawierać znaki specjalne.")


def delete_text(entry_object):
    """A function that removes text from the entry object and unbinds the function from the object."""
    entry_object.delete(0, END)
    entry_object.unbind("<Button-1>")


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
        response_for_updating_user = Backend_requests.request_to_update_user_data(column, value)

        # If the status code is 200 then update the given field in the user object.
        if response_for_updating_user.status_code == codes.ok:
            if column == "first_name":
                Config_data.logged_in_user_info.change_user_firstname(value)
            elif column == "last_name":
                Config_data.logged_in_user_info.change_user_lastname(value)
            elif column == "email":
                Config_data.logged_in_user_info.change_user_email(value)
            elif column == "password":
                Config_data.logged_in_user_info.change_user_password(value)
            elif column == "street":
                Config_data.logged_in_user_info.change_user_street(value)
            elif column == "zip_code":
                Config_data.logged_in_user_info.change_user_zip_code(value)
            elif column == "city":
                Config_data.logged_in_user_info.change_user_city(value)

            # Label update on the user's website.
            if column == "password" and hidden_password:
                label.config(text=f"{attribute} {'*'*len(value)}")
            else:
                label.config(text=f"{attribute} {value}")
            # Delete the entered text in the imported object.
            entry.delete(0, END)
            # Display success message.
            messagebox.showinfo("Pomyślnie zaktualizowano profil użytkownika.",
                                f"Twoj profil został zaktualizowany, {Config_data.logged_in_user_info.first_name}.")

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


def move_active_announcement_to_completed_announcements(user_active_announcement_object, init_user_page_frame, root):
    """Function responsible for ending the announcement. The announcement flag will change from active to completed."""
    # Calling the function sending a request to end the announcement.
    response_for_end_of_announcement\
        = Backend_requests.request_to_complete_the_announcement(user_active_announcement_object.announcement_id)

    # If the returned response has a status of 200, then display a success message and refresh the page.
    if response_for_end_of_announcement.status_code == codes.ok:
        messagebox.showinfo(f"Pomyślnie zakończono ogłoszenie.",
                            f"{Config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_active_announcement_object.title}\" zostało przeniesione do zakończonych.")
        init_user_page_frame(root)

    # If the returned response has a status other than 200, then display an error message.
    else:
        messagebox.showerror("Błąd podczas zakańczania ogłoszenia.",
                             f"Nie udalo sie zakończyć Twojego ogłoszenia "
                             f"\"{user_active_announcement_object.title}\", spróbuj później.")


def move_completed_announcement_to_active_announcements(user_completed_announcement_object, init_user_page_frame, root):
    """Function responsible for restoring the announcement. The announcement flag will change from completed to
    active."""
    # Calling a function sending a request to restore a given announcement to the active state.
    response_for_restore_of_announcement\
        = Backend_requests.request_to_restore_the_announcement(user_completed_announcement_object.announcement_id)

    # If the returned response has a status of 200, then display a success message and refresh the page.
    if response_for_restore_of_announcement.status_code == codes.ok:
        messagebox.showinfo("Pomyślnie aktywowano ogłoszenie.",
                            f"{Config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_completed_announcement_object.title}\" zostało aktywowane.")
        init_user_page_frame(root)

    # If the returned response has a status other than 200, then display an error message.
    else:
        messagebox.showerror("Błąd podczas aktywowania ogłoszenia.",
                             f"Nie udalo sie aktywować Twojego ogłoszenia "
                             f"\"{user_completed_announcement_object.title}\", spróbuj później.")


def delete_from_completed_announcements(user_completed_announcement_object, init_user_page_frame, root):
    """Function responsible for deleting a completed announcement. The announcement flag will change from completed to
     deleted."""
    # Calling the function sending a request to remove a given announcement.
    response_for_delete_of_announcement\
        = Backend_requests.request_to_delete_the_announcement(user_completed_announcement_object.announcement_id)

    # If the returned response has a status of 200, then display a success message and refresh the page.
    if response_for_delete_of_announcement.status_code == codes.ok:
        messagebox.showinfo(f"Pomyślnie usunięto ogłoszenie.",
                            f"{Config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_completed_announcement_object.title}\" zostało usunięte.")
        init_user_page_frame(root)

    # If the returned response has a status other than 200, then display an error message.
    else:
        messagebox.showerror("Błąd podczas usuwania ogłoszenia.",
                             f"Nie udalo sie usunąć Twojego ogłoszenia "
                             f"\"{user_completed_announcement_object.title}\", spróbuj później.")


def download_announcements(from_search_engine, page, first_init, search_engine=None, search_location=None,
                           current_var=None, categories=None):
    """Function responsible for downloading announcements on the home page. When the user calls the function from
     search_engine, the user specifies the parameters with which he wants to download announcements."""
    # If the function was called from search_engine, the program will assign the imported values to the variables.
    if from_search_engine:
        content_to_search = search_engine.get()
        location = search_location.get()
        category_id = ""
        if current_var.get() in categories["values"]:
            category_id = categories["values"].index(current_var.get()) + 1

        # Calling a function sending a request to download a message with specific additional parameters.
        response_for_getting_announcements = Backend_requests.request_to_get_announcements(from_search_engine, page,
                                                                                           content_to_search, location,
                                                                                           category_id)

    # If the function is called not from search_engine, announcements will be downloaded without additional parameters.
    else:
        response_for_getting_announcements = Backend_requests.request_to_get_announcements(from_search_engine, page)

    # # If the returned response has a status of 200, the program will create a list of announcements objects from the
    # downloaded data.
    if response_for_getting_announcements.status_code == codes.ok:

        # If any announcements are downloaded, the program creates a list of objects.
        if response_for_getting_announcements.json()["result"]:

            list_of_objects_announcements = []
            for announcement in response_for_getting_announcements.json()["result"]:
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

                # Downloading main photos for announcements with a path to the main photo.
                if announcement_object.main_photo:
                    response_for_getting_photo = Backend_requests.request_to_get_photo(announcement_object.main_photo)
                    if response_for_getting_photo.status == codes.ok:
                        image = Image.open(response_for_getting_photo)
                        image.thumbnail((90, 67), resample=3)
                        main_photo = ImageTk.PhotoImage(image)
                        announcement_object.main_photo = main_photo
                    else:
                        announcement_object.main_photo = None

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
    response_for_getting_user_favorite_announcements = Backend_requests.request_to_get_user_favorite_announcements(
        active_flag, page, per_page)

    # If the returned response has a status of 200, the program will create a list of user's announcements objects from
    # the downloaded data.
    if response_for_getting_user_favorite_announcements.status_code == codes.ok:

        list_of_user_fav_announcement_objects = []
        for favorite_announcement in response_for_getting_user_favorite_announcements.json()["result"]:
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

            # Downloading main photos for user's announcements with a path to the main photo.
            if user_fav_announcement_object.main_photo:
                response_for_getting_photo = Backend_requests.request_to_get_photo(user_fav_announcement_object.
                                                                                   main_photo)
                if response_for_getting_photo.status == codes.ok:
                    image = Image.open(response_for_getting_photo)
                    image.thumbnail((90, 67), resample=3)
                    main_photo = ImageTk.PhotoImage(image)
                    user_fav_announcement_object.main_photo = main_photo
                else:
                    user_fav_announcement_object.main_photo = None

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
    if Config_data.is_user_logged_in:

        # Calling the function sending a request to add the announcement to the user's favorites.
        response_for_adding_to_favorite\
            = Backend_requests.request_to_add_announcement_to_favorite(announcement_object.announcement_id)

        # If the returned response has a status of 201, the program will display a success message.
        if response_for_adding_to_favorite.status_code == codes.created:
            messagebox.showinfo("Pomyślnie dodano do ulubionych.",
                                f"Ogłoszenie \"{announcement_object.title}\" zostało dodane do ulubionych.")

        # If the returned response has a status of 400, The program will display a message that the ad has already been
        # liked by the user.
        elif response_for_adding_to_favorite.status_code == codes.bad_request:
            messagebox.showwarning(
                f"{Config_data.logged_in_user_info.first_name}, wybrane ogłoszenie znajduję sie już w ulubionych.",
                f"Ogłoszenie \"{announcement_object.title}\" znajduje się na Twojej liście ulubionych.")

        # If the returned response has a status other than 201 and 400, the program will display an error message.
        else:
            messagebox.showerror("Błąd podczas dodawania do ulubionych.",
                                 "Nie udalo sie dodać do ulubionych, spróbuj później.")

    # User not logged in message.
    else:
        messagebox.showwarning("Nie jesteś zalogowany.",
                               "Aby dodać ogłoszenie do ulubionych musisz sie zalogować.")


def delete_announcement_from_favorite(user_fav_announcement_object, init_favorite_page_frame, root):
    response_for_deleting_announcement_from_favorite\
        = Backend_requests.request_to_delete_announcement_from_favorite(user_fav_announcement_object.
                                                                        favorite_announcement_id)

    if response_for_deleting_announcement_from_favorite.status_code == codes.ok:
        messagebox.showinfo("Pomyślnie usunięto z ulubionych.",
                            f"Ogłoszenie \"{user_fav_announcement_object.title}\" zostało usunięte z ulubionych.")
        init_favorite_page_frame(root)

    else:
        messagebox.showerror("Błąd podczas usuwania z ulubionych.",
                             "Nie udalo sie usunąć z ulubionych.")


def download_messages(announcement_object=None, conversation_object=None):
    """Function responsible for retrieving user's messages using conversation id or announcement id."""
    # If the user has imported a conversation object, the program sends a request with the conversation_id parameter.
    if conversation_object:
        response_for_getting_messages\
            = Backend_requests.request_to_get_messages(conversation_id=conversation_object.conversation_id)

    # If the user has not imported the conversation id, it means that he has imported the announcement id,
    # the program will send a request with the announcement_id parameter.
    else:
        response_for_getting_messages\
            = Backend_requests.request_to_get_messages(announcement_id=announcement_object.announcement_id)

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
                response_for_sending_message = Backend_requests.request_to_send_message(message_entry.get(),
                                                                                        is_user_customer,
                                                                                        conversation_id=conversation_id)

            # If the user does not yet have a message for a given announcement, a request will be sent with the given
            # announcement_id to first create conversations for a given announcement and then create a message for the
            # conversation.
            else:
                announcement_id = announcement_object.announcement_id
                response_for_sending_message = Backend_requests.request_to_send_message(message_entry.get(),
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
    response_for_getting_conversations = Backend_requests.request_to_get_conversations(customer_flag, page)

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
    """A function that downloads photo paths for a given ad and then photos from the downloaded paths."""
    # Defining an empty list and an error flag.
    list_of_photos = []
    error_with_getting_photos = False

    # Calling the function sending a request to download the path of the main photo for the announcement.
    response_for_getting_paths_to_main_photo = Backend_requests.request_to_get_media_paths(announcement_id, 1)

    # If the returned response has a status of 200, The program will download the photo from the path, open it and
    # assign it to a variable. Depending on whether the downloaded photo is to be edited or displayed, the program will
    # add appropriate values to the list.
    if response_for_getting_paths_to_main_photo.status_code == codes.ok:
        for dictionary in response_for_getting_paths_to_main_photo.json()["result"]:
            response_for_getting_main_photo = Backend_requests.request_to_get_photo(dictionary["path"])
            if response_for_getting_main_photo.status == codes.ok:
                image = Image.open(response_for_getting_main_photo)
                image.thumbnail((px, py), resample=3)
                photo = ImageTk.PhotoImage(image)
                if to_edit:
                    list_of_photos.append((photo, dictionary["path"], 1))
                else:
                    list_of_photos.append(photo)
            else:
                error_with_getting_photos = True
    else:
        error_with_getting_photos = True

    # Calling the function sending a request to download the path of the photos for the announcement.
    response_for_getting_paths_to_photos = Backend_requests.request_to_get_media_paths(announcement_id, 0)

    # If the returned response has a status of 200, The program will download the photos from the paths, open it and
    # assign it to a variable. Depending on whether the downloaded photo is to be edited or displayed, the program will
    # add appropriate values to the list.
    if response_for_getting_paths_to_photos.status_code == codes.ok:
        for dictionary in response_for_getting_paths_to_photos.json()["result"]:
            response_for_getting_photos = Backend_requests.request_to_get_photo(dictionary["path"])
            if response_for_getting_photos.status == codes.ok:
                image = Image.open(response_for_getting_photos)
                image.thumbnail((px, py), resample=3)
                photo = ImageTk.PhotoImage(image)
                if to_edit:
                    list_of_photos.append((photo, dictionary["path"], 0))
                else:
                    list_of_photos.append(photo)
            else:
                error_with_getting_photos = True
    else:
        error_with_getting_photos = True

    # If any error occurs during the download, the program will display a message.
    if error_with_getting_photos:
        messagebox.showerror("Błąd podczas wczytywania zdjęć.",
                             "Nie udalo sie wczytać zdjęć lub ich części, spróbuj później.")

    # Returning a list with error information.
    return list_of_photos, error_with_getting_photos


def loading_images():
    """The function is launched when the program starts from the Main.py module. The function is responsible for loading
    static graphic files and assigning them to the global dictionary."""
    # The program tries to load photos from your computer.
    try:
        Config_data.images["arrows"] = [ImageTk.PhotoImage(Image.open("Photos/left.png").resize((50, 50))),
                                        ImageTk.PhotoImage(Image.open("Photos/right.png").resize((50, 50)))]
        Config_data.images["camera_icon"] = ImageTk.PhotoImage(Image.open("Photos/camera_icon.png").resize((50, 50)))

    # If an error occurs while loading, the program will display an error message and assign the value None to the
    # dictionary keys.
    except FileNotFoundError:
        messagebox.showerror("Błąd podczas wczytywania statycznych plików graficznych.",
                             "Nie udało się wczytać statycznych plików graficznych.")
        Config_data.images["arrows"] = [None, None]
        Config_data.images["camera_icon"] = None


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


def select_photo(list_of_photo_button_objects, page, deleted_photos=None):
    """The function responsible for selecting a graphic file from the user's computer, displaying it and assigning
    appropriate values to the PhotoButton object."""
    # Assigning the path of the file that was selected by the user. The program allows you to select JPG files.
    filename = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("Pliki JPG", "*.jpg"),))

    # If the user selects a file, the program will try to open it and assign it to a variable.
    if filename:
        # Checking whether the selected file is not larger than 3MB.
        if os.path.getsize(filename) > 3145728:
            messagebox.showwarning("Zbyt duży plik.", "Plik który chcesz dodać jest zbyt duży,"
                                                      " maksymalny rozmiar pliku to 3MB.")
            return

        try:
            # Opening and converting the selected file.
            image = Image.open(filename)
            image.thumbnail((115, 75), resample=3)
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
                                           command=lambda: delete_photo(button_object, deleted_photos))
                    delete_button.place(x=button_object.position_x+25, y=button_object.position_y+75)
                    button_object.button_delete = delete_button

                    # Loop break.
                    break

            # If the loop did not find any free buttons, an appropriate message will be displayed.
            if not available_image_button:
                messagebox.showwarning("Brak możliwości dodania kolejnego zdjęcia.",
                                       "Twój limit dodanych zdjęć został osiągnięty.")


def delete_photo(button_object, deleted_photos):
    """Function responsible for removing a photo from the PhotoButton object and restoring the initial values
    to the PhotoButton object."""
    # If the function is called with the deleted_photos parameter, which is a list, then the program additionally
    # clears the necessary fields of the object and adds the photo to the list.
    if isinstance(deleted_photos, list):
        if button_object.photo_from_main:
            button_object.photo_from_main = False
            deleted_photos.append((button_object.photo_to_upload, 1))
        elif button_object.photo_from_media:
            deleted_photos.append((button_object.photo_to_upload, 0))
            button_object.photo_from_media = False

    # Clearing the remaining fields.
    button_object.button.config(image=Config_data.images["camera_icon"], state="disabled")
    button_object.photo_to_display = None
    button_object.photo_to_upload = None
    # If the photo being deleted was the main photo, change additional fields.
    if button_object.main_photo == 1:
        button_object.main_photo = 0
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
        if button_object.main_photo == 1:
            button_object.main_photo = 0
            button_object.button.config(borderwidth=0)

    # Assigning the photo as the main one to the selected button.
    selected_button_object.main_photo = 1
    selected_button_object.button.config(borderwidth=4)


def set_right(event):
    """A function that configures the text in the Text object so that it can be displayed on the right."""
    event.widget.configure(tabs=(event.width - 6, "right"))


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
