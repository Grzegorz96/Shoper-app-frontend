import config_data
import functions
from tkinter import ttk
from tkinter import *
from pages.announcement_page import init_announcement_page_frame
from windows.message_window import init_message_window


def init_shoper_page_frame(search_engine=None, search_location=None, current_var_category=None):
    """The function initializing the main page of the application. On this page, the user can view searched
    announcements, go to specific announcements, send messages or like."""
    # At first initialization current_page is None, this prevents the error.
    if isinstance(config_data.current_page, Frame):
        config_data.current_page.destroy()

    # Init main_page for root.
    main_page = Frame(config_data.root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                      highlightthickness=2)
    main_page.pack()

    # Init vertical separators.
    ttk.Separator(main_page).place(x=427, y=15, height=600)
    ttk.Separator(main_page).place(x=854, y=15, height=600)

    def config_page_of_announcements(actual_page=1, list_of_objects=None, first_init=False):
        """Page pagination function for shoper_page_frame, default call accepts parameters actual_page=1,
        list_of_objects=None, first_init=False, this allows the program to work properly."""
        # The program verifies where the first function was called from.
        if search_engine:
            # If with search_engine then it will call functions with additional parameters and download list of
            # announcement objects to variable announcements.
            announcements = functions.download_announcements(actual_page, first_init, search_engine, search_location,
                                                             current_var_category)
        else:
            # If not with search_engine then it will call functions without additional parameters and download list of
            # announcement objects to variable announcements.
            announcements = functions.download_announcements(actual_page, first_init, search_engine)

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
        # Initialization of announcement objects from the list of announcements in the main_page object in 2d.
        for announcement_object in announcements:
            # X and y positions for objects.
            x1, x2, x3 = 40 + (columns * 425), 158 + (columns * 425), 275 + (columns * 425)
            y1, y2, y3 = (rows * 120) + 42, (rows * 120) + 57, (rows * 120) + 72

            # Init title_button and adding it to the list of objects.
            title_button = Button(main_page, text=announcement_object.title, anchor=W, font=("Arial", 10),
                                  borderwidth=1, bg="#D3D3D3",
                                  command=lambda announcement=announcement_object:
                                  init_announcement_page_frame(main_page, announcement, False,
                                                               False))
            title_button.place(x=x1, y=(rows * 120) + 18, width=350, height=22)
            list_of_objects.append(title_button)

            # Init labels for announcement and adding these to the list of objects.
            functions.init_label_objects_of_announcement(main_page, announcement_object, x1, x2, x3, y1, y2, y3,
                                                         list_of_objects)

            # Init message_button and adding it to the list of objects.
            message_button = Button(main_page, text="Wiadomość", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                    command=lambda announcement=announcement_object:
                                    init_message_window(announcement))
            message_button.place(x=x3, y=(rows * 120) + 87, width=115, height=22)
            list_of_objects.append(message_button)

            # Init like_button and adding it to the list of objects.
            like_button = Button(main_page, text="Lubię to", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                 command=lambda announcement=announcement_object:
                                 functions.add_announcement_to_favorite(announcement))
            like_button.place(x=x2, y=(rows * 120) + 87, width=115, height=22)
            list_of_objects.append(like_button)

            rows += 1
            if rows == 5:
                rows = 0
                columns += 1
                if rows == 0 and columns == 3:
                    break

        # Updating buttons depending on the number of the current page and the number of downloaded announcements.
        functions.config_buttons(actual_page, button_previous, button_next, announcements, config_page_of_announcements,
                                 list_of_objects, 15)

    # Calling the button creation function and assigning the returned objects to variables.
    button_previous, button_next = functions.create_buttons(main_page, 15, 1200)
    # The first call to the page setup function.
    config_page_of_announcements(first_init=True)
    # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
    config_data.current_page = main_page
