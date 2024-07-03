from utils import config_data
from utils.helpers import config_buttons, create_buttons, create_labels
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pages.announcement_page import init_announcement_page_frame
from windows.message_window import init_message_window
from logic.announcements.favorites.get_user_favorite_announcements import get_user_favorite_announcements
from logic.announcements.favorites.delete_announcement_from_favorites import delete_announcement_from_favorites


def init_favorite_page_frame():
    """Function of a page with the user's favorite announcements, from this page the user can unlike an announcement,
    send a message to seller, view the announcement. The page also has pagination for active and completed favorite
    announcements."""
    # Checking if user is logged in.
    if config_data.is_user_logged_in:
        # Destroying current_page.
        config_data.current_page.destroy()
        # Init favorite_page object for root.
        favorite_page = Frame(config_data.root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                              highlightthickness=2)
        favorite_page.pack()

        # Init vertical separator.
        ttk.Separator(favorite_page).place(x=427, y=15, height=600)
        ttk.Separator(favorite_page).place(x=854, y=15, height=600)
        # Init horizontal separator.
        ttk.Separator(favorite_page).place(x=40, y=85, width=350)
        ttk.Separator(favorite_page).place(x=890, y=85, width=350)
        # Init labels for information.
        Label(favorite_page, text="Ulubione", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=145, y=30)
        Label(favorite_page, text="Zakończone", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=970, y=30)

        def config_page_of_fav_active_announcements(actual_page=1, list_of_objects=None):
            """Pagination function for active favorite announcements."""
            # Retrieving the list of active_favorite_announcements from function called with specified arguments.
            user_fav_active_announcements = get_user_favorite_announcements(1, actual_page, 8)

            if not isinstance(list_of_objects, list):
                list_of_objects = []
            else:
                # Destroying list of initialized announcement objects.
                for element in list_of_objects:
                    element.destroy()
                # Clearing destroyed objects from list.
                list_of_objects.clear()

            columns = 0
            rows = 0
            # Init fav_active_announcement_objects from list to favorite_page.
            for user_fav_active_announcement_object in user_fav_active_announcements:
                # X and y positions for objects.
                x1, x2, x3 = 40 + (columns * 425), 158 + (columns * 425), 275 + (columns * 425)
                y1, y2, y3 = (rows * 120) + 162, (rows * 120) + 177, (rows * 120) + 192

                # Init title_button and adding it to the list of objects.
                title_button = Button(favorite_page, text=user_fav_active_announcement_object.title, anchor=W,
                                      font=("Arial", 10), bg="#D3D3D3", borderwidth=1,
                                      command=lambda announcement_object=user_fav_active_announcement_object:
                                      init_announcement_page_frame(favorite_page, announcement_object, True,
                                                                   False))
                title_button.place(x=x1, y=(rows * 120) + 138, width=350, height=22)
                list_of_objects.append(title_button)

                # Init labels for announcement and adding these to the list of objects.
                create_labels(favorite_page, user_fav_active_announcement_object, x1, x2, x3, y1, y2, y3,
                              list_of_objects)

                # Init message_button and adding it to the list of objects.
                message_button = Button(favorite_page, text="Wiadomość", font=("Arial", 8), borderwidth=1,
                                        bg="#D3D3D3",
                                        command=lambda announcement_object=user_fav_active_announcement_object:
                                        init_message_window(announcement_object))
                message_button.place(x=x3, y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(message_button)

                # Init unlike_button and adding it to the list of objects.
                unlike_button = Button(favorite_page, text="Nie lubię", font=("Arial", 8), borderwidth=1,
                                       bg="#D3D3D3",
                                       command=lambda announcement_object=user_fav_active_announcement_object:
                                       delete_announcement_from_favorites(announcement_object,
                                                                          init_favorite_page_frame))
                unlike_button.place(x=x2, y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(unlike_button)

                rows += 1
                if rows == 4:
                    rows = 0
                    columns += 1
                    if rows == 0 and columns == 2:
                        break

            # Updating buttons depending on the number of the current page and the number of downloaded announcements.
            config_buttons(actual_page, button_previous_active, button_next_active, user_fav_active_announcements,
                           config_page_of_fav_active_announcements, list_of_objects, 8)

        def config_page_of_fav_completed_announcements(actual_page=1, list_of_objects=None):
            """Pagination function for completed favorite announcements."""
            # Retrieving the list of completed_favorite_announcements from function called with specified arguments.
            user_fav_completed_announcements = get_user_favorite_announcements(0, actual_page, 4)

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
            # Init fav_completed_announcement_objects from list to favorite_page.
            for user_fav_completed_announcement_object in user_fav_completed_announcements:
                # Y positions for objects.
                y1, y2, y3 = (rows * 120) + 162, (rows * 120) + 177, (rows * 120) + 192

                # Init title_button and adding it to the list of objects.
                title_button = Button(favorite_page, text=user_fav_completed_announcement_object.title, anchor=W,
                                      font=("Arial", 10), bg="#D3D3D3", borderwidth=1,
                                      command=lambda announcement_object=user_fav_completed_announcement_object:
                                      init_announcement_page_frame(favorite_page, announcement_object, True,
                                                                   False))
                title_button.place(x=890, y=(rows * 120) + 138, width=350, height=22)
                list_of_objects.append(title_button)

                # Init labels for announcement and adding these to the list of objects.
                create_labels(favorite_page, user_fav_completed_announcement_object, x1, x2, x3, y1, y2, y3,
                              list_of_objects)

                # Init message_button and adding it to the list of objects.
                message_button = Button(favorite_page, text="Wiadomość", font=("Arial", 8), borderwidth=1,
                                        bg="#D3D3D3",
                                        command=lambda announcement_object=user_fav_completed_announcement_object:
                                        init_message_window(announcement_object))
                message_button.place(x=1125, y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(message_button)

                # Init delete_button and adding it to the list of objects.
                delete_button = Button(favorite_page, text="Usuń", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                       command=lambda announcement_object=user_fav_completed_announcement_object:
                                       delete_announcement_from_favorites(announcement_object,
                                                                          init_favorite_page_frame))
                delete_button.place(x=1008, y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(delete_button)

                rows += 1
                if rows == 4:
                    break

            # Updating buttons depending on the number of the current page and the number of downloaded announcements.
            config_buttons(actual_page, button_previous_completed, button_next_completed,
                           user_fav_completed_announcements, config_page_of_fav_completed_announcements,
                           list_of_objects, 4)

        # Calling the button creation function and assigning the returned objects to variables.
        button_previous_active, button_next_active = create_buttons(favorite_page, 15, 785)
        button_previous_completed, button_next_completed = create_buttons(favorite_page, 865, 1200)
        # The first call to the page setup functions.
        config_page_of_fav_active_announcements()
        config_page_of_fav_completed_announcements()
        # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
        config_data.current_page = favorite_page

    # Displaying warning.
    else:
        messagebox.showwarning("Nie jesteś zalogowany.",
                               "Aby zobaczyć ulubione ogłoszenia musisz sie zalogować.")
