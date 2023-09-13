# Modules import.
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
# Import modules with functions.
import Functions
# Import modules with global variables.
import Config_data
# Import PhotoButton class from Classes module.
from Classes import PhotoButton
# Import datetime
from datetime import datetime


def init_main_window():
    """The function that initializes the main application window, this is a function that is called from the Main.py
    module once and then returns the created root object to the Main.py module."""
    # Creating root
    root = Tk()
    # Creating geometry, title and setting resizable.
    window_width = 1280
    window_height = 720
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.title("SHOPER.PL")
    root.resizable(width=True, height=True)
    # Creating background color and icon of app.
    root.config(bg="#B0C4DE")
    root.call("wm", "iconphoto", root._w, PhotoImage(file="Photos/home_icon.png"))

    # Returning root into Main.py
    return root


def init_top_panel(root):
    """The function initializing the top panel of the application is called once from Main.py and attaches the top
    panel objects to the main application window, which are later used by the user to initialize subsequent pages."""
    # Init top_panel_frame for root.
    top_panel_frame = Frame(root, width=1280, height=80)
    top_panel_frame.pack()

    # Init SHOPPER_button for top_panel_frame.
    Button(top_panel_frame, text="SHOPER", width=30, height=2, borderwidth=0, bg="#D3D3D3",
           command=lambda: init_shopper_page_frame(root)).place(x=20, y=20)

    # Init search_engine for top_panel_frame.
    search_engine = Entry(top_panel_frame, font=("Arial", 11), width=36, borderwidth=0, bg="#D3D3D3")
    search_engine.place(x=280, y=10)
    search_engine.insert(0, "Czego szukasz ?")
    search_engine.bind("<Button-1>", lambda event: Functions.delete_text(search_engine))

    # Init search_location for top_panel_frame.
    Label(top_panel_frame, text="Wpisz lokalizacje").place(x=580, y=30)
    search_location = Entry(top_panel_frame, font=("Arial", 11), width=36, borderwidth=0, bg="#D3D3D3")
    search_location.place(x=280, y=30)

    # Init categories for top_panel_frame.
    Label(top_panel_frame, text="Wybierz kategorie").place(x=580, y=50)
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="#D3D3D3", background="white")
    current_var = StringVar()
    categories = ttk.Combobox(top_panel_frame, textvariable=current_var, width=45, values=Config_data.categories)
    categories.place(x=280, y=50)

    # Init search_button for top_panel_frame.
    Button(top_panel_frame, text="Wyszukaj produkt", borderwidth=0, bg="#D3D3D3",
           command=lambda: init_shopper_page_frame(root, search_engine, search_location, current_var, categories,
                                                   True)).place(x=580, y=6)

    # Init favorite_button for top_panel_frame.
    Button(top_panel_frame, text="Ulubione", width=16, height=2, borderwidth=0, bg="#D3D3D3",
           command=lambda: init_favorite_page_frame(root)).place(x=730, y=20)

    # Init messages_button for top_panel_frame.
    Button(top_panel_frame, text="Wiadomości", width=16, height=2, borderwidth=0, bg="#D3D3D3",
           command=lambda: init_messages_page_frame(root)).place(x=865, y=20)

    # Init add_announcement button for top_panel_frame.
    Button(top_panel_frame, text="Dodaj ogłoszenie", width=16, height=2, borderwidth=0,
           bg="#D3D3D3", command=lambda: init_add_announcement_page_frame(root)).place(x=1000, y=20)

    # Init account_button for top_panel_frame.
    Button(top_panel_frame, text="Twoje konto", width=16, height=2, borderwidth=0, bg="#D3D3D3",
           command=lambda: is_user_logged_to_user_page(top_panel_frame, root)).place(x=1135, y=20)


def is_user_logged_to_user_page(top_panel_frame, root):
    """The function to check if the user is logged in, if logged in, I call the init_user_page_frame function,
    if not already logged in, it calls the init_login_window function so that the user can log in."""
    if Config_data.is_user_logged_in:
        init_user_page_frame(root)
    else:
        init_login_window(top_panel_frame, root)


