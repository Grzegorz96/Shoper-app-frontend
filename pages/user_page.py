import config_data
import functions
from tkinter import *
from tkinter import ttk
from datetime import datetime
from pages.edit_announcement_page import init_edit_user_announcement_page_frame
from pages.announcement_page import init_announcement_page_frame
from logic.announcements.get_user_announcements import download_user_announcements
from helpers import delete_text


def init_user_page_frame():
    """User page initialization function. Using it, the user can make changes to his account. It can also modify,
    activate, terminate and delete announcements."""
    # Destroying the current page.
    config_data.current_page.destroy()
    # Init account_page for root.
    account_page = Frame(config_data.root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                         highlightthickness=2)
    account_page.pack()

    # Init account_page vertical separates.
    ttk.Separator(account_page).place(x=427, y=15, height=600)
    ttk.Separator(account_page).place(x=854, y=15, height=600)

    # Init account_page horizontal separates.
    ttk.Separator(account_page).place(x=40, y=85, width=350)
    ttk.Separator(account_page).place(x=465, y=85, width=350)
    ttk.Separator(account_page).place(x=890, y=85, width=350)
    ttk.Separator(account_page).place(x=40, y=140, width=350)

    # Init labels for information.
    Label(account_page, text="Dane użytkownika", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=70, y=30)
    Label(account_page, text="Aktywne ogłoszenia", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=485, y=30)
    Label(account_page, text="Zakończone ogłoszenia", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=875,
                                                                                                             y=30)

    # Calculation of the time that has passed since the registration of the user account and displaying it in the number
    # of days.
    time_delta = datetime.now().replace(microsecond=0) - config_data.logged_in_user_info.creation_account_date
    Label(account_page, text=f"Jesteś z nami od {time_delta.days} dni.", font=("Arial", 20), borderwidth=0,
          bg="#A9A9A9").place(x=0, y=100, width=427)

    # Creating list of tuples of data for displaying in for loop.
    list_of_texts_and_user_info = [("Imie:", config_data.logged_in_user_info.first_name),
                                   ("Nazwisko:", config_data.logged_in_user_info.last_name),
                                   ("Email:", config_data.logged_in_user_info.email),
                                   ("Login:", config_data.logged_in_user_info.login),
                                   ("Hasło:", config_data.logged_in_user_info.password),
                                   ("Data urodzenia:", config_data.logged_in_user_info.date_of_birth),
                                   ("Ulica:", config_data.logged_in_user_info.street),
                                   ("Kod pocztowy:", config_data.logged_in_user_info.zip_code),
                                   ("Miasto:", config_data.logged_in_user_info.city)]

    # Assigning the y and i variables to 0 and specifying the hidden_password variable to True.
    y = 0
    i = 0
    hidden_password = True
    # Displaying data from the list in 2d form
    for text, user_info in list_of_texts_and_user_info:
        label = Label(account_page, text=f"{text} {user_info}", anchor=W, font=("Arial", 10), bg="#D3D3D3")
        label.place(x=10, y=(y * 52) + 160, width=200, height=30)
        entry = Entry(account_page, font=("Arial", 9))
        entry.place(x=220, y=(y * 52) + 160, width=200, height=30)
        # User can't change Login and data of birth.
        if i == 3 or i == 5:
            entry.insert("0", "Nie możesz zmienić tych danych")
            entry["state"] = "disabled"

        else:
            # Displaying password by hidden mode. Creating button for showing and hiding password.
            if i == 4:
                password_label = label
                password_label.config(text=f"{text} {'*'*len(user_info)}")
                button = Button(account_page, text="Pokaż hasło", font=("Arial", 7), borderwidth=0, bg="#D3D3D3",
                                command=lambda: show_password())
                button.place(x=155, y=350, width=55)
            # If "i" isn't 3 and 5, bind functions.
            entry.insert("0", "Zmień dane, enter aby zatwierdzić")
            entry.bind("<Button-1>", lambda event, e=entry: delete_text(e))
            entry.bind("<Return>", lambda event, ent=entry, lab=label: functions.change_user_data(ent, lab,
                                                                                                  hidden_password))
        i += 1
        y += 1

    def show_password():
        """The password discovery function takes the local variable hidden_password, sets its state to False,
        configures the local button so that its next press points to the hide_password function. Finally,
        it replaces the text with password_label as decoded."""
        nonlocal hidden_password
        hidden_password = False
        button.config(text="Ukryj hasło", command=lambda: hide_password())
        password_label.config(text=f"Hasło: {config_data.logged_in_user_info.password}")

    def hide_password():
        """The password-hiding function takes the local variable hidden_password, sets its state to True, configures
        the local button so that its next press points to the show_password function. Finally, it replaces text with
        password_label as encoded with "*"* len of actual password."""
        nonlocal hidden_password
        hidden_password = True
        button.config(text="Pokaż hasło", command=lambda: show_password())
        password_label.config(text=f"Hasło: {'*' * len(config_data.logged_in_user_info.password)}")

    def config_page_of_user_active_announcements(actual_page=1, list_of_objects=None):
        """The pagination function of the user's active announcements, downloads a specific number of announcements
        from the backend and then displays it on the page, and finally determines, depending on the number of
        downloaded objects and the current page, whether it can assign the function of the next call to a specific
        button or must block it."""
        # Downloading user active announcements from backend with specific arguments.
        user_active_announcements = download_user_announcements(1, actual_page)

        if not isinstance(list_of_objects, list):
            list_of_objects = []
        else:
            # Destroying list of initialized announcement objects.
            for element in list_of_objects:
                element.destroy()
            # Clearing destroyed objects from list.
            list_of_objects.clear()

        rows = 0
        # X positions for objects.
        x1, x2, x3 = 465, 583, 700
        # Init user_active_announcement_objects into account_page.
        for user_active_announcement_object in user_active_announcements:
            # Y positions for objects.
            y1, y2, y3 = (rows * 120) + 162, (rows * 120) + 177, (rows * 120) + 192

            # Init title_button and adding it to the list of objects.
            title_button = Button(account_page, text=user_active_announcement_object.title, anchor=W,
                                  font=("Arial", 10), bg="#D3D3D3", borderwidth=1,
                                  command=lambda announcement_object=user_active_announcement_object:
                                  init_announcement_page_frame(account_page, announcement_object, True,
                                                               True))
            title_button.place(x=x1, y=(rows * 120) + 138, width=350, height=22)
            list_of_objects.append(title_button)

            # Init labels for announcement and adding these to the list of objects.
            functions.init_label_objects_of_announcement(account_page, user_active_announcement_object, x1, x2, x3, y1,
                                                         y2, y3, list_of_objects)

            # Init edit_button and adding it to the list of objects.
            edit_button = Button(account_page, text="Edytuj", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                 command=lambda announcement_object=user_active_announcement_object:
                                 init_edit_user_announcement_page_frame(announcement_object, init_user_page_frame))
            edit_button.place(x=x3, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(edit_button)

            # Init complete_button and adding it to the list of objects.
            complete_button = Button(account_page, text="Zakończ", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                     command=lambda announcement_object=user_active_announcement_object:
                                     functions.move_active_announcement_to_completed_announcements(
                                         announcement_object, init_user_page_frame))
            complete_button.place(x=x2, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(complete_button)

            rows += 1
            if rows == 4:
                break

        # Updating buttons depending on the number of the current page and the number of downloaded announcements.
        functions.config_buttons(actual_page, button_previous_active, button_next_active, user_active_announcements,
                                 config_page_of_user_active_announcements, list_of_objects, 4)

    def config_page_of_user_completed_announcements(actual_page=1, list_of_objects=None):
        """The pagination function of the user's completed announcements, downloads a specific number of announcements
        from the backend and then displays it on the page, and finally determines, depending on the number of
        downloaded objects and the current page, whether it can assign the function of the next call to a specific
        button or must block it."""
        # List of downloaded user_completed_announcements from calling a function with specific arguments.
        user_completed_announcements = download_user_announcements(0, actual_page)

        if not isinstance(list_of_objects, list):
            list_of_objects = []
        else:
            # Destroying list of initialized announcement objects.
            for element in list_of_objects:
                element.destroy()
            # Clearing destroyed objects from list.
            list_of_objects.clear()

        rows = 0
        # X positions for objects.
        x1, x2, x3 = 890, 1008, 1125
        # Init user_completed_announcement_objects for account_page.
        for user_completed_announcement_object in user_completed_announcements:
            # Y positions for objects.
            y1, y2, y3 = (rows * 120) + 162, (rows * 120) + 177, (rows * 120) + 192

            # Init title_button and adding it to the list of objects.
            title_button = Button(account_page, text=user_completed_announcement_object.title, anchor=W,
                                  font=("Arial", 10), bg="#D3D3D3", borderwidth=1,
                                  command=lambda announcement_object=user_completed_announcement_object:
                                  init_announcement_page_frame(account_page, announcement_object, True, True))
            title_button.place(x=x1, y=(rows * 120) + 138, width=350, height=22)
            list_of_objects.append(title_button)

            # Init labels for announcement and adding these to the list of objects.
            functions.init_label_objects_of_announcement(account_page, user_completed_announcement_object, x1, x2, x3,
                                                         y1, y2, y3, list_of_objects)

            # Init activate_button and adding it to the list of objects.
            activate_button = Button(account_page, text="Aktywuj", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                     command=lambda announcement_object=user_completed_announcement_object:
                                     functions.move_completed_announcement_to_active_announcements(
                                         announcement_object, init_user_page_frame))
            activate_button.place(x=x3, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(activate_button)

            # Init delete_button and adding it to the list of objects.
            delete_button = Button(account_page, text="Usuń", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                   command=lambda announcement_object=user_completed_announcement_object:
                                   functions.delete_from_completed_announcements(
                                       announcement_object, init_user_page_frame))
            delete_button.place(x=x2, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(delete_button)

            rows += 1
            if rows == 4:
                break

        # Updating buttons depending on the number of the current page and the number of downloaded announcements.
        functions.config_buttons(actual_page, button_previous_completed, button_next_completed,
                                 user_completed_announcements, config_page_of_user_completed_announcements,
                                 list_of_objects, 4)

    # Calling the button creation function and assigning the returned objects to variables.
    button_previous_active, button_next_active = functions.create_buttons(account_page, 438, 785)
    button_previous_completed, button_next_completed = functions.create_buttons(account_page, 865, 1200)
    # The first call to the page setup functions.
    config_page_of_user_active_announcements()
    config_page_of_user_completed_announcements()
    # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
    config_data.current_page = account_page


# def init_edit_user_announcement_page_frame(announcement_object):
#     """The function initializing the page for editing the announcement by the user. The user can update the data for
#     the announcement, remove the photo, add a photo or Modify the main photo."""
#     # Destroying the current page.
#     config_data.current_page.destroy()
#     # Init edit_user_announcement_page for root.
#     edit_user_announcement_page = Frame(config_data.root, bg="#A9A9A9", width=1280, height=640,
#                                         highlightbackground="black", highlightthickness=2)
#     edit_user_announcement_page.pack()
#
#     # Init labels with information about announcement.
#     Label(edit_user_announcement_page, text="Edytuj swoje ogłoszenie!", font=("Arial", 27), borderwidth=0,
#           bg="#A9A9A9").place(x=70, y=30)
#     ttk.Separator(edit_user_announcement_page).place(x=40, y=85, width=465)
#
#     Label(edit_user_announcement_page, text=f"ID OGŁOSZENIA: {announcement_object.announcement_id}",
#           font=("Arial", 7), borderwidth=0, bg="#A9A9A9").place(x=40, y=10)
#
#     # Init label and title_entry for announcement.
#     Label(edit_user_announcement_page, text="Tytuł ogłoszenia", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
#         x=367, y=100)
#     title_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
#     title_entry.insert(0, announcement_object.title)
#     title_entry.place(x=40, y=130, width=465)
#
#     # Init label and location_entry for announcement.
#     Label(edit_user_announcement_page, text="Lokalizacja", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=296,
#                                                                                                                   y=170)
#     location_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
#     location_entry.insert(0, announcement_object.location)
#     location_entry.place(x=40, y=200, width=350)
#
#     # Init label and price_entry for announcement.
#     Label(edit_user_announcement_page, text="Kwota", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=451,
#                                                                                                             y=170)
#     price_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
#     price_entry.insert(0, announcement_object.price)
#     price_entry.place(x=405, y=200, width=100)
#     Label(edit_user_announcement_page, text="ZŁ", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=510, y=200)
#
#     # Init label and select_state for announcement.
#     Label(edit_user_announcement_page, text="Stan", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=689, y=15)
#     current_var_state = StringVar()
#     select_state = ttk.Combobox(edit_user_announcement_page, textvariable=current_var_state, font=("Arial", 13),
#                                 state="readonly", values=config_data.states)
#     select_state.place(x=560, y=40, width=170)
#     current_var_state.set(announcement_object.state)
#
#     # Init label and mobile_number_entry for announcement.
#     Label(edit_user_announcement_page, text="Numer telefonu", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
#         x=789, y=15)
#     mobile_number_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
#     if announcement_object.mobile_number:
#         mobile_number_entry.insert(0, announcement_object.mobile_number)
#     mobile_number_entry.place(x=750, y=40, width=170)
#
#     # Init labels and description_text for announcement.
#     Label(edit_user_announcement_page, text="Opis", borderwidth=0, font=("Arial", 20), bg="#A9A9A9").place(x=1175, y=15)
#     Label(edit_user_announcement_page, text="Wpisz minimum 80 znaków", borderwidth=0, font=("Arial", 11),
#           bg="#A9A9A9").place(x=1050, y=47)
#     description_text = Text(edit_user_announcement_page, width=61, height=24, font=("Arial", 14), borderwidth=0)
#     description_text.insert(INSERT, announcement_object.description)
#     description_text.place(x=560, y=70)
#
#     # Defining the current row, column and list_of_photo_button_objects.
#     rows = 0
#     columns = 0
#     list_of_photo_button_objects = []
#     # Initialization of objects for adding multimedia files, these objects have their graphical representation
#     # on the page, they are displayed as a loop in two dimensions. Each of the photo_button objects belongs to
#     # the field of the PhotoButton object, which is then placed in the list, thanks to which I can determine
#     # what state each object is in and what changes have been made.
#     for i in range(8):
#         photo_button = Button(edit_user_announcement_page, bg="#D3D3D3", image=config_data.images["camera_icon"],
#                               state="disabled", borderwidth=0)
#         photo_button.place(x=40 + (columns * 175), y=250 + (rows * 100), width=115, height=75)
#         photo_button_object = PhotoButton(photo_button, None, None, 40 + (columns * 175),
#                                           250 + (rows * 100), False, None, False,
#                                           False)
#
#         list_of_photo_button_objects.append(photo_button_object)
#         # Inserting the main photo selection function into the photo button.
#         photo_button.config(command=lambda selected_button_object=photo_button_object: functions.
#                             set_main_photo(selected_button_object, list_of_photo_button_objects))
#
#         rows += 1
#         if rows == 3:
#             rows = 0
#             columns += 1
#
#     # Downloading photos for the announcement and information about whether there was any error with downloading the
#     # photos.
#     photos_to_edit, error_with_getting_photos = functions.download_photos_to_announcement(
#         announcement_object.announcement_id, True, 115, 75)
#     # Declaring a list of photos to be removed from the server.
#     deleted_photos = []
#
#     # Depending on what values are in the downloaded photos_to_edit, the program modifies the objects in the
#     # list_of_photo_button_objects in an appropriate way.
#     # If there was no error with downloading photos, it assigns data from downloaded photos to PhotoButton objects.
#     if not error_with_getting_photos:
#         for index, (photo, filename, is_main_photo) in enumerate(photos_to_edit):
#             list_of_photo_button_objects[index].button.config(state="normal", image=photo)
#             list_of_photo_button_objects[index].photo_to_display = photo
#             list_of_photo_button_objects[index].photo_to_upload = filename
#             if is_main_photo:
#                 list_of_photo_button_objects[index].button.config(borderwidth=4)
#                 list_of_photo_button_objects[index].photo_from_main = True
#                 list_of_photo_button_objects[index].main_photo = True
#             else:
#                 list_of_photo_button_objects[index].photo_from_media = True
#
#             # Creating a delete photo button for the downloaded photo and assigning it to the PhotoButton object field.
#             delete_button = Button(edit_user_announcement_page, text="Usuń zdjęcie", font=("Arial", 8), borderwidth=0,
#                                    bg="#D3D3D3", command=lambda button_object=list_of_photo_button_objects[index]:
#                                    functions.delete_photo(button_object, deleted_photos))
#             delete_button.place(x=list_of_photo_button_objects[index].position_x + 25,
#                                 y=list_of_photo_button_objects[index].position_y + 75)
#
#             list_of_photo_button_objects[index].button_delete = delete_button
#
#     Label(edit_user_announcement_page, text="Naciśnij na obraz, aby wybrać zdjęcie główne."
#                                             " W razie niewybrania, pierwsze zdjęcie będzie zdjęciem głównym.",
#           bg="#D3D3D3", font=("Arial", 7), anchor=W).place(x=40, y=228, width=465)
#
#     # Init add_photo_button for edited announcement.
#     add_photo_button = Button(edit_user_announcement_page, bg="#D3D3D3", text="Dodaj zdjęcie", font=("Arial", 10),
#                               command=lambda: functions.select_photo(list_of_photo_button_objects,
#                                                                      edit_user_announcement_page))
#     add_photo_button.place(x=390, y=450, width=115, height=75)
#     # If was error_with_getting_photos, add_photo_button will be disabled.
#     if error_with_getting_photos:
#         add_photo_button.config(text="Brak możliwości\ndodania zdjęcia", state="disabled")
#
#     # Init change_announcement_button for edit_user_announcement_page.
#     Button(edit_user_announcement_page, bg="#00BFFF", text="Zmień ogłoszenie!", borderwidth=0, font=("Arial", 15),
#            command=lambda: functions.change_announcement_data(title_entry, location_entry, price_entry,
#                                                               description_text, announcement_object,
#                                                               init_user_page_frame, current_var_state,
#                                                               select_state, mobile_number_entry,
#                                                               list_of_photo_button_objects, deleted_photos)).place(
#         x=40, y=550, width=465, height=50)
#
#     # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
#     config_data.current_page = edit_user_announcement_page
