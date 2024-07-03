from utils import config_data, constants
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from models import PhotoButton
from logic.announcements.add_announcement import add_announcement
from logic.announcements.media.select_image import select_image
from logic.announcements.media.set_main_image import set_main_image


def init_add_announcement_page_frame():
    """The function initializing the page for adding announcements by the user. With this function, the user can enter
    all the necessary data and multimedia files and then, after their validation, they will be placed on the server and
    in the database. If the user is logged in, he has access to this function, otherwise he will receive a message."""
    # Checking if user is logged in.
    if config_data.is_user_logged_in:
        # Destroying the current page.
        config_data.current_page.destroy()

        # Init add_announcement_page for root.
        add_announcement_page = Frame(config_data.root, bg="#A9A9A9", width=1280, height=640,
                                      highlightbackground="black", highlightthickness=2)
        add_announcement_page.pack()

        Label(add_announcement_page, text="Utwórz swoje ogłoszenie!", font=("Arial", 27), borderwidth=0,
              bg="#A9A9A9").place(x=70, y=30)
        ttk.Separator(add_announcement_page).place(x=40, y=85, width=465)

        # Init title_entry for add_announcement_page.
        Label(add_announcement_page, text="Tytuł ogłoszenia*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
            x=360, y=100)
        title_entry = Entry(add_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
        title_entry.place(x=40, y=130, width=465)

        # Init location_entry for add_announcement_page.
        Label(add_announcement_page, text="Lokalizacja*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=109,
                                                                                                                 y=170)
        location_entry = Entry(add_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
        location_entry.place(x=40, y=200, width=170)

        # Init select_categories for add_announcement_page.
        Label(add_announcement_page, text="Kategoria*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=302,
                                                                                                               y=170)
        current_var_category = StringVar()
        ttk.Combobox(add_announcement_page, textvariable=current_var_category, font=("Arial", 13), state="readonly",
                     values=constants.categories).place(x=223, y=200, width=170)

        # Init price_entry for add_announcement_page.
        Label(add_announcement_page, text="Kwota*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=444, y=170)
        price_entry = Entry(add_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
        price_entry.place(x=405, y=200, width=100)
        Label(add_announcement_page, text="ZŁ", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=510, y=200)

        # Init select_state for add_announcement_page.
        Label(add_announcement_page, text="Stan*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=683, y=15)
        current_var_state = StringVar()
        ttk.Combobox(add_announcement_page, textvariable=current_var_state, font=("Arial", 13), state="readonly",
                     values=constants.states).place(x=560, y=40, width=170)

        # Init mobile_number_entry for add_announcement_page.
        Label(add_announcement_page, text="Numer telefonu", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
            x=789, y=15)
        mobile_number_entry = Entry(add_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
        mobile_number_entry.place(x=750, y=40, width=170)

        Label(add_announcement_page, text="Opis*", borderwidth=0, font=("Arial", 20), bg="#A9A9A9").place(x=1164, y=15)
        Label(add_announcement_page, text="Wpisz minimum 80 znaków", borderwidth=0, font=("Arial", 11),
              bg="#A9A9A9").place(x=1050, y=47)
        # Init description_text for add_announcement_page.
        description_text = Text(add_announcement_page, width=61, height=24, font=("Arial", 14), borderwidth=0)
        description_text.place(x=560, y=70)
        Label(add_announcement_page, text="*Pole wymagane", borderwidth=0, font=("Arial", 8), bg="#A9A9A9").place(
            x=40, y=600)

        # Defining the current row, column and list_of_photo_button_objects.
        rows = 0
        columns = 0
        list_of_photo_button_objects = []
        # Initialization of objects for adding multimedia files, these objects have their graphical representation
        # on the page, they are displayed as a loop in two dimensions. Each of the photo_button objects belongs to
        # the field of the PhotoButton object, which is then placed in the list, thanks to which I can determine
        # what state each object is in and what changes have been made.
        for i in range(8):
            photo_button = Button(add_announcement_page, bg="#D3D3D3", image=config_data.images["camera_icon"],
                                  state="disabled", borderwidth=0)
            photo_button.place(x=40+(columns*175), y=250+(rows*100), width=115, height=75)
            photo_button_object = PhotoButton(photo_button, None, None, 40+(columns*175),
                                              250+(rows*100), False, None, False,
                                              False)
            list_of_photo_button_objects.append(photo_button_object)
            # Added function to change the main photo.
            photo_button.config(command=lambda selected_button_object=photo_button_object: set_main_image(
                selected_button_object, list_of_photo_button_objects))

            rows += 1
            if rows == 3:
                rows = 0
                columns += 1

        Label(add_announcement_page, text="Naciśnij na obraz, aby wybrać zdjęcie główne."
                                          " W razie niewybrania, pierwsze zdjęcie będzie zdjęciem głównym.",
              bg="#D3D3D3", font=("Arial", 7), anchor=W).place(x=40, y=228, width=465)

        # Init add_photo_button for add_announcement_page.
        Button(add_announcement_page, bg="#D3D3D3", text="Dodaj zdjęcie", font=("Arial", 10),
               command=lambda: select_image(list_of_photo_button_objects, add_announcement_page)).place(
            x=390, y=450, width=115, height=75)

        # Init add_announcement_button for add_announcement_page.
        Button(add_announcement_page, bg="#00BFFF", text="Dodaj ogłoszenie!", borderwidth=0, font=("Arial", 15),
               command=lambda: add_announcement(title_entry, location_entry, current_var_category, price_entry,
                                                description_text, list_of_photo_button_objects, current_var_state,
                                                mobile_number_entry)).place(x=40, y=550, width=465, height=50)

        # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
        config_data.current_page = add_announcement_page

    else:
        # Display a warning.
        messagebox.showwarning("Nie jesteś zalogowany.", "Aby dodać ogłoszenie musisz sie zalogować.")