def init_login_window(top_panel_frame, root):
    """A function that initializes an additional window with a login and registration form. Using it,
    the user can log in or register a new account."""
    # Init login_window from Top_Level() Class.
    login_window = Toplevel()
    # Adding the created window object to the global list to be able to destroy the created objects at the right moment.
    Config_data.list_of_active_windows.append(login_window)
    # Define window dimensions.
    login_window_width = 400
    login_window_height = 719
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    # Define x and y on the desktop where the window should appear.
    center_x = int(screen_width / 2 - login_window_width / 2)
    center_y = int(screen_height / 2 - login_window_height / 2)
    # Calling the geometry method, which specifies the dimensions of the window and the coordinates of the anchor.
    login_window.geometry(f"{login_window_width}x{login_window_height}+{center_x}+{center_y}")
    login_window.title("Logowanie")
    login_window.resizable(width=True, height=True)
    login_window.config(bg="#B0C4DE")
    login_window.wm_iconphoto(False, PhotoImage(file="Photos/login_icon.png"))

    # Init login_window_label for login_window.
    login_window_label = Label(login_window)
    login_window_label.grid(row=0, column=0, columnspan=2, rowspan=13, ipady=2, ipadx=2)

    Label(login_window_label, text="Zaloguj się", font="Arial").grid(row=0, column=0, pady=(10, 0))

    # Init entry_login_or_email for login_window_label.
    Label(login_window_label, text="Login lub email", font="Arial").grid(row=1, column=1, pady=10)
    entry_login_or_email = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    entry_login_or_email.grid(row=1, column=0, pady=10, ipadx=25, padx=(20, 0))

    # Init entry_password for login_window_label.
    Label(login_window_label, text="Hasło", font="Arial").grid(row=2, column=1, pady=10)
    entry_password = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    entry_password.grid(row=2, column=0, pady=10, ipadx=25, padx=(20, 0))

    # Init login_button for login_window_label.
    Button(login_window_label, text="Zaloguj się", font=("Arial", 10), borderwidth=0, bg="#D3D3D3",
           command=lambda: Functions.login_user(entry_login_or_email, entry_password, top_panel_frame,
                                                init_shopper_page_frame, root)).grid(row=3, column=1, ipadx=10, ipady=8,
                                                                                     pady=(10, 0))

    ttk.Separator(login_window_label, orient="horizontal").grid(row=4, columnspan=2, ipadx=185, pady=15, padx=10)
    Label(login_window_label, text="Zarejestruj się", font="Arial").grid(row=5, column=0, pady=(0, 10))

    # Init first_name_entry for login_window_label.
    Label(login_window_label, text="Imie*", font="Arial").grid(row=6, column=1)
    first_name_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    first_name_entry.grid(row=6, column=0, pady=10, ipadx=25, padx=(20, 0))

    # Init last_name_entry for login_window_label.
    Label(login_window_label, text="Nazwisko*", font="Arial").grid(row=7, column=1)
    last_name_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    last_name_entry.grid(row=7, column=0, pady=10, ipadx=25, padx=(20, 0))

    # Init email for login_window_label.
    Label(login_window_label, text="E-mail*", font="Arial").grid(row=8, column=1)
    email_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    email_entry.grid(row=8, column=0, pady=10, ipadx=25, padx=(20, 0))

    # Init login_entry for login_window_label.
    Label(login_window_label, text="Login*", font="Arial").grid(row=9, column=1)
    login_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    login_entry.grid(row=9, column=0, pady=(10, 4), ipadx=25, padx=(20, 0))

    # Init verify_login_button for login_window_label.
    Button(login_window_label, text="Zweryfikuj login", borderwidth=0, bg="#D3D3D3",
           command=lambda: Functions.verify_login(login_entry)).grid(row=10, column=0, sticky=E, pady=(0, 10),
                                                                     padx=(0, 8))

    # Init login_pattern_button for login_window_label.
    login_pattern = Button(login_window_label, text="Wzór loginu", borderwidth=0, bg="#D3D3D3",
                           command=lambda: Functions.show_pattern(login_pattern["text"]))
    login_pattern.grid(row=10, column=0, sticky=W, pady=(0, 10), padx=(26, 0))

    # Init password_entry for login_window_label.
    Label(login_window_label, text="Hasło*", font="Arial").grid(row=11, column=1)
    password_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    password_entry.grid(row=11, column=0, pady=(10, 4), ipadx=25, padx=(20, 0))

    # Init verify_password_button for login_window_label.
    Button(login_window_label, text="Zweryfikuj hasło", borderwidth=0, bg="#D3D3D3",
           command=lambda: Functions.verify_password(password_entry)).grid(row=12, column=0, sticky=E, pady=(0, 10),
                                                                           padx=(0, 8))

    # Init password_pattern_button for login_window_label.
    password_pattern = Button(login_window_label, text="Wzór hasła", borderwidth=0, bg="#D3D3D3",
                              command=lambda: Functions.show_pattern(password_pattern["text"]))
    password_pattern.grid(row=12, column=0, sticky=W, pady=(0, 10), padx=(26, 0))

    # Init combobox_day_birthday for login_window_label.
    Label(login_window_label, text="Data urodzenia*", font="Arial").grid(row=13, column=1)
    combobox_day_var = StringVar()
    combobox_day_birthday = ttk.Combobox(login_window_label, textvariable=combobox_day_var, width=6, state="readonly")
    combobox_day_birthday["values"] = [i for i in range(1, 32)]
    combobox_day_birthday.grid(row=13, column=0, sticky=W, pady=10, padx=(26, 0))

    # Init combobox_month_birthday for login_window_label.
    combobox_month_var = StringVar()
    combobox_month_birthday = ttk.Combobox(login_window_label, textvariable=combobox_month_var, width=10,
                                           state="readonly")
    combobox_month_birthday["values"] = ("Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec",
                                         "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień")
    combobox_month_birthday.grid(row=13, column=0, padx=(20, 0))

    # Init combobox_year_birthday for login_window_label.
    combobox_year_var = StringVar()
    combobox_year_birthday = ttk.Combobox(login_window_label, textvariable=combobox_year_var, width=6, state="readonly")
    combobox_year_birthday["values"] = [i for i in range(1900, 2024)]
    combobox_year_birthday.grid(row=13, column=0, sticky=E, padx=(0, 7))

    # Init street_entry for login_window_label.
    Label(login_window_label, text="Ulica", font="Arial").grid(row=14, column=1)
    street_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    street_entry.grid(row=14, column=0, pady=10, ipadx=25, padx=(20, 0))

    # Init zip_code_entry for login_window_label.
    Label(login_window_label, text="Kod pocztowy", font="Arial").grid(row=15, column=1)
    zip_code_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    zip_code_entry.grid(row=15, column=0, pady=10, ipadx=25, padx=(20, 0))

    # Init city_entry for login_window_label.
    Label(login_window_label, text="Miasto", font="Arial").grid(row=16, column=1)
    city_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    city_entry.grid(row=16, column=0, pady=10, ipadx=25, padx=(20, 0))

    # Init create_account_button for login_window_label.
    Button(login_window_label, text="Załóż konto", font=("Arial", 10), borderwidth=0, bg="#D3D3D3",
           command=lambda: Functions.register_user(first_name_entry, last_name_entry, email_entry, login_entry,
                                                   password_entry, combobox_day_var, combobox_day_birthday,
                                                   combobox_month_var, combobox_month_birthday, combobox_year_var,
                                                   combobox_year_birthday, street_entry, zip_code_entry,
                                                   city_entry)).grid(row=17, column=1, ipadx=10, ipady=8, pady=10)

    Label(login_window_label, text="*Pole wymagane").grid(row=17, column=0, pady=(0, 10), sticky=SW)


