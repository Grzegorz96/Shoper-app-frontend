from utils import config_data
from utils.helpers import delete_text, config_buttons, create_buttons, create_labels
from tkinter import Frame, Label, Entry, Button, W, ttk
from datetime import datetime
from pages.edit_announcement_page import init_edit_user_announcement_page_frame
from pages.announcement_page import init_announcement_page_frame
from logic.announcements.user_management.get_user_announcements import get_user_announcements
from logic.users.update_user import update_user
from logic.announcements.state_management.move_to_completed_announcements import move_to_completed_announcements
from logic.announcements.state_management.move_to_active_announcements import move_to_active_announcements
from logic.announcements.state_management.move_to_deleted_announcements import move_to_deleted_announcements


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
            entry.bind("<Return>", lambda event, ent=entry, lab=label: update_user(ent, lab, hidden_password))
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
        user_active_announcements = get_user_announcements(1, actual_page)

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
                                  init_announcement_page_frame(account_page, announcement_object, True, True))
            title_button.place(x=x1, y=(rows * 120) + 138, width=350, height=22)
            list_of_objects.append(title_button)

            # Init labels for announcement and adding these to the list of objects.
            create_labels(account_page, user_active_announcement_object, x1, x2, x3, y1, y2, y3, list_of_objects)

            # Init edit_button and adding it to the list of objects.
            edit_button = Button(account_page, text="Edytuj", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                 command=lambda announcement_object=user_active_announcement_object:
                                 init_edit_user_announcement_page_frame(announcement_object, init_user_page_frame))
            edit_button.place(x=x3, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(edit_button)

            # Init complete_button and adding it to the list of objects.
            complete_button = Button(account_page, text="Zakończ", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                     command=lambda announcement_object=user_active_announcement_object:
                                     move_to_completed_announcements(announcement_object, init_user_page_frame))
            complete_button.place(x=x2, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(complete_button)

            rows += 1
            if rows == 4:
                break

        # Updating buttons depending on the number of the current page and the number of downloaded announcements.
        config_buttons(actual_page, button_previous_active, button_next_active, user_active_announcements,
                       config_page_of_user_active_announcements, list_of_objects, 4)

    def config_page_of_user_completed_announcements(actual_page=1, list_of_objects=None):
        """The pagination function of the user's completed announcements, downloads a specific number of announcements
        from the backend and then displays it on the page, and finally determines, depending on the number of
        downloaded objects and the current page, whether it can assign the function of the next call to a specific
        button or must block it."""
        # List of downloaded user_completed_announcements from calling a function with specific arguments.
        user_completed_announcements = get_user_announcements(0, actual_page)

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
            create_labels(account_page, user_completed_announcement_object, x1, x2, x3, y1, y2, y3, list_of_objects)

            # Init activate_button and adding it to the list of objects.
            activate_button = Button(account_page, text="Aktywuj", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                     command=lambda announcement_object=user_completed_announcement_object:
                                     move_to_active_announcements(announcement_object, init_user_page_frame))
            activate_button.place(x=x3, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(activate_button)

            # Init delete_button and adding it to the list of objects.
            delete_button = Button(account_page, text="Usuń", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                   command=lambda announcement_object=user_completed_announcement_object:
                                   move_to_deleted_announcements(announcement_object, init_user_page_frame))
            delete_button.place(x=x2, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(delete_button)

            rows += 1
            if rows == 4:
                break

        # Updating buttons depending on the number of the current page and the number of downloaded announcements.
        config_buttons(actual_page, button_previous_completed, button_next_completed, user_completed_announcements,
                       config_page_of_user_completed_announcements, list_of_objects, 4)

    # Calling the button creation function and assigning the returned objects to variables.
    button_previous_active, button_next_active = create_buttons(account_page, 438, 785)
    button_previous_completed, button_next_completed = create_buttons(account_page, 865, 1200)
    # The first call to the page setup functions.
    config_page_of_user_active_announcements()
    config_page_of_user_completed_announcements()
    # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
    config_data.current_page = account_page