def init_add_announcement_page_frame(root):
    """The function initializing the page for adding announcements by the user. With this function, the user can enter
    all the necessary data and multimedia files and then, after their validation, they will be placed on the server and
    in the database. If the user is logged in, he has access to this function, otherwise he will receive a message."""
    # Checking if user is logged in.
    if Config_data.is_user_logged_in:
        # Destroying the current page.
        Config_data.current_page.destroy()

        # Init add_announcement_page for root.
        add_announcement_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                                      highlightthickness=2)
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
        select_categories = ttk.Combobox(add_announcement_page, textvariable=current_var_category, font=("Arial", 13),
                                         state="readonly", values=Config_data.categories)
        select_categories.place(x=223, y=200, width=170)

        # Init price_entry for add_announcement_page.
        Label(add_announcement_page, text="Kwota*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=444, y=170)
        price_entry = Entry(add_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
        price_entry.place(x=405, y=200, width=100)
        Label(add_announcement_page, text="ZŁ", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=510, y=200)

        # Init select_state for add_announcement_page.
        Label(add_announcement_page, text="Stan*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=683, y=15)
        current_var_state = StringVar()
        select_state = ttk.Combobox(add_announcement_page, textvariable=current_var_state, font=("Arial", 13),
                                    state="readonly", values=Config_data.states)
        select_state.place(x=560, y=40, width=170)

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
            photo_button = Button(add_announcement_page, bg="#D3D3D3", image=Config_data.images["camera_icon"],
                                  state="disabled", borderwidth=0)
            photo_button.place(x=40+(columns*175), y=250+(rows*100), width=115, height=75)
            photo_button_object = PhotoButton(photo_button, None, None, 40+(columns*175),
                                              250+(rows*100), 0, None, False,
                                              False)
            list_of_photo_button_objects.append(photo_button_object)
            # Added function to change the main photo.
            photo_button.config(command=lambda selected_button_object=photo_button_object: Functions.
                                set_main_photo(selected_button_object, list_of_photo_button_objects))

            rows += 1
            if rows == 3:
                rows = 0
                columns += 1

        Label(add_announcement_page, text="Naciśnij na obraz, aby wybrać zdjęcie główne."
                                          " W razie niewybrania, pierwsze zdjęcie będzie zdjęciem głównym.",
              bg="#D3D3D3", font=("Arial", 7), anchor=W).place(x=40, y=228, width=465)

        # Init add_photo_button for add_announcement_page.
        Button(add_announcement_page, bg="#D3D3D3", text="Dodaj zdjęcie", font=("Arial", 10),
               command=lambda: Functions.select_photo(list_of_photo_button_objects, add_announcement_page)).place(
            x=390, y=450, width=115, height=75)

        # Init add_announcement_button for add_announcement_page.
        Button(add_announcement_page, bg="#00BFFF", text="Dodaj ogłoszenie!", borderwidth=0, font=("Arial", 15),
               command=lambda: Functions.add_announcement(title_entry, location_entry, current_var_category,
                                                          price_entry, description_text, select_categories,
                                                          list_of_photo_button_objects, select_state, current_var_state,
                                                          mobile_number_entry)).place(x=40, y=550, width=465, height=50)

        # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
        Config_data.current_page = add_announcement_page

    else:
        # Display a warning.
        messagebox.showwarning("Nie jesteś zalogowany.", "Aby dodać ogłoszenie musisz sie zalogować.")


def init_user_page_frame(root):
    """User page initialization function. Using it, the user can make changes to his account. It can also modify,
    activate, terminate and delete announcements."""
    # Destroying the current page.
    Config_data.current_page.destroy()
    # Init account_page for root.
    account_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
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
    time_delta = datetime.now().replace(microsecond=0) - Config_data.logged_in_user_info.creation_account_date
    Label(account_page, text=f"Jesteś z nami od {time_delta.days} dni.", font=("Arial", 20), borderwidth=0,
          bg="#A9A9A9").place(x=0, y=100, width=427)

    # Creating list of tuples of data for displaying in for loop.
    list_of_texts_and_user_info = [("Imie:", Config_data.logged_in_user_info.first_name),
                                   ("Nazwisko:", Config_data.logged_in_user_info.last_name),
                                   ("Email:", Config_data.logged_in_user_info.email),
                                   ("Login:", Config_data.logged_in_user_info.login),
                                   ("Hasło:", Config_data.logged_in_user_info.password),
                                   ("Data urodzenia:", Config_data.logged_in_user_info.date_of_birth),
                                   ("Ulica:", Config_data.logged_in_user_info.street),
                                   ("Kod pocztowy:", Config_data.logged_in_user_info.zip_code),
                                   ("Miasto:", Config_data.logged_in_user_info.city)]

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
            entry.bind("<Button-1>", lambda event, e=entry: Functions.delete_text(e))
            entry.bind("<Return>", lambda event, e=entry, l=label: Functions.change_user_data(e, l, hidden_password))
        i += 1
        y += 1

    def show_password():
        """The password discovery function takes the local variable hidden_password, sets its state to False,
        configures the local button so that its next press points to the hide_password function. Finally,
        it replaces the text with password_label as decoded."""
        nonlocal hidden_password
        hidden_password = False
        button.config(text="Ukryj hasło", command=lambda: hide_password())
        password_label.config(text=f"Hasło: {Config_data.logged_in_user_info.password}")

    def hide_password():
        """The password-hiding function takes the local variable hidden_password, sets its state to True, configures
        the local button so that its next press points to the show_password function. Finally, it replaces text with
        password_label as encoded with "*"* len of actual password."""
        nonlocal hidden_password
        hidden_password = True
        button.config(text="Pokaż hasło", command=lambda: show_password())
        password_label.config(text=f"Hasło: {'*' * len(Config_data.logged_in_user_info.password)}")

    def config_page_of_user_active_announcements(actual_page=1, list_of_objects=None):
        """The pagination function of the user's active announcements, downloads a specific number of announcements
        from the backend and then displays it on the page, and finally determines, depending on the number of
        downloaded objects and the current page, whether it can assign the function of the next call to a specific
        button or must block it."""
        # Downloading user active announcements from backend with specific arguments.
        user_active_announcements = Functions.download_user_announcements(1, actual_page)

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
            Functions.init_label_objects_of_announcement(account_page, user_active_announcement_object, x1, x2, x3, y1,
                                                         y2, y3, list_of_objects)

            # Init edit_button and adding it to the list of objects.
            edit_button = Button(account_page, text="Edytuj", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                 command=lambda announcement_object=user_active_announcement_object:
                                 init_edit_user_announcement_page_frame(announcement_object, root))
            edit_button.place(x=x3, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(edit_button)

            # Init complete_button and adding it to the list of objects.
            complete_button = Button(account_page, text="Zakończ", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                     command=lambda announcement_object=user_active_announcement_object:
                                     Functions.move_active_announcement_to_completed_announcements(
                                         announcement_object, init_user_page_frame, root))
            complete_button.place(x=x2, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(complete_button)

            rows += 1
            if rows == 4:
                break

        # Updating buttons depending on the number of the current page and the number of downloaded announcements.
        Functions.config_buttons(actual_page, button_previous_active, button_next_active, user_active_announcements,
                                 config_page_of_user_active_announcements, list_of_objects, 4)

    def config_page_of_user_completed_announcements(actual_page=1, list_of_objects=None):
        """The pagination function of the user's completed announcements, downloads a specific number of announcements
        from the backend and then displays it on the page, and finally determines, depending on the number of
        downloaded objects and the current page, whether it can assign the function of the next call to a specific
        button or must block it."""
        # List of downloaded user_completed_announcements from calling a function with specific arguments.
        user_completed_announcements = Functions.download_user_announcements(0, actual_page)

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
            Functions.init_label_objects_of_announcement(account_page, user_completed_announcement_object, x1, x2, x3,
                                                         y1, y2, y3, list_of_objects)

            # Init activate_button and adding it to the list of objects.
            activate_button = Button(account_page, text="Aktywuj", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                     command=lambda announcement_object=user_completed_announcement_object:
                                     Functions.move_completed_announcement_to_active_announcements(
                                         announcement_object, init_user_page_frame, root))
            activate_button.place(x=x3, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(activate_button)

            # Init delete_button and adding it to the list of objects.
            delete_button = Button(account_page, text="Usuń", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                   command=lambda announcement_object=user_completed_announcement_object:
                                   Functions.delete_from_completed_announcements(
                                       announcement_object, init_user_page_frame, root))
            delete_button.place(x=x2, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(delete_button)

            rows += 1
            if rows == 4:
                break

        # Updating buttons depending on the number of the current page and the number of downloaded announcements.
        Functions.config_buttons(actual_page, button_previous_completed, button_next_completed,
                                 user_completed_announcements, config_page_of_user_completed_announcements,
                                 list_of_objects, 4)

    # Calling the button creation function and assigning the returned objects to variables.
    button_previous_active, button_next_active = Functions.create_buttons(account_page, 438, 785)
    button_previous_completed, button_next_completed = Functions.create_buttons(account_page, 865, 1200)
    # The first call to the page setup functions.
    config_page_of_user_active_announcements()
    config_page_of_user_completed_announcements()
    # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
    Config_data.current_page = account_page


def init_edit_user_announcement_page_frame(announcement_object, root):
    """The function initializing the page for editing the announcement by the user. The user can update the data for
    the announcement, remove the photo, add a photo or Modify the main photo."""
    # Destroying the current page.
    Config_data.current_page.destroy()
    # Init edit_user_announcement_page for root.
    edit_user_announcement_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                                        highlightthickness=2)
    edit_user_announcement_page.pack()

    # Init labels with information about announcement.
    Label(edit_user_announcement_page, text="Edytuj swoje ogłoszenie!", font=("Arial", 27), borderwidth=0,
          bg="#A9A9A9").place(x=70, y=30)
    ttk.Separator(edit_user_announcement_page).place(x=40, y=85, width=465)

    Label(edit_user_announcement_page, text=f"ID OGŁOSZENIA: {announcement_object.announcement_id}",
          font=("Arial", 7), borderwidth=0, bg="#A9A9A9").place(x=40, y=10)

    # Init label and title_entry for announcement.
    Label(edit_user_announcement_page, text="Tytuł ogłoszenia", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
        x=367, y=100)
    title_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
    title_entry.insert(0, announcement_object.title)
    title_entry.place(x=40, y=130, width=465)

    # Init label and location_entry for announcement.
    Label(edit_user_announcement_page, text="Lokalizacja", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=296,
                                                                                                                  y=170)
    location_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
    location_entry.insert(0, announcement_object.location)
    location_entry.place(x=40, y=200, width=350)

    # Init label and price_entry for announcement.
    Label(edit_user_announcement_page, text="Kwota", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=451,
                                                                                                            y=170)
    price_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
    price_entry.insert(0, announcement_object.price)
    price_entry.place(x=405, y=200, width=100)
    Label(edit_user_announcement_page, text="ZŁ", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=510, y=200)

    # Init label and select_state for announcement.
    Label(edit_user_announcement_page, text="Stan", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=689, y=15)
    current_var_state = StringVar()
    select_state = ttk.Combobox(edit_user_announcement_page, textvariable=current_var_state, font=("Arial", 13),
                                state="readonly", values=Config_data.states)
    select_state.place(x=560, y=40, width=170)
    current_var_state.set(announcement_object.state)

    # Init label and mobile_number_entry for announcement.
    Label(edit_user_announcement_page, text="Numer telefonu", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
        x=789, y=15)
    mobile_number_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
    if announcement_object.mobile_number:
        mobile_number_entry.insert(0, announcement_object.mobile_number)
    mobile_number_entry.place(x=750, y=40, width=170)

    # Init labels and description_text for announcement.
    Label(edit_user_announcement_page, text="Opis", borderwidth=0, font=("Arial", 20), bg="#A9A9A9").place(x=1175, y=15)
    Label(edit_user_announcement_page, text="Wpisz minimum 80 znaków", borderwidth=0, font=("Arial", 11),
          bg="#A9A9A9").place(x=1050, y=47)
    description_text = Text(edit_user_announcement_page, width=61, height=24, font=("Arial", 14), borderwidth=0)
    description_text.insert(INSERT, announcement_object.description)
    description_text.place(x=560, y=70)

    # Defining the current row, column and list_of_photo_button_objects.
    rows = 0
    columns = 0
    list_of_photo_button_objects = []
    # Initialization of objects for adding multimedia files, these objects have their graphical representation
    # on the page, they are displayed as a loop in two dimensions. Each of the photo_button objects belongs to
    # the field of the PhotoButton object, which is then placed in the list, thanks to which I can determine
    # what state each object is in and what changes have been made.
    for i in range(8):
        photo_button = Button(edit_user_announcement_page, bg="#D3D3D3", image=Config_data.images["camera_icon"],
                              state="disabled", borderwidth=0)
        photo_button.place(x=40 + (columns * 175), y=250 + (rows * 100), width=115, height=75)
        photo_button_object = PhotoButton(photo_button, None, None, 40 + (columns * 175),
                                          250 + (rows * 100), 0, None, False,
                                          False)

        list_of_photo_button_objects.append(photo_button_object)
        # Inserting the main photo selection function into the photo button.
        photo_button.config(command=lambda selected_button_object=photo_button_object: Functions.
                            set_main_photo(selected_button_object, list_of_photo_button_objects))

        rows += 1
        if rows == 3:
            rows = 0
            columns += 1

    # Downloading photos for the announcement and information about whether there was any error with downloading the
    # photos.
    photos_to_edit, error_with_getting_photos = Functions.download_photos_to_announcement(
        announcement_object.announcement_id, True, 115, 75)
    # Declaring a list of photos to be removed from the server.
    deleted_photos = []

    # Depending on what values are in the downloaded photos_to_edit, the program modifies the objects in the
    # list_of_photo_button_objects in an appropriate way.
    # If there was no error with downloading photos, it assigns data from downloaded photos to PhotoButton objects.
    if not error_with_getting_photos:
        for i in range(len(photos_to_edit)):
            list_of_photo_button_objects[i].button.config(state="normal", image=photos_to_edit[i][0])
            list_of_photo_button_objects[i].photo_to_display = photos_to_edit[i][0]
            list_of_photo_button_objects[i].photo_to_upload = photos_to_edit[i][1]
            list_of_photo_button_objects[i].main_photo = photos_to_edit[i][2]
            if photos_to_edit[i][2] == 1:
                list_of_photo_button_objects[i].button.config(borderwidth=4)
                list_of_photo_button_objects[i].photo_from_main = True
            else:
                list_of_photo_button_objects[i].photo_from_media = True

            # Creating a delete photo button for the downloaded photo and assigning it to the PhotoButton object field.
            delete_button = Button(edit_user_announcement_page, text="Usuń zdjęcie", font=("Arial", 8), borderwidth=0,
                                   bg="#D3D3D3", command=lambda button_object=list_of_photo_button_objects[i]:
                                   Functions.delete_photo(button_object, deleted_photos))
            delete_button.place(x=list_of_photo_button_objects[i].position_x + 25,
                                y=list_of_photo_button_objects[i].position_y + 75)

            list_of_photo_button_objects[i].button_delete = delete_button

    Label(edit_user_announcement_page, text="Naciśnij na obraz, aby wybrać zdjęcie główne."
                                            " W razie niewybrania, pierwsze zdjęcie będzie zdjęciem głównym.",
          bg="#D3D3D3", font=("Arial", 7), anchor=W).place(x=40, y=228, width=465)

    # Init add_photo_button for edited announcement.
    add_photo_button = Button(edit_user_announcement_page, bg="#D3D3D3", text="Dodaj zdjęcie", font=("Arial", 10),
                              command=lambda: Functions.select_photo(list_of_photo_button_objects,
                                                                     edit_user_announcement_page, deleted_photos))
    add_photo_button.place(x=390, y=450, width=115, height=75)
    # If was error_with_getting_photos, add_photo_button will be disabled.
    if error_with_getting_photos:
        add_photo_button.config(text="Brak możliwości\ndodania zdjęcia", state="disabled")

    # Init change_announcement_button for edit_user_announcement_page.
    Button(edit_user_announcement_page, bg="#00BFFF", text="Zmień ogłoszenie!", borderwidth=0, font=("Arial", 15),
           command=lambda: Functions.change_announcement_data(title_entry, location_entry, price_entry,
                                                              description_text, announcement_object,
                                                              init_user_page_frame, root, current_var_state,
                                                              select_state, mobile_number_entry,
                                                              list_of_photo_button_objects, deleted_photos)).place(
        x=40, y=550, width=465, height=50)

    # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
    Config_data.current_page = edit_user_announcement_page


def init_shopper_page_frame(root, search_engine=None, search_location=None, current_var=None, categories=None,
                            from_search_engine=False):
    """The function initializing the main page of the application. On this page, the user can view searched
    announcements, go to specific announcements, send messages or like."""
    # At first initialization current_page is None, this prevents the error.
    if isinstance(Config_data.current_page, Frame):
        Config_data.current_page.destroy()

    # Init main_page for root
    main_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black", highlightthickness=2)
    main_page.pack()

    # Init vertical separators.
    ttk.Separator(main_page).place(x=427, y=15, height=600)
    ttk.Separator(main_page).place(x=854, y=15, height=600)

    def config_page_of_announcements(actual_page=1, list_of_objects=None, first_init=False):
        """Page pagination function for shopper_page_frame, default call accepts parameters actual_page=1,
        list_of_objects=None, first_init=False, this allows the program to work properly."""
        # The program verifies where the first function was called from.
        if from_search_engine:
            # If with search_engine then it will call functions with additional parameters and download list of
            # announcement objects to variable announcements.
            announcements = Functions.download_announcements(from_search_engine, actual_page, first_init, search_engine,
                                                             search_location, current_var, categories)
        else:
            # If not with search_engine then it will call functions without additional parameters and download list of
            # announcement objects to variable announcements.
            announcements = Functions.download_announcements(from_search_engine, actual_page, first_init)

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
            Functions.init_label_objects_of_announcement(main_page, announcement_object, x1, x2, x3, y1, y2, y3,
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
                                 Functions.add_announcement_to_favorite(announcement))
            like_button.place(x=x2, y=(rows * 120) + 87, width=115, height=22)
            list_of_objects.append(like_button)

            rows += 1
            if rows == 5:
                rows = 0
                columns += 1
                if rows == 0 and columns == 3:
                    break

        # Updating buttons depending on the number of the current page and the number of downloaded announcements.
        Functions.config_buttons(actual_page, button_previous, button_next, announcements, config_page_of_announcements,
                                 list_of_objects, 15)

    # Calling the button creation function and assigning the returned objects to variables.
    button_previous, button_next = Functions.create_buttons(main_page, 15, 1200)
    # The first call to the page setup function.
    config_page_of_announcements(first_init=True)
    # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
    Config_data.current_page = main_page


def init_announcement_page_frame(page, announcement_object, block_fav, block_mess):
    """The function initializing the announcement page, displays all data for a given announcement. It also downloads
    photos and displays them in the gallery. From this page, the user can like the announcement, send a message
    or unlock the seller's mobile number."""
    # Initialization of the local tmp_page, this object will not be assigned to the Config_data.current_page because it
    # is created for the object of the imported page and not for the root, in case of destroying the imported page,
    # this object will automatically be destroyed.
    tmp_page = Frame(page, bg="#A9A9A9", width=1276, height=636)
    tmp_page.pack()

    # Init of labels with information about the announcement.
    Label(tmp_page, text=f"ID OGŁOSZENIA: {announcement_object.announcement_id}",
          font=("Arial", 10), borderwidth=0, bg="#A9A9A9").place(x=20, y=15)
    Label(tmp_page, text=f"Dodano: {announcement_object.creation_date}",
          font=("Arial", 10), borderwidth=0, bg="#A9A9A9").place(x=20, y=594)
    Label(tmp_page, text=announcement_object.first_name, font=("Arial", 14), borderwidth=0, anchor=E,
          width=45, bg="#A9A9A9").place(x=740, y=15)
    Label(tmp_page, text=announcement_object.title, font=("Arial", 20), borderwidth=0, anchor=W,
          width=55, bg="#A9A9A9").place(x=20, y=60)
    Label(tmp_page, text=f"{announcement_object.price} ZŁ", font=("Arial", 14), borderwidth=0, anchor=E,
          width=15, bg="#A9A9A9").place(x=1070, y=60)
    Label(tmp_page, text=announcement_object.location, font=("Arial", 14), borderwidth=0, anchor=E,
          width=45, bg="#A9A9A9").place(x=740, y=90)
    Label(tmp_page, text=announcement_object.name_category, font=("Arial", 9), borderwidth=0, anchor=E,
          width=40, bg="#A9A9A9").place(x=955, y=135)
    Label(tmp_page, text=announcement_object.state, font=("Arial", 9), borderwidth=0, anchor=E,
          width=20, bg="#A9A9A9").place(x=1095, y=155)
    ttk.Separator(tmp_page).place(x=987, y=50, width=250)
    ttk.Separator(tmp_page).place(x=987, y=125, width=250)

    # Init description_text for displaying description of announcement.
    description_text = Text(tmp_page, width=45, height=18, font=("Arial", 14), borderwidth=0)
    description_text.insert(INSERT, f"{announcement_object.description}")
    description_text.place(x=740, y=180)
    description_text["state"] = "disabled"

    # Init button_mobile_phone with function of showing mobile number, if the object does not meet the specified
    # conditions, it's state will be disabled.
    button_mobile_phone = Button(tmp_page, text="Zadzwoń", font=("Arial", 12), borderwidth=0, bg="#D3D3D3", width=15,
                                 command=lambda: button_mobile_phone.config(text=announcement_object.mobile_number,
                                                                            state="disabled"))
    button_mobile_phone["state"] = "disabled" if not announcement_object.mobile_number or block_mess else "normal"
    button_mobile_phone.place(x=740, y=594)

    # Init button_mess if the object does not meet the specified conditions, it's state will be disabled.
    button_mess = Button(tmp_page, text="Wyślij wiadomość", font=("Arial", 12), borderwidth=0, bg="#D3D3D3", width=15,
                         command=lambda: init_message_window(announcement_object))
    button_mess.place(x=888, y=594)
    button_mess["state"] = "disabled" if block_mess else "normal"

    # Init button_fav if the object does not meet the specified conditions, it's state will be disabled.
    button_fav = Button(tmp_page, text="Lubię to", font=("Arial", 12), borderwidth=0, bg="#D3D3D3", width=10,
                        command=lambda: Functions.add_announcement_to_favorite(announcement_object))
    button_fav.place(x=1037, y=594)
    button_fav["state"] = "disabled" if block_fav else "normal"

    # Init photo_label for displaying photos of announcement.
    photo_label = Label(tmp_page, text="Brak zdjęć do ogłoszenia.", font=("Arial", 12), borderwidth=3, bg="#D3D3D3")
    photo_label.place(x=20, y=112, width=700, height=466)

    # Init button_back for destroying tmp_page and returning to previous page.
    Button(tmp_page, text="Wróć", font=("Arial", 12), borderwidth=0, bg="#D3D3D3", width=10,
           command=lambda: tmp_page.destroy()).place(x=1141, y=594)

    # Downloading list of photos to announcement.
    photos, error_with_getting_photos = Functions.download_photos_to_announcement(
        announcement_object.announcement_id, False, 600, 400)

    def init_photo(actual_photo=0):
        """Photo initialization function, thanks to which the user can configure the photo displayed on the label."""
        # If actual_photo is greater or equal to 0 and lower than length of photos, the program will enter the block
        # and modify the objects accordingly.
        if 0 <= actual_photo < len(photos):
            photo_label.config(image=photos[actual_photo])
            button_previous.config(command=lambda: init_photo(actual_photo-1))
            button_next.config(command=lambda: init_photo(actual_photo+1))

    # If list of photos is not empty, the buttons will be created and the first init_photo will be called.
    if len(photos) > 0:
        button_previous = Button(tmp_page, image=Config_data.images["arrows"][0], borderwidth=0, bg="#D3D3D3")
        button_previous.place(x=20, y=325, width=50, height=50)
        button_next = Button(tmp_page, image=Config_data.images["arrows"][1], borderwidth=0, bg="#D3D3D3")
        button_next.place(x=670, y=325, width=50, height=50)
        init_photo()


def init_messages_page_frame(root):
    """A function that initializes the user's messages page. The user can select the appropriate conversation
    and reply to the buyer or seller."""
    # Checking if the user is logged in.
    if Config_data.is_user_logged_in:
        # Destroying the current page.
        Config_data.current_page.destroy()

        # Init messages_page for root.
        messages_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                              highlightthickness=2)
        messages_page.pack()

        # Init horizontal separators.
        ttk.Separator(messages_page).place(x=40, y=85, width=240)
        ttk.Separator(messages_page).place(x=360, y=85, width=240)

        # Init vertical separators.
        ttk.Separator(messages_page).place(x=320, y=15, height=600)
        ttk.Separator(messages_page).place(x=640, y=15, height=600)

        # Init labels.
        Label(messages_page, text="Kupujesz", font=("Arial", 27), bg="#A9A9A9").place(x=85, y=30)
        Label(messages_page, text="Sprzedajesz", font=("Arial", 27), bg="#A9A9A9").place(x=378, y=30)

        def config_conversations_page_as_customer(actual_page=1, list_of_objects=None):
            """Pagination function for downloaded conversations as a customer."""
            # Retrieving a list of conversation objects and assigning them to a variable.
            conversations_as_customer = Functions.download_conversations(1, actual_page)

            # for first calling of function.
            if not isinstance(list_of_objects, list):
                list_of_objects = []
            else:
                # Destroying list of initialized announcement objects.
                for element in list_of_objects:
                    element.destroy()
                # Clearing destroyed objects from list.
                list_of_objects.clear()

            rows = 0
            # init customer_conversation_objects from list to messages_page.
            for customer_conversation_object in conversations_as_customer:
                # Init title_button and adding it to the list of objects.
                title_button = Button(messages_page, text=customer_conversation_object.title, bg="#D3D3D3",
                                      font=("Arial", 10), anchor=W, borderwidth=1,
                                      command=lambda conversation_object=customer_conversation_object:
                                      update_text_of_messages(conversation_object, True))
                title_button.place(x=15, y=(rows * 75) + 100, width=300, height=22)
                list_of_objects.append(title_button)

                # Init id_label and adding it to the list of objects.
                id_label = Label(messages_page, text=f"ID: {customer_conversation_object.announcement_id}", anchor=E,
                                 bg="#D3D3D3", font=("Arial", 9))
                id_label.place(x=244, y=(rows * 75) + 123, width=70, height=15)
                list_of_objects.append(id_label)

                # Init name_label and adding it to the list of objects.
                name_label = Label(messages_page, text=f"Sprzedający: {customer_conversation_object.first_name}",
                                   anchor=W, bg="#D3D3D3", font=("Arial", 9))
                name_label.place(x=15, y=(rows * 75) + 123, width=227, height=15)
                list_of_objects.append(name_label)

                rows += 1
                if rows == 7:
                    break

            # Updating buttons depending on the number of the current page and the number of downloaded conversations.
            Functions.config_buttons(actual_page, button_previous_customer, button_next_customer,
                                     conversations_as_customer, config_conversations_page_as_customer, list_of_objects,
                                     7)

        def config_conversations_page_as_seller(actual_page=1, list_of_objects=None):
            """Pagination function for downloaded conversations as a seller."""
            # Retrieving a list of conversation objects and assigning them to a variable.
            conversations_as_seller = Functions.download_conversations(0, actual_page)

            if not isinstance(list_of_objects, list):
                list_of_objects = []
            else:
                # Destroying list of initialized announcement objects.
                for element in list_of_objects:
                    element.destroy()
                # Clearing destroyed objects from list.
                list_of_objects.clear()

            rows = 0
            # init seller_conversation_objects from list to messages_page.
            for seller_conversation_object in conversations_as_seller:
                # Init title_button and adding it to the list of objects.
                title_button = Button(messages_page, text=seller_conversation_object.title, bg="#D3D3D3",
                                      font=("Arial", 10), anchor=W, borderwidth=1,
                                      command=lambda conversation_object=seller_conversation_object:
                                      update_text_of_messages(conversation_object, False))
                title_button.place(x=335, y=(rows * 75) + 100, width=300, height=22)
                list_of_objects.append(title_button)

                # Init id_label and adding it to the list of objects.
                id_label = Label(messages_page, text=f"ID: {seller_conversation_object.announcement_id}", anchor=E,
                                 bg="#D3D3D3", font=("Arial", 9))
                id_label.place(x=564, y=(rows * 75) + 123, width=70, height=15)
                list_of_objects.append(id_label)

                # Init name_label and adding it to the list of objects.
                name_label = Label(messages_page, text=f"Kupujący: {seller_conversation_object.first_name}", anchor=W,
                                   bg="#D3D3D3", font=("Arial", 9))
                name_label.place(x=335, y=(rows * 75) + 123, width=227, height=15)
                list_of_objects.append(name_label)

                rows += 1
                if rows == 7:
                    break

            # Updating buttons depending on the number of the current page and the number of downloaded conversations.
            Functions.config_buttons(actual_page, button_previous_seller, button_next_seller, conversations_as_seller,
                                     config_conversations_page_as_seller, list_of_objects, 7)

        # Calling the button creation function and assigning the returned objects to variables.
        button_previous_customer, button_next_customer = Functions.create_buttons(messages_page, 15, 254)
        button_previous_seller, button_next_seller = Functions.create_buttons(messages_page, 335, 574)
        # The first call to the page setup functions.
        config_conversations_page_as_customer()
        config_conversations_page_as_seller()

        choose_conversation_label = Label(messages_page, bg="#A9A9A9", font=("Arial", 20),
                                          text=f"Wybierz konwersacje, {Config_data.logged_in_user_info.first_name}")
        choose_conversation_label.place(x=750, y=250)
        # Message window objects will be stored in this list and then deleted when a new window is created.
        list_of_objects_to_destroy = []

        def update_text_of_messages(conversation_object, is_user_customer):
            """The function supports the display of new message windows and the correct destruction of old windows."""
            nonlocal choose_conversation_label
            # Removing the label the first time the function is called.
            if isinstance(choose_conversation_label, Label):
                choose_conversation_label.destroy()
                choose_conversation_label = None

            # Destroying objects of the previous window.
            for element in list_of_objects_to_destroy:
                element.destroy()
            # Clearing objects of the previous window.
            list_of_objects_to_destroy.clear()

            # Init text object for displaying messages and adding it to the list of objects.
            text = Text(messages_page, width=67, height=30, bg="#D3D3D3", borderwidth=0, font=("Arial", 12))
            text.place(x=650, y=50)
            list_of_objects_to_destroy.append(text)

            # Init scrollbar object for scrolling messages and adding it to the list of objects.
            scrollbar = Scrollbar(messages_page, command=text.yview)
            scrollbar.place(x=1258, y=50, height=577)
            list_of_objects_to_destroy.append(scrollbar)

            # Configuration of the scrollbar object with the text object.
            text["yscrollcommand"] = scrollbar.set
            # Configure the message setting function on the right.
            text.bind("<Configure>", Functions.set_right)
            person = "Sprzedający" if is_user_customer else "Kupujący"

            # Init title_label and adding it to the list of objects.
            title_label = Label(messages_page, text=conversation_object.title, anchor=W, font=("Arial", 16),
                                bg="#A9A9A9")
            title_label.place(x=650, y=15, width=370)
            list_of_objects_to_destroy.append(title_label)

            # Init person_label and adding it to the list of objects.
            person_label = Label(messages_page, text=f"{person}: {conversation_object.first_name}", anchor=E,
                                 font=("Arial", 16), bg="#A9A9A9")
            person_label.place(x=1025, y=15, width=250)
            list_of_objects_to_destroy.append(person_label)

            # Init message_entry to enter message text and adding it to the list of objects.
            message_entry = Entry(messages_page, width=41, font=("Arial", 16))
            message_entry.place(x=650, y=600)
            message_entry.insert(0, "Napisz wiadomość...")
            message_entry.bind("<Button-1>", lambda event: Functions.delete_text(message_entry))
            list_of_objects_to_destroy.append(message_entry)

            # Init send_button to send message text and adding it to the list of objects.
            send_button = Button(messages_page, text="Wyślij", width=11, borderwidth=1, font=("Arial", 11))
            send_button.place(x=1150, y=600)
            list_of_objects_to_destroy.append(send_button)

            def refresh_messages():
                """The function is responsible for downloading messages, appropriate text display and configuration
                of the button for sending messages."""
                # Downloading messages from conversation_object and assigning them to a variable.
                list_of_message_objects = Functions.download_messages(conversation_object=conversation_object)

                # Setting the default values of the text object before adding the message.
                text["state"] = "normal"
                text.delete("1.0", END)

                i = 1
                # Displaying messages in the appropriate position depending on who sent the message.
                for message in list_of_message_objects:
                    position = f"{i}.0"
                    if message.customer_flag == 1:
                        text.insert(position, f"{message.first_name}\n{message.post_date}\n{message.content}\n\n")
                    else:
                        text.insert(position, f"\t{message.first_name}\n\t{message.post_date}"
                                              f"\n\t{message.content}\n\n")
                    i += 4

                # Setting state on disabled.
                text["state"] = "disabled"
                # Setting send_button with correct state and function.
                if list_of_message_objects:
                    send_button.config(command=lambda: Functions.send_message(list_of_message_objects, message_entry,
                                                                              refresh_messages, is_user_customer))
                else:
                    send_button.config(state="disabled")

            # First function call.
            refresh_messages()
        # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
        Config_data.current_page = messages_page

    # Showing communicate if user is not logged in.
    else:
        messagebox.showwarning("Nie jesteś zalogowany.", "Aby zobaczyć wiadomości musisz sie zalogować.")


def init_favorite_page_frame(root):
    """Function of a page with the user's favorite announcements, from this page the user can unlike an announcement,
    send a message to seller, view the announcement. The page also has pagination for active and completed favorite
    announcements."""
    # Checking if user is logged in.
    if Config_data.is_user_logged_in:
        # Destroying current_page.
        Config_data.current_page.destroy()
        # Init favorite_page object for root.
        favorite_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
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
            user_fav_active_announcements = Functions.download_user_favorite_announcements(1, actual_page, 8)

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
                Functions.init_label_objects_of_announcement(favorite_page, user_fav_active_announcement_object, x1, x2,
                                                             x3, y1, y2, y3, list_of_objects)

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
                                       Functions.delete_announcement_from_favorite(announcement_object,
                                                                                   init_favorite_page_frame, root))
                unlike_button.place(x=x2, y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(unlike_button)

                rows += 1
                if rows == 4:
                    rows = 0
                    columns += 1
                    if rows == 0 and columns == 2:
                        break

            # Updating buttons depending on the number of the current page and the number of downloaded announcements.
            Functions.config_buttons(actual_page, button_previous_active, button_next_active,
                                     user_fav_active_announcements, config_page_of_fav_active_announcements,
                                     list_of_objects, 8)

        def config_page_of_fav_completed_announcements(actual_page=1, list_of_objects=None):
            """Pagination function for completed favorite announcements."""
            # Retrieving the list of completed_favorite_announcements from function called with specified arguments.
            user_fav_completed_announcements = Functions.download_user_favorite_announcements(0, actual_page, 4)

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
                Functions.init_label_objects_of_announcement(favorite_page, user_fav_completed_announcement_object, x1,
                                                             x2, x3, y1, y2, y3, list_of_objects)

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
                                       Functions.delete_announcement_from_favorite(announcement_object,
                                                                                   init_favorite_page_frame, root))
                delete_button.place(x=1008, y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(delete_button)

                rows += 1
                if rows == 4:
                    break

            # Updating buttons depending on the number of the current page and the number of downloaded announcements.
            Functions.config_buttons(actual_page, button_previous_completed, button_next_completed,
                                     user_fav_completed_announcements, config_page_of_fav_completed_announcements,
                                     list_of_objects, 4)

        # Calling the button creation function and assigning the returned objects to variables.
        button_previous_active, button_next_active = Functions.create_buttons(favorite_page, 15, 785)
        button_previous_completed, button_next_completed = Functions.create_buttons(favorite_page, 865, 1200)
        # The first call to the page setup functions.
        config_page_of_fav_active_announcements()
        config_page_of_fav_completed_announcements()
        # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
        Config_data.current_page = favorite_page

    # Displaying warning.
    else:
        messagebox.showwarning("Nie jesteś zalogowany.",
                               "Aby zobaczyć ulubione ogłoszenia musisz sie zalogować.")


def init_message_window(announcement_object):
    """A function that initializes an additional message window, the user can use it to display and send a message to
    another user's announcement. Then sent message will be displayed on the message page of both the buyer and the
    seller."""
    # Checking if user is logged in.
    if Config_data.is_user_logged_in:
        # When user is logged in, program checking if selected announcement isn't user's announcement.
        if Config_data.logged_in_user_info.user_id != announcement_object.seller_id:
            # Init message_window from Toplevel class.
            message_window = Toplevel()
            # Adding a window to the global list so that if the window is not closed, the window will automatically
            # close when logging out.
            Config_data.list_of_active_windows.append(message_window)
            # Determining the window dimensions.
            message_window_width = 477
            message_window_height = 484
            screen_width = message_window.winfo_screenwidth()
            screen_height = message_window.winfo_screenheight()
            center_x = int(screen_width / 2 - message_window_width / 2)
            center_y = int(screen_height / 2 - message_window_height / 2)
            # Setting the dimensions and position of the window.
            message_window.geometry(f"{message_window_width}x{message_window_height}+{center_x}+{center_y}")
            # Setting the title, resizable, background color and icon-photo.
            message_window.title(announcement_object.first_name)
            message_window.resizable(width=True, height=True)
            message_window.config(bg="#B0C4DE")
            message_window.wm_iconphoto(False, PhotoImage(file="Photos/messages_icon.png"))

            # Init labels with information.
            Label(message_window, width=68, height=1, text=announcement_object.title, anchor=W).pack()
            Label(message_window, width=68, height=1, text=f"Cena: {announcement_object.price} ZŁ", anchor=W).pack()
            Label(message_window, width=80, height=1, text=f"ID: {announcement_object.announcement_id}", anchor=W,
                  font=("Arial", 8)).pack()

            # Init text object for displaying messages.
            text = Text(message_window, width=57, height=26, bg="#D3D3D3")
            text.pack(side=LEFT)

            # Init scrollbar object.
            scrollbar = Scrollbar(message_window, command=text.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Connecting a scrollbar object to a text object.
            text["yscrollcommand"] = scrollbar.set
            # Configure the text object to display messages on the right side.
            text.bind("<Configure>", Functions.set_right)

            # Init the message_entry object for entering the message text.
            message_entry = Entry(message_window, font=("Arial", 14))
            message_entry.place(x=0, y=457, width=385)
            message_entry.insert(0, "Napisz wiadomość...")
            message_entry.bind("<Button-1>", lambda event: Functions.delete_text(message_entry))

            # Init send_button to send messages.
            send_button = Button(message_window, text="Wyślij", width=9, borderwidth=1)
            send_button.place(x=389, y=457)

            def refresh_messages():
                """The function is responsible for downloading messages, appropriate text display and configuration of
                the button for sending messages."""
                # Downloading list of messages from announcement object.
                list_of_message_objects = Functions.download_messages(announcement_object=announcement_object)
                # Setting default values for text object.
                text["state"] = "normal"
                text.delete("1.0", END)

                i = 1
                # Appropriate positioning of the message on the text object depending on who sent the message.
                for message in list_of_message_objects:
                    position = f"{i}.0"
                    if message.customer_flag == 1:
                        text.insert(position, f"{message.first_name}\n{message.post_date}\n{message.content}\n\n")
                    else:
                        text.insert(position, f"\t{message.first_name}\n\t{message.post_date}"
                                              f"\n\t{message.content}\n\n")
                    i += 4

                # Setting text state on disabled.
                text["state"] = "disabled"
                # Setting the correct function for the button
                send_button.config(command=lambda: Functions.send_message(list_of_message_objects, message_entry,
                                                                          refresh_messages, True,
                                                                          announcement_object))

            # First function call.
            refresh_messages()

        # Displaying correct warning.
        else:
            messagebox.showwarning("Nie możesz wysłać wiadomości do samego siebie.",
                                   "Próbujesz wysłać wiadomość do własnego ogłoszenia.")
    # Displaying correct warning.
    else:
        messagebox.showwarning("Nie jesteś zalogowany.", "Aby wysłać wiadomość, musisz sie zalogować.")
