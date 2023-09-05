# Modules import.
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
# Import modules with functions and global variables.
import My_functions
import Config_data
from User_Class import PhotoButton
from datetime import datetime


# Initialization main window of application.
def init_main_window():
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
    root.title("SHOPPER.PL")
    root.resizable(width=True, height=True)
    # Creating background color and icon of app.
    root.config(bg="#B0C4DE")
    root.call("wm", "iconphoto", root._w, PhotoImage(file="Photos/home_icon.png"))

    # Returning root into Main.py
    return root


# Initialization of the top panel for user selection of pages.
def init_top_panel(root):
    # Init top panel label for root
    top_panel_frame = Frame(root, width=1280, height=80)
    top_panel_frame.pack()

    # Init home button for top panel
    home_button = Button(top_panel_frame, text="SHOPPER", width=30, height=2, borderwidth=0, bg="#D3D3D3",
                         command=lambda: init_shopper_page_frame(root))
    home_button.place(x=20, y=20)

    # Init search engine for label
    search_engine = Entry(top_panel_frame, font=("Arial", 11), width=36, borderwidth=0, bg="#D3D3D3")
    search_engine.place(x=280, y=10)
    search_engine.insert(0, "Czego szukasz ?")
    search_engine.bind("<Button-1>", lambda event: My_functions.delete_text(search_engine))

    # Init search location for label
    search_location = Entry(top_panel_frame, font=("Arial", 11), width=36, borderwidth=0, bg="#D3D3D3")
    search_location.place(x=280, y=30)

    # Init enter location label for label2
    enter_location_label = Label(top_panel_frame, text="Wpisz lokalizacje")
    enter_location_label.place(x=580, y=30)

    # Init select category label for label2
    select_category_label = Label(top_panel_frame, text="Wybierz kategorie")
    select_category_label.place(x=580, y=50)

    # Init categories for top panel
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="#D3D3D3", background="white")
    current_var = StringVar()
    categories = ttk.Combobox(top_panel_frame, textvariable=current_var, width=45, state="readonly",
                              values=Config_data.categories)
    categories.place(x=280, y=50)

    # Init search button for top panel
    search_button = Button(top_panel_frame, text="Wyszukaj produkt", borderwidth=0, bg="#D3D3D3",
                           command=lambda: init_shopper_page_frame(root, search_engine, search_location,
                                                                   current_var, categories, True))
    search_button.place(x=580, y=6)

    # Init favorite button for top panel
    favorite_button = Button(top_panel_frame, text="Ulubione", width=16, height=2, borderwidth=0, bg="#D3D3D3",
                             command=lambda: init_favorite_page_frame(root))
    favorite_button.place(x=730, y=20)

    # Init messages button for top panel
    messages_button = Button(top_panel_frame, text="Wiadomości", width=16, height=2, borderwidth=0, bg="#D3D3D3",
                             command=lambda: init_messages_page_frame(root))
    messages_button.place(x=865, y=20)

    # Init add announcement button for top panel
    add_announcement_button = Button(top_panel_frame, text="Dodaj ogłoszenie", width=16, height=2, borderwidth=0,
                                     bg="#D3D3D3", command=lambda: init_add_announcement_page_frame(root))
    add_announcement_button.place(x=1000, y=20)

    # Init account button for top panel
    account_button = Button(top_panel_frame, text="Twoje konto", width=16, height=2, borderwidth=0, bg="#D3D3D3",
                            command=lambda: is_user_logged_to_user_page(top_panel_frame, root))
    account_button.place(x=1135, y=20)


def is_user_logged_to_user_page(top_panel_frame, root):
    if Config_data.is_user_logged_in:
        init_user_page_frame(root)
    else:
        init_login_window(top_panel_frame, root)


def init_login_window(top_panel_frame, root):
    # Init login window
    login_window = Toplevel()
    Config_data.list_of_active_windows.append(login_window)
    login_window_width = 400
    login_window_height = 719
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    center_x = int(screen_width / 2 - login_window_width / 2)
    center_y = int(screen_height / 2 - login_window_height / 2)
    login_window.geometry(f"{login_window_width}x{login_window_height}+{center_x}+{center_y}")
    login_window.title("Logowanie")
    login_window.resizable(width=True, height=True)
    login_window.config(bg="#B0C4DE")
    login_window.wm_iconphoto(False, PhotoImage(file="Photos/login_icon.png"))

    login_window_label = Label(login_window)
    login_window_label.grid(row=0, column=0, columnspan=2, rowspan=13, ipady=2, ipadx=2)

    login_heading = Label(login_window_label, text="Zaloguj się", font="Arial")
    login_heading.grid(row=0, column=0, pady=(10, 0))

    label_login_or_email = Label(login_window_label, text="Login lub email", font="Arial")
    label_login_or_email.grid(row=1, column=1, pady=10)

    entry_login_or_email = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    entry_login_or_email.grid(row=1, column=0, pady=10, ipadx=25, padx=(20, 0))

    label_password = Label(login_window_label, text="Hasło", font="Arial")
    label_password.grid(row=2, column=1, pady=10)

    entry_password = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    entry_password.grid(row=2, column=0, pady=10, ipadx=25, padx=(20, 0))

    login_button = Button(login_window_label, text="Zaloguj się", font=("Arial", 10), borderwidth=0, bg="#D3D3D3",
                          command=lambda: My_functions.login_user(entry_login_or_email, entry_password, top_panel_frame,
                                                                  init_shopper_page_frame, root))
    login_button.grid(row=3, column=1, ipadx=10, ipady=8, pady=(10, 0))

    separator = ttk.Separator(login_window_label, orient="horizontal")
    separator.grid(row=4, columnspan=2, ipadx=185, pady=15, padx=10)

    register_heading = Label(login_window_label, text="Zarejestruj sie", font="Arial")
    register_heading.grid(row=5, column=0, pady=(0, 10))
    # ________________________________________________________________________
    first_name_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    first_name_entry.grid(row=6, column=0, pady=10, ipadx=25, padx=(20, 0))

    first_name_label = Label(login_window_label, text="Imie*", font="Arial")
    first_name_label.grid(row=6, column=1)
    # ________________________________________________________________________
    last_name_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    last_name_entry.grid(row=7, column=0, pady=10, ipadx=25, padx=(20, 0))

    last_name_label = Label(login_window_label, text="Nazwisko*", font="Arial")
    last_name_label.grid(row=7, column=1)
    # ________________________________________________________________________
    email_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    email_entry.grid(row=8, column=0, pady=10, ipadx=25, padx=(20, 0))

    email_label = Label(login_window_label, text="E-mail*", font="Arial")
    email_label.grid(row=8, column=1)
    # ________________________________________________________________________
    login_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    login_entry.grid(row=9, column=0, pady=(10, 4), ipadx=25, padx=(20, 0))

    login_label = Label(login_window_label, text="Login*", font="Arial")
    login_label.grid(row=9, column=1)

    login_check = Button(login_window_label, text="Zweryfikuj login", borderwidth=0, bg="#D3D3D3",
                         command=lambda: My_functions.verify_login(login_entry))
    login_check.grid(row=10, column=0, sticky=E, pady=(0, 10), padx=(0, 8))

    login_pattern = Button(login_window_label, text="Wzór loginu", borderwidth=0, bg="#D3D3D3",
                           command=lambda: My_functions.show_pattern(login_pattern["text"]))
    login_pattern.grid(row=10, column=0, sticky=W, pady=(0, 10), padx=(26, 0))
    # ________________________________________________________________________
    password_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    password_entry.grid(row=11, column=0, pady=(10, 4), ipadx=25, padx=(20, 0))

    password_label = Label(login_window_label, text="Hasło*", font="Arial")
    password_label.grid(row=11, column=1)

    password_check = Button(login_window_label, text="Zweryfikuj hasło", borderwidth=0, bg="#D3D3D3",
                            command=lambda: My_functions.verify_password(password_entry))
    password_check.grid(row=12, column=0, sticky=E, pady=(0, 10), padx=(0, 8))

    password_pattern = Button(login_window_label, text="Wzór hasła", borderwidth=0, bg="#D3D3D3",
                              command=lambda: My_functions.show_pattern(password_pattern["text"]))
    password_pattern.grid(row=12, column=0, sticky=W, pady=(0, 10), padx=(26, 0))
    # ________________________________________________________________________
    combobox_day_var = StringVar()
    combobox_day_birthday = ttk.Combobox(login_window_label, textvariable=combobox_day_var, width=6, state="readonly")
    combobox_day_birthday["values"] = [i for i in range(1, 32)]

    combobox_day_birthday.grid(row=13, column=0, sticky=W, pady=10, padx=(26, 0))

    combobox_month_var = StringVar()
    combobox_month_birthday = ttk.Combobox(login_window_label, textvariable=combobox_month_var, width=10,
                                           state="readonly")
    combobox_month_birthday["values"] = ("Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec",
                                         "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień")
    combobox_month_birthday.grid(row=13, column=0, padx=(20, 0))

    combobox_year_var = StringVar()
    combobox_year_birthday = ttk.Combobox(login_window_label, textvariable=combobox_year_var, width=6, state="readonly")
    combobox_year_birthday["values"] = [i for i in range(1900, 2024)]
    combobox_year_birthday.grid(row=13, column=0, sticky=E, padx=(0, 7))

    birthday_label = Label(login_window_label, text="Data urodzenia*", font="Arial")
    birthday_label.grid(row=13, column=1)
    # ________________________________________________________________________
    street_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    street_entry.grid(row=14, column=0, pady=10, ipadx=25, padx=(20, 0))

    street_label = Label(login_window_label, text="Ulica", font="Arial")
    street_label.grid(row=14, column=1)
    # ________________________________________________________________________
    zip_code_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    zip_code_entry.grid(row=15, column=0, pady=10, ipadx=25, padx=(20, 0))

    zip_code_label = Label(login_window_label, text="Kod pocztowy", font="Arial")
    zip_code_label.grid(row=15, column=1)
    # ________________________________________________________________________
    city_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    city_entry.grid(row=16, column=0, pady=10, ipadx=25, padx=(20, 0))

    city_label = Label(login_window_label, text="Miasto", font="Arial")
    city_label.grid(row=16, column=1)
    # ________________________________________________________________________
    register_button = Button(login_window_label, text="Załóż konto", font=("Arial", 10), borderwidth=0, bg="#D3D3D3",
                             command=lambda: My_functions.register_user(first_name_entry, last_name_entry, email_entry,
                                                                        login_entry, password_entry, combobox_day_var,
                                                                        combobox_day_birthday, combobox_month_var,
                                                                        combobox_month_birthday, combobox_year_var,
                                                                        combobox_year_birthday, street_entry,
                                                                        zip_code_entry, city_entry))
    register_button.grid(row=17, column=1, ipadx=10, ipady=8, pady=10)
    info_label = Label(login_window_label, text="*Pole wymagane")
    info_label.grid(row=17, column=0, pady=(0, 10), sticky=SW)


def init_add_announcement_page_frame(root):
    if Config_data.is_user_logged_in:
        Config_data.current_page.destroy()
        add_announcement_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                                      highlightthickness=2)
        add_announcement_page.pack()

        Label(add_announcement_page, text="Utwórz swoje ogłoszenie!", font=("Arial", 27), borderwidth=0,
              bg="#A9A9A9").place(x=70, y=30)
        ttk.Separator(add_announcement_page).place(x=40, y=85, width=465)

        Label(add_announcement_page, text="Tytuł ogłoszenia*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
            x=360, y=100)
        title_entry = Entry(add_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
        title_entry.place(x=40, y=130, width=465)

        Label(add_announcement_page, text="Lokalizacja*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=109,
                                                                                                                 y=170)
        location_entry = Entry(add_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
        location_entry.place(x=40, y=200, width=170)

        Label(add_announcement_page, text="Kategoria*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=302,
                                                                                                               y=170)
        current_var_category = StringVar()
        select_categories = ttk.Combobox(add_announcement_page, textvariable=current_var_category, font=("Arial", 13),
                                         state="readonly", values=Config_data.categories)
        select_categories.place(x=223, y=200, width=170)

        Label(add_announcement_page, text="Kwota*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=444, y=170)
        price_entry = Entry(add_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
        price_entry.place(x=405, y=200, width=100)
        Label(add_announcement_page, text="ZŁ", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=510, y=200)

        Label(add_announcement_page, text="Stan*", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=683, y=15)
        current_var_state = StringVar()
        select_state = ttk.Combobox(add_announcement_page, textvariable=current_var_state, font=("Arial", 13),
                                    state="readonly", values=Config_data.states)
        select_state.place(x=560, y=40, width=170)

        Label(add_announcement_page, text="Numer telefonu", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
            x=789, y=15)
        mobile_number_entry = Entry(add_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
        mobile_number_entry.place(x=750, y=40, width=170)

        Label(add_announcement_page, text="Opis*", borderwidth=0, font=("Arial", 20), bg="#A9A9A9").place(x=1164, y=15)
        Label(add_announcement_page, text="Wpisz minimum 80 znaków", borderwidth=0, font=("Arial", 11),
              bg="#A9A9A9").place(x=1050, y=47)
        description_text = Text(add_announcement_page, width=61, height=24, font=("Arial", 14), borderwidth=0)
        description_text.place(x=560, y=70)
        Label(add_announcement_page, text="*Pole wymagane", borderwidth=0, font=("Arial", 8), bg="#A9A9A9").place(
            x=40, y=600)

        rows = 0
        columns = 0
        list_of_photo_button_objects = []
        for i in range(8):
            photo_button = Button(add_announcement_page, bg="#D3D3D3", image=Config_data.images["camera_icon"],
                                  state="disabled", borderwidth=0)
            photo_button.place(x=40+(columns*175), y=250+(rows*100), width=115, height=75)
            photo_button_object = PhotoButton(photo_button, None, None, 40+(columns*175),
                                              250+(rows*100), 0, None, False,
                                              False)

            list_of_photo_button_objects.append(photo_button_object)

            photo_button.config(command=lambda selected_button_object=photo_button_object: My_functions.
                                set_main_photo(selected_button_object, list_of_photo_button_objects))

            rows += 1
            if rows == 3:
                rows = 0
                columns += 1

        Label(add_announcement_page, text="Naciśnij na obraz, aby wybrać zdjęcie główne."
                                          " W razie niewybrania, pierwsze zdjęcie będzie zdjęciem głównym.",
              bg="#D3D3D3", font=("Arial", 7), anchor=W).place(x=40, y=228, width=465)

        Button(add_announcement_page, bg="#D3D3D3", text="Dodaj zdjęcie", font=("Arial", 10),
               command=lambda: My_functions.select_photo(list_of_photo_button_objects, add_announcement_page)).place(
            x=390, y=450, width=115, height=75)

        Button(add_announcement_page, bg="#00BFFF", text="Dodaj ogłoszenie!", borderwidth=0, font=("Arial", 15),
               command=lambda: My_functions.add_announcement(title_entry, location_entry, current_var_category,
                                                             price_entry, description_text, select_categories,
                                                             list_of_photo_button_objects, select_state,
                                                             current_var_state, mobile_number_entry)).place(x=40, y=550,
                                                                                                            width=465,
                                                                                                            height=50)

        Config_data.current_page = add_announcement_page

    else:
        messagebox.showwarning("Nie jesteś zalogowany.", "Aby dodać ogłoszenie musisz sie zalogować.")


def init_user_page_frame(root):
    Config_data.current_page.destroy()
    account_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                         highlightthickness=2)
    account_page.pack()

    # Init account_page separates
    ttk.Separator(account_page).place(x=427, y=15, height=600)
    ttk.Separator(account_page).place(x=854, y=15, height=600)

    ttk.Separator(account_page).place(x=40, y=85, width=350)
    ttk.Separator(account_page).place(x=465, y=85, width=350)
    ttk.Separator(account_page).place(x=890, y=85, width=350)
    ttk.Separator(account_page).place(x=40, y=140, width=350)

    Label(account_page, text="Dane użytkownika", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=70, y=30)
    Label(account_page, text="Aktywne ogłoszenia", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=485, y=30)
    Label(account_page, text="Zakończone ogłoszenia", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=875,
                                                                                                             y=30)
    time_delta = datetime.now().replace(microsecond=0) - Config_data.logged_in_user_info.creation_account_date
    Label(account_page, text=f"Jesteś z nami od {time_delta.days} dni.", font=("Arial", 20), borderwidth=0,
          bg="#A9A9A9").place(x=0, y=100, width=427)

    list_of_texts_and_user_info = [("Imie:", Config_data.logged_in_user_info.first_name),
                                   ("Nazwisko:", Config_data.logged_in_user_info.last_name),
                                   ("Email:", Config_data.logged_in_user_info.email),
                                   ("Login:", Config_data.logged_in_user_info.login),
                                   ("Hasło:", Config_data.logged_in_user_info.password),
                                   ("Data urodzenia:", Config_data.logged_in_user_info.date_of_birth),
                                   ("Ulica:", Config_data.logged_in_user_info.street),
                                   ("Kod pocztowy:", Config_data.logged_in_user_info.zip_code),
                                   ("Miasto:", Config_data.logged_in_user_info.city)]

    y = 0
    i = 0
    hidden_password = True
    for text, user_info in list_of_texts_and_user_info:
        label = Label(account_page, text=f"{text} {user_info}", anchor=W, font=("Arial", 10), bg="#D3D3D3")
        label.place(x=10, y=(y * 52) + 160, width=200, height=30)
        entry = Entry(account_page, font=("Arial", 9))
        entry.place(x=220, y=(y * 52) + 160, width=200, height=30)
        if i == 3 or i == 5:
            entry.insert("0", "Nie możesz zmienić tych danych")
            entry["state"] = "disabled"

        else:
            if i == 4:
                password_label = label
                password_label.config(text=f"{text} {'*'*len(user_info)}")
                button = Button(account_page, text="Pokaż hasło", font=("Arial", 7), borderwidth=0, bg="#D3D3D3",
                                command=lambda: show_password())
                button.place(x=155, y=350, width=55)
            entry.insert("0", "Zmień dane, enter aby zatwierdzić")
            entry.bind("<Button-1>", lambda event, e=entry: My_functions.delete_text(e))
            entry.bind("<Return>", lambda event, e=entry, l=label: My_functions.change_user_data(e, l, hidden_password))
        i += 1
        y += 1

    def show_password():
        nonlocal hidden_password
        hidden_password = False
        button.config(text="Ukryj hasło", command=lambda: hide_password())
        password_label.config(text=f"Hasło: {Config_data.logged_in_user_info.password}")

    def hide_password():
        nonlocal hidden_password
        hidden_password = True
        button.config(text="Pokaż hasło", command=lambda: show_password())
        password_label.config(text=f"Hasło: {'*' * len(Config_data.logged_in_user_info.password)}")

    def config_page_of_user_active_announcements(actual_page=1, list_of_objects=None):
        user_active_announcements = My_functions.download_user_announcements(1, actual_page)

        if list_of_objects:

            for element in list_of_objects:
                element.destroy()

        list_of_objects = []

        rows = 0
        # Init user active announcements
        for user_active_announcement_object in user_active_announcements:
            photo_label = Label(account_page, bg="#D3D3D3", image=user_active_announcement_object.main_photo)
            photo_label.place(x=465, y=(rows * 120) + 162, width=115, height=67)
            list_of_objects.append(photo_label)

            title_button = Button(account_page, text=user_active_announcement_object.title, anchor=W,
                                  font=("Arial", 10), bg="#D3D3D3", borderwidth=1,
                                  command=lambda announcement_object=user_active_announcement_object:
                                  init_announcement_page_frame(account_page, announcement_object, True,
                                                               True))
            title_button.place(x=465, y=(rows * 120) + 138, width=350, height=22)
            list_of_objects.append(title_button)

            category_label = Label(account_page, text=user_active_announcement_object.name_category, anchor=W,
                                   font=("Arial", 8), bg="#D3D3D3")
            category_label.place(x=583, y=(rows * 120) + 162, width=114, height=13)
            list_of_objects.append(category_label)

            location_label = Label(account_page, text=user_active_announcement_object.location, anchor=W,
                                   font=("Arial", 8), bg="#D3D3D3")
            location_label.place(x=583, y=(rows * 120) + 177, width=114, height=13)
            list_of_objects.append(location_label)

            price_label = Label(account_page, text=f"{user_active_announcement_object.price} ZŁ", anchor=E,
                                font=("Arial", 10), bg="#D3D3D3")
            price_label.place(x=700, y=(rows * 120) + 162, width=114, height=13)
            list_of_objects.append(price_label)

            state_label = Label(account_page, text=user_active_announcement_object.state, anchor=E, font=("Arial", 8),
                                bg="#D3D3D3")
            state_label.place(x=700, y=(rows * 120) + 177, width=114, height=13)
            list_of_objects.append(state_label)

            date_label = Label(account_page, text=f"Dodano: {user_active_announcement_object.creation_date}", anchor=W,
                               font=("Arial", 8), bg="#D3D3D3")
            date_label.place(x=583, y=(rows * 120) + 192, width=231, height=13)
            list_of_objects.append(date_label)

            edit_button = Button(account_page, text="Edytuj", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                 command=lambda announcement_object=user_active_announcement_object:
                                 init_edit_user_announcement_page_frame(announcement_object, root))
            edit_button.place(x=700, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(edit_button)

            complete_button = Button(account_page, text="Zakończ", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                     command=lambda announcement_object=user_active_announcement_object:
                                     My_functions.move_active_announcement_to_completed_announcements(
                                         announcement_object, init_user_page_frame, root))
            complete_button.place(x=583, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(complete_button)

            rows += 1
            if rows == 4:
                break

        My_functions.config_buttons(actual_page, button_previous_active, button_next_active, user_active_announcements,
                                    config_page_of_user_active_announcements, list_of_objects, 4)

    def config_page_of_user_completed_announcements(actual_page=1, list_of_objects=None):
        user_completed_announcements = My_functions.download_user_announcements(0, actual_page)

        if list_of_objects:

            for element in list_of_objects:
                element.destroy()

        list_of_objects = []

        rows = 0
        # Init user completed announcements
        for user_completed_announcement_object in user_completed_announcements:
            photo_label = Label(account_page, bg="#D3D3D3", image=user_completed_announcement_object.main_photo)
            photo_label.place(x=890, y=(rows * 120) + 162, width=115, height=67)
            list_of_objects.append(photo_label)

            title_button = Button(account_page, text=user_completed_announcement_object.title, anchor=W,
                                  font=("Arial", 10), bg="#D3D3D3", borderwidth=1,
                                  command=lambda announcement_object=user_completed_announcement_object:
                                  init_announcement_page_frame(account_page, announcement_object, True, True))
            title_button.place(x=890, y=(rows * 120) + 138, width=350, height=22)
            list_of_objects.append(title_button)

            category_label = Label(account_page, text=user_completed_announcement_object.name_category, anchor=W,
                                   font=("Arial", 8), bg="#D3D3D3")
            category_label.place(x=1008, y=(rows * 120) + 162, width=114, height=13)
            list_of_objects.append(category_label)

            location_label = Label(account_page, text=user_completed_announcement_object.location, anchor=W,
                                   font=("Arial", 8), bg="#D3D3D3")
            location_label.place(x=1008, y=(rows * 120) + 177, width=114, height=13)
            list_of_objects.append(location_label)

            price_label = Label(account_page, text=f"{user_completed_announcement_object.price} ZŁ", anchor=E,
                                font=("Arial", 10), bg="#D3D3D3")
            price_label.place(x=1125, y=(rows * 120) + 162, width=114, height=13)
            list_of_objects.append(price_label)

            state_label = Label(account_page, text=user_completed_announcement_object.state, anchor=E,
                                font=("Arial", 8), bg="#D3D3D3")
            state_label.place(x=1125, y=(rows * 120) + 177, width=114, height=13)
            list_of_objects.append(state_label)

            date_label = Label(account_page, text=f"Dodano: {user_completed_announcement_object.creation_date}",
                               anchor=W, font=("Arial", 8), bg="#D3D3D3")
            date_label.place(x=1008, y=(rows * 120) + 192, width=231, height=13)
            list_of_objects.append(date_label)

            activate_button = Button(account_page, text="Aktywuj", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                     command=lambda announcement_object=user_completed_announcement_object:
                                     My_functions.move_completed_announcement_to_active_announcements(
                                         announcement_object, init_user_page_frame, root))
            activate_button.place(x=1125, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(activate_button)

            delete_button = Button(account_page, text="Usuń", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                   command=lambda announcement_object=user_completed_announcement_object:
                                   My_functions.delete_from_completed_announcements(
                                       announcement_object, init_user_page_frame, root))
            delete_button.place(x=1008, y=(rows * 120) + 207, width=115, height=22)
            list_of_objects.append(delete_button)

            rows += 1
            if rows == 4:
                break

        My_functions.config_buttons(actual_page, button_previous_completed, button_next_completed,
                                    user_completed_announcements, config_page_of_user_completed_announcements,
                                    list_of_objects, 4)

    button_previous_active, button_next_active = My_functions.create_buttons(account_page, 438, 785)
    button_previous_completed, button_next_completed = My_functions.create_buttons(account_page, 865, 1200)
    config_page_of_user_active_announcements()
    config_page_of_user_completed_announcements()

    Config_data.current_page = account_page


def init_edit_user_announcement_page_frame(announcement_object, root):
    Config_data.current_page.destroy()
    edit_user_announcement_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                                        highlightthickness=2)
    edit_user_announcement_page.pack()

    Label(edit_user_announcement_page, text="Edytuj swoje ogłoszenie!", font=("Arial", 27), borderwidth=0,
          bg="#A9A9A9").place(x=70, y=30)
    ttk.Separator(edit_user_announcement_page).place(x=40, y=85, width=465)

    Label(edit_user_announcement_page, text=f"ID OGŁOSZENIA: {announcement_object.announcement_id}",
          font=("Arial", 7), borderwidth=0, bg="#A9A9A9").place(x=40, y=10)

    Label(edit_user_announcement_page, text="Tytuł ogłoszenia", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
        x=367, y=100)
    title_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
    title_entry.insert(0, announcement_object.title)
    title_entry.place(x=40, y=130, width=465)

    Label(edit_user_announcement_page, text="Lokalizacja", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=296,
                                                                                                                  y=170)
    location_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
    location_entry.insert(0, announcement_object.location)
    location_entry.place(x=40, y=200, width=350)

    Label(edit_user_announcement_page, text="Kwota", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=451,
                                                                                                            y=170)
    price_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
    price_entry.insert(0, announcement_object.price)
    price_entry.place(x=405, y=200, width=100)
    Label(edit_user_announcement_page, text="ZŁ", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=510, y=200)

    Label(edit_user_announcement_page, text="Stan", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(x=689, y=15)
    current_var_state = StringVar()
    select_state = ttk.Combobox(edit_user_announcement_page, textvariable=current_var_state, font=("Arial", 13),
                                state="readonly", values=Config_data.states)
    select_state.place(x=560, y=40, width=170)
    current_var_state.set(announcement_object.state)

    Label(edit_user_announcement_page, text="Numer telefonu", font=("Arial", 14), borderwidth=0, bg="#A9A9A9").place(
        x=789, y=15)
    mobile_number_entry = Entry(edit_user_announcement_page, font=("Arial", 14), borderwidth=0, bg="#D3D3D3")
    if announcement_object.mobile_number:
        mobile_number_entry.insert(0, announcement_object.mobile_number)
    mobile_number_entry.place(x=750, y=40, width=170)

    Label(edit_user_announcement_page, text="Opis", borderwidth=0, font=("Arial", 20), bg="#A9A9A9").place(x=1175, y=15)
    Label(edit_user_announcement_page, text="Wpisz minimum 80 znaków", borderwidth=0, font=("Arial", 11),
          bg="#A9A9A9").place(x=1050, y=47)
    description_text = Text(edit_user_announcement_page, width=61, height=24, font=("Arial", 14), borderwidth=0)
    description_text.insert(INSERT, announcement_object.description)
    description_text.place(x=560, y=70)

    rows = 0
    columns = 0
    list_of_photo_button_objects = []
    for i in range(8):
        photo_button = Button(edit_user_announcement_page, bg="#D3D3D3", image=Config_data.images["camera_icon"],
                              state="disabled", borderwidth=0)
        photo_button.place(x=40 + (columns * 175), y=250 + (rows * 100), width=115, height=75)
        photo_button_object = PhotoButton(photo_button, None, None, 40 + (columns * 175),
                                          250 + (rows * 100), 0, None, False,
                                          False)

        list_of_photo_button_objects.append(photo_button_object)

        photo_button.config(command=lambda selected_button_object=photo_button_object: My_functions.
                            set_main_photo(selected_button_object, list_of_photo_button_objects))

        rows += 1
        if rows == 3:
            rows = 0
            columns += 1

    photos_to_edit, error_with_getting_photos = My_functions.download_photos_to_announcement(
        announcement_object.announcement_id, True, 115, 75)
    deleted_photos = []

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

            delete_button = Button(edit_user_announcement_page, text="Usuń zdjęcie", font=("Arial", 8), borderwidth=0,
                                   bg="#D3D3D3", command=lambda button_object=list_of_photo_button_objects[i]:
                                   My_functions.delete_photo(button_object, deleted_photos))
            delete_button.place(x=list_of_photo_button_objects[i].position_x + 25,
                                y=list_of_photo_button_objects[i].position_y + 75)

            list_of_photo_button_objects[i].button_delete = delete_button

    Label(edit_user_announcement_page, text="Naciśnij na obraz, aby wybrać zdjęcie główne."
                                            " W razie niewybrania, pierwsze zdjęcie będzie zdjęciem głównym.",
          bg="#D3D3D3", font=("Arial", 7), anchor=W).place(x=40, y=228, width=465)

    add_photo_button = Button(edit_user_announcement_page, bg="#D3D3D3", text="Dodaj zdjęcie", font=("Arial", 10),
                              command=lambda: My_functions.select_photo(list_of_photo_button_objects,
                                                                        edit_user_announcement_page, deleted_photos))
    add_photo_button.place(x=390, y=450, width=115, height=75)
    if error_with_getting_photos:
        add_photo_button.config(text="Brak możliwości\ndodania zdjęcia", state="disabled")

    Button(edit_user_announcement_page, bg="#00BFFF", text="Zmień ogłoszenie!", borderwidth=0, font=("Arial", 15),
           command=lambda: My_functions.change_announcement_data(title_entry, location_entry, price_entry,
                                                                 description_text, announcement_object,
                                                                 init_user_page_frame, root, current_var_state,
                                                                 select_state, mobile_number_entry,
                                                                 list_of_photo_button_objects,
                                                                 deleted_photos)).place(x=40, y=550, width=465,
                                                                                        height=50)

    Config_data.current_page = edit_user_announcement_page


def init_shopper_page_frame(root, search_engine=None, search_location=None, current_var=None, categories=None,
                            from_search_engine=False):

    if isinstance(Config_data.current_page, Frame):
        Config_data.current_page.destroy()

    main_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black", highlightthickness=2)
    main_page.pack()
    ttk.Separator(main_page).place(x=427, y=15, height=600)
    ttk.Separator(main_page).place(x=854, y=15, height=600)

    def config_page_of_announcements(actual_page=1, list_of_objects=None, first_init=False):

        if from_search_engine:
            # Update all_announcements list from download_from_search_engine
            announcements = My_functions.download_announcements(from_search_engine, actual_page, first_init,
                                                                search_engine, search_location, current_var, categories)
        else:
            # Update all_announcements list from download_all_announcements
            announcements = My_functions.download_announcements(from_search_engine, actual_page, first_init)

        if list_of_objects:

            for element in list_of_objects:
                element.destroy()

        list_of_objects = []

        columns = 0
        rows = 0
        for announcement_object in announcements:
            photo_label = Label(main_page, bg="#D3D3D3", image=announcement_object.main_photo)
            photo_label.place(x=40 + (columns * 425), y=(rows * 120) + 42, width=115, height=67)
            list_of_objects.append(photo_label)

            title_button = Button(main_page, text=announcement_object.title, anchor=W, font=("Arial", 10),
                                  borderwidth=1, bg="#D3D3D3",
                                  command=lambda announcement=announcement_object:
                                  init_announcement_page_frame(main_page, announcement, False,
                                                               False))
            title_button.place(x=40 + (columns * 425), y=(rows * 120) + 18, width=350, height=22)
            list_of_objects.append(title_button)

            category_label = Label(main_page, text=announcement_object.name_category, anchor=W,
                                   font=("Arial", 8), bg="#D3D3D3")
            category_label.place(x=158 + (columns * 425), y=(rows * 120) + 42, width=114, height=13)
            list_of_objects.append(category_label)

            location_label = Label(main_page, text=announcement_object.location, anchor=W,
                                   font=("Arial", 8), bg="#D3D3D3")
            location_label.place(x=158 + (columns * 425), y=(rows * 120) + 57, width=114, height=13)
            list_of_objects.append(location_label)

            price_label = Label(main_page, text=f"{announcement_object.price} ZŁ", anchor=E, font=("Arial", 10),
                                bg="#D3D3D3")
            price_label.place(x=275 + (columns * 425), y=(rows * 120) + 42, width=114, height=13)
            list_of_objects.append(price_label)

            state_label = Label(main_page, text=announcement_object.state, anchor=E, font=("Arial", 8),
                                bg="#D3D3D3")
            state_label.place(x=275 + (columns * 425), y=(rows * 120) + 57, width=114, height=13)
            list_of_objects.append(state_label)

            date_label = Label(main_page, text=f"Dodano: {announcement_object.creation_date}", anchor=W,
                               font=("Arial", 8), bg="#D3D3D3")
            date_label.place(x=158 + (columns * 425), y=(rows * 120) + 72, width=231, height=13)
            list_of_objects.append(date_label)

            message_button = Button(main_page, text="Wiadomość", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                    command=lambda announcement=announcement_object:
                                    init_message_window(announcement))
            message_button.place(x=275 + (columns * 425), y=(rows * 120) + 87, width=115, height=22)
            list_of_objects.append(message_button)

            like_button = Button(main_page, text="Lubię to", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                 command=lambda announcement=announcement_object:
                                 My_functions.add_announcement_to_favorite(announcement))
            like_button.place(x=158 + (columns * 425), y=(rows * 120) + 87, width=115, height=22)
            list_of_objects.append(like_button)

            rows += 1
            if rows == 5:
                rows = 0
                columns += 1
                if rows == 0 and columns == 3:
                    break

        My_functions.config_buttons(actual_page, button_previous, button_next, announcements,
                                    config_page_of_announcements, list_of_objects, 15)

    button_previous, button_next = My_functions.create_buttons(main_page, 15, 1200)
    config_page_of_announcements(first_init=True)

    Config_data.current_page = main_page


def init_announcement_page_frame(page, announcement_object, block_fav, block_mess):
    tmp_page = Frame(page, bg="#A9A9A9", width=1276, height=636)
    tmp_page.pack()

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

    description_text = Text(tmp_page, width=45, height=18, font=("Arial", 14), borderwidth=0)
    description_text.insert(INSERT, f"{announcement_object.description}")
    description_text.place(x=740, y=180)
    description_text["state"] = "disabled"

    button_mobile_phone = Button(tmp_page, text="Zadzwoń", font=("Arial", 12), borderwidth=0, bg="#D3D3D3", width=15,
                                 command=lambda: button_mobile_phone.config(text=announcement_object.mobile_number,
                                                                            state="disabled"))
    button_mobile_phone["state"] = "disabled" if not announcement_object.mobile_number or block_mess else "normal"
    button_mobile_phone.place(x=740, y=594)

    button_mess = Button(tmp_page, text="Wyślij wiadomość", font=("Arial", 12), borderwidth=0, bg="#D3D3D3", width=15,
                         command=lambda: init_message_window(announcement_object))
    button_mess.place(x=888, y=594)
    button_mess["state"] = "disabled" if block_mess else "normal"
    button_fav = Button(tmp_page, text="Lubię to", font=("Arial", 12), borderwidth=0, bg="#D3D3D3", width=10,
                        command=lambda: My_functions.add_announcement_to_favorite(announcement_object))
    button_fav.place(x=1037, y=594)
    button_fav["state"] = "disabled" if block_fav else "normal"
    Button(tmp_page, text="Wróć", font=("Arial", 12), borderwidth=0, bg="#D3D3D3", width=10,
           command=lambda: tmp_page.destroy()).place(x=1141, y=594)

    photo_label = Label(tmp_page, text="Brak zdjęć do ogłoszenia.", font=("Arial", 12), borderwidth=3, bg="#D3D3D3")
    photo_label.place(x=20, y=112, width=700, height=466)
    photos, error_with_getting_photos = My_functions.download_photos_to_announcement(
        announcement_object.announcement_id, False, 600, 400)

    def init_photo(actual_photo=0):
        if 0 <= actual_photo < len(photos):
            photo_label.config(image=photos[actual_photo])
            button_previous.config(command=lambda: init_photo(actual_photo-1))
            button_next.config(command=lambda: init_photo(actual_photo+1))

    if len(photos) > 0:
        button_previous = Button(tmp_page, image=Config_data.images["arrows"][0], borderwidth=0, bg="#D3D3D3")
        button_previous.place(x=20, y=325, width=50, height=50)
        button_next = Button(tmp_page, image=Config_data.images["arrows"][1], borderwidth=0, bg="#D3D3D3")
        button_next.place(x=670, y=325, width=50, height=50)
        init_photo()


def init_messages_page_frame(root):
    if Config_data.is_user_logged_in:
        Config_data.current_page.destroy()

        messages_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                              highlightthickness=2)
        messages_page.pack()

        ttk.Separator(messages_page).place(x=40, y=85, width=240)
        ttk.Separator(messages_page).place(x=360, y=85, width=240)

        ttk.Separator(messages_page).place(x=320, y=15, height=600)
        ttk.Separator(messages_page).place(x=640, y=15, height=600)

        Label(messages_page, text="Kupujesz", font=("Arial", 27), bg="#A9A9A9").place(x=85, y=30)
        Label(messages_page, text="Sprzedajesz", font=("Arial", 27), bg="#A9A9A9").place(x=378, y=30)

        def config_conversations_page_as_customer(actual_page=1, list_of_objects=None):
            conversations_as_customer = My_functions.download_conversations(1, actual_page)

            if list_of_objects:

                for element in list_of_objects:
                    element.destroy()

            list_of_objects = []

            rows = 0
            for customer_conversation_object in conversations_as_customer:
                title_button = Button(messages_page, text=customer_conversation_object.title, bg="#D3D3D3",
                                      font=("Arial", 10), anchor=W, borderwidth=1,
                                      command=lambda conversation_object=customer_conversation_object:
                                      update_text_of_messages(conversation_object, True))
                title_button.place(x=15, y=(rows * 75) + 100, width=300, height=22)
                list_of_objects.append(title_button)

                id_label = Label(messages_page, text=f"ID: {customer_conversation_object.announcement_id}", anchor=E,
                                 bg="#D3D3D3", font=("Arial", 9))
                id_label.place(x=244, y=(rows * 75) + 123, width=70, height=15)
                list_of_objects.append(id_label)

                name_label = Label(messages_page, text=f"Sprzedający: {customer_conversation_object.first_name}",
                                   anchor=W, bg="#D3D3D3", font=("Arial", 9))
                name_label.place(x=15, y=(rows * 75) + 123, width=227, height=15)
                list_of_objects.append(name_label)

                rows += 1
                if rows == 7:
                    break

            My_functions.config_buttons(actual_page, button_previous_customer, button_next_customer,
                                        conversations_as_customer, config_conversations_page_as_customer,
                                        list_of_objects, 7)

        def config_conversations_page_as_seller(actual_page=1, list_of_objects=None):
            conversations_as_seller = My_functions.download_conversations(0, actual_page)

            if list_of_objects:

                for element in list_of_objects:
                    element.destroy()

            list_of_objects = []

            rows = 0
            for seller_conversation_object in conversations_as_seller:
                title_button = Button(messages_page, text=seller_conversation_object.title, bg="#D3D3D3",
                                      font=("Arial", 10), anchor=W, borderwidth=1,
                                      command=lambda conversation_object=seller_conversation_object:
                                      update_text_of_messages(conversation_object, False))
                title_button.place(x=335, y=(rows * 75) + 100, width=300, height=22)
                list_of_objects.append(title_button)

                id_label = Label(messages_page, text=f"ID: {seller_conversation_object.announcement_id}", anchor=E,
                                 bg="#D3D3D3", font=("Arial", 9))
                id_label.place(x=564, y=(rows * 75) + 123, width=70, height=15)
                list_of_objects.append(id_label)

                name_label = Label(messages_page, text=f"Kupujący: {seller_conversation_object.first_name}", anchor=W,
                                   bg="#D3D3D3", font=("Arial", 9))
                name_label.place(x=335, y=(rows * 75) + 123, width=227, height=15)
                list_of_objects.append(name_label)

                rows += 1
                if rows == 7:
                    break

            My_functions.config_buttons(actual_page, button_previous_seller, button_next_seller,
                                        conversations_as_seller, config_conversations_page_as_seller,
                                        list_of_objects, 7)

        button_previous_customer, button_next_customer = My_functions.create_buttons(messages_page, 15, 254)
        button_previous_seller, button_next_seller = My_functions.create_buttons(messages_page, 335, 574)
        config_conversations_page_as_customer()
        config_conversations_page_as_seller()

        choose_conversation_label = Label(messages_page, bg="#A9A9A9", font=("Arial", 20),
                                          text=f"Wybierz konwersacje, {Config_data.logged_in_user_info.first_name}")
        choose_conversation_label.place(x=750, y=250)

        def update_text_of_messages(conversation_object, is_user_customer):
            # nie niszczyc ciagle tego labela
            choose_conversation_label.destroy()
            # nie nadklejac textu na text
            text = Text(messages_page, width=67, height=30, bg="#D3D3D3", borderwidth=0, font=("Arial", 12))
            text.place(x=650, y=50)
            # nie naklejac scrola na scroll
            scrollbar = Scrollbar(messages_page, command=text.yview)
            scrollbar.place(x=1258, y=50, height=577)

            text["yscrollcommand"] = scrollbar.set
            text.bind("<Configure>", My_functions.set_right)

            person = "Sprzedający" if is_user_customer else "Kupujący"
            # nie naklejac lebali na siebie
            Label(messages_page, text=conversation_object.title, anchor=W,
                  font=("Arial", 16), bg="red").place(x=650, y=15, width=370)
            Label(messages_page, text=f"{person}: {conversation_object.first_name}", anchor=E,
                  font=("Arial", 16), bg="red").place(x=1025, y=15, width=250)
            # nie naklejac entry na entry
            message_entry = Entry(messages_page, width=41, font=("Arial", 16))
            message_entry.place(x=650, y=600)
            message_entry.insert(0, "Napisz wiadomość...")
            message_entry.bind("<Button-1>", lambda event: My_functions.delete_text(message_entry))

            def refresh_messages():
                list_of_message_objects = My_functions.download_messages(conversation_object=conversation_object)

                text["state"] = "normal"
                text.delete("1.0", END)

                i = 1
                for message in list_of_message_objects:
                    position = f"{i}.0"
                    if message.customer_flag == 1:
                        text.insert(position, f"{message.first_name}\n{message.post_date}\n{message.content}\n\n")
                    else:
                        text.insert(position, f"\t{message.first_name}\n\t{message.post_date}"
                                              f"\n\t{message.content}\n\n")
                    i += 4

                text["state"] = "disabled"
                # zmienic ten button aby sie nie inicjalizował cały czas nowy
                Button(messages_page, text="Wyślij", width=11, borderwidth=1, font=("Arial", 11),
                       command=lambda: My_functions.send_message(list_of_message_objects, message_entry,
                                                                 refresh_messages,
                                                                 is_user_customer)).place(x=1150, y=600)
            refresh_messages()

        Config_data.current_page = messages_page
    else:
        messagebox.showwarning("Nie jesteś zalogowany.", "Aby zobaczyć wiadomości musisz sie zalogować.")


def init_favorite_page_frame(root):
    if Config_data.is_user_logged_in:
        Config_data.current_page.destroy()
        favorite_page = Frame(root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                              highlightthickness=2)
        favorite_page.pack()

        ttk.Separator(favorite_page).place(x=427, y=15, height=600)
        ttk.Separator(favorite_page).place(x=854, y=15, height=600)

        ttk.Separator(favorite_page).place(x=40, y=85, width=350)
        ttk.Separator(favorite_page).place(x=890, y=85, width=350)
        Label(favorite_page, text="Ulubione", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=145, y=30)
        Label(favorite_page, text="Zakończone", font=("Arial", 27), borderwidth=0, bg="#A9A9A9").place(x=970, y=30)

        def config_page_of_fav_active_announcements(actual_page=1, list_of_objects=None):
            user_fav_active_announcements = My_functions.download_user_favorite_announcements(1, actual_page,
                                                                                              8)

            if list_of_objects:

                for element in list_of_objects:
                    element.destroy()

            list_of_objects = []

            columns = 0
            rows = 0
            # Init user fav active announcements
            for user_fav_active_announcement_object in user_fav_active_announcements:
                photo_label = Label(favorite_page, bg="#D3D3D3", image=user_fav_active_announcement_object.
                                    main_photo)
                photo_label.place(x=40 + (columns * 425), y=(rows * 120) + 162, width=115, height=67)
                list_of_objects.append(photo_label)

                title_button = Button(favorite_page, text=user_fav_active_announcement_object.title, anchor=W,
                                      font=("Arial", 10), bg="#D3D3D3", borderwidth=1,
                                      command=lambda announcement_object=user_fav_active_announcement_object:
                                      init_announcement_page_frame(favorite_page, announcement_object, True,
                                                                   False))
                title_button.place(x=40 + (columns * 425), y=(rows * 120) + 138, width=350, height=22)
                list_of_objects.append(title_button)

                category_label = Label(favorite_page, text=user_fav_active_announcement_object.name_category,
                                       anchor=W, font=("Arial", 8), bg="#D3D3D3")
                category_label.place(x=158 + (columns * 425), y=(rows * 120) + 162, width=114, height=13)
                list_of_objects.append(category_label)

                location_label = Label(favorite_page, text=user_fav_active_announcement_object.location, anchor=W,
                                       font=("Arial", 8), bg="#D3D3D3")
                location_label.place(x=158 + (columns * 425), y=(rows * 120) + 177, width=114, height=13)
                list_of_objects.append(location_label)

                price_label = Label(favorite_page, text=f"{user_fav_active_announcement_object.price} ZŁ", anchor=E,
                                    font=("Arial", 10), bg="#D3D3D3")
                price_label.place(x=275 + (columns * 425), y=(rows * 120) + 162, width=114, height=13)
                list_of_objects.append(price_label)

                state_label = Label(favorite_page, text=user_fav_active_announcement_object.state, anchor=E,
                                    font=("Arial", 8), bg="#D3D3D3")
                state_label.place(x=275 + (columns * 425), y=(rows * 120) + 177, width=114, height=13)
                list_of_objects.append(state_label)

                date_label = Label(favorite_page, text=f"Dodano: {user_fav_active_announcement_object.creation_date}",
                                   anchor=W, font=("Arial", 8), bg="#D3D3D3")
                date_label.place(x=158 + (columns * 425), y=(rows * 120) + 192, width=231, height=13)
                list_of_objects.append(date_label)

                message_button = Button(favorite_page, text="Wiadomość", font=("Arial", 8), borderwidth=1,
                                        bg="#D3D3D3",
                                        command=lambda announcement_object=user_fav_active_announcement_object:
                                        init_message_window(announcement_object))
                message_button.place(x=275 + (columns * 425), y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(message_button)

                unlike_button = Button(favorite_page, text="Nie lubię", font=("Arial", 8), borderwidth=1,
                                       bg="#D3D3D3",
                                       command=lambda announcement_object=user_fav_active_announcement_object:
                                       My_functions.delete_announcement_from_favorite(announcement_object,
                                                                                      init_favorite_page_frame,
                                                                                      root))
                unlike_button.place(x=158 + (columns * 425), y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(unlike_button)

                rows += 1
                if rows == 4:
                    rows = 0
                    columns += 1
                    if rows == 0 and columns == 2:
                        break

            My_functions.config_buttons(actual_page, button_previous_active, button_next_active,
                                        user_fav_active_announcements, config_page_of_fav_active_announcements,
                                        list_of_objects, 8)

        def config_page_of_fav_completed_announcements(actual_page=1, list_of_objects=None):
            user_fav_completed_announcements = My_functions.download_user_favorite_announcements(0,
                                                                                                 actual_page, 4)

            if list_of_objects:

                for element in list_of_objects:
                    element.destroy()

            list_of_objects = []

            rows = 0
            # Init user fav completed announcements
            for user_fav_completed_announcement_object in user_fav_completed_announcements:
                photo_label = Label(favorite_page, bg="#D3D3D3",
                                    image=user_fav_completed_announcement_object.main_photo)
                photo_label.place(x=890, y=(rows * 120) + 162, width=115, height=67)
                list_of_objects.append(photo_label)

                title_button = Button(favorite_page, text=user_fav_completed_announcement_object.title, anchor=W,
                                      font=("Arial", 10), bg="#D3D3D3", borderwidth=1,
                                      command=lambda announcement_object=user_fav_completed_announcement_object:
                                      init_announcement_page_frame(favorite_page, announcement_object, True,
                                                                   False))
                title_button.place(x=890, y=(rows * 120) + 138, width=350, height=22)
                list_of_objects.append(title_button)

                category_label = Label(favorite_page, text=user_fav_completed_announcement_object.name_category,
                                       anchor=W, font=("Arial", 8), bg="#D3D3D3")
                category_label.place(x=1008, y=(rows * 120) + 162, width=114, height=13)
                list_of_objects.append(category_label)

                location_label = Label(favorite_page, text=user_fav_completed_announcement_object.location,
                                       anchor=W, font=("Arial", 8), bg="#D3D3D3")
                location_label.place(x=1008, y=(rows * 120) + 177, width=114, height=13)
                list_of_objects.append(location_label)

                price_label = Label(favorite_page, text=f"{user_fav_completed_announcement_object.price} ZŁ",
                                    anchor=E, font=("Arial", 10), bg="#D3D3D3")
                price_label.place(x=1125, y=(rows * 120) + 162, width=114, height=13)
                list_of_objects.append(price_label)

                state_label = Label(favorite_page, text=user_fav_completed_announcement_object.state, anchor=E,
                                    font=("Arial", 8), bg="#D3D3D3")
                state_label.place(x=1125, y=(rows * 120) + 177, width=114, height=13)
                list_of_objects.append(state_label)

                date_label = Label(favorite_page,
                                   text=f"Dodano: {user_fav_completed_announcement_object.creation_date}", anchor=W,
                                   font=("Arial", 8), bg="#D3D3D3")
                date_label.place(x=1008, y=(rows * 120) + 192, width=231, height=13)
                list_of_objects.append(date_label)

                message_button = Button(favorite_page, text="Wiadomość", font=("Arial", 8), borderwidth=1,
                                        bg="#D3D3D3",
                                        command=lambda announcement_object=user_fav_completed_announcement_object:
                                        init_message_window(announcement_object))
                message_button.place(x=1125, y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(message_button)

                delete_button = Button(favorite_page, text="Usuń", font=("Arial", 8), borderwidth=1, bg="#D3D3D3",
                                       command=lambda announcement_object=user_fav_completed_announcement_object:
                                       My_functions.delete_announcement_from_favorite(announcement_object,
                                                                                      init_favorite_page_frame,
                                                                                      root))
                delete_button.place(x=1008, y=(rows * 120) + 207, width=115, height=22)
                list_of_objects.append(delete_button)

                rows += 1
                if rows == 4:
                    break

            My_functions.config_buttons(actual_page, button_previous_completed, button_next_completed,
                                        user_fav_completed_announcements, config_page_of_fav_completed_announcements,
                                        list_of_objects, 4)

        button_previous_active, button_next_active = My_functions.create_buttons(favorite_page, 15, 785)
        button_previous_completed, button_next_completed = My_functions.create_buttons(favorite_page, 865, 1200)
        config_page_of_fav_active_announcements()
        config_page_of_fav_completed_announcements()

        Config_data.current_page = favorite_page

    else:
        messagebox.showwarning("Nie jesteś zalogowany.",
                               "Aby zobaczyć ulubione ogłoszenia musisz sie zalogować.")


def init_message_window(announcement_object):
    if Config_data.is_user_logged_in:
        message_window = Toplevel()
        Config_data.list_of_active_windows.append(message_window)
        message_window_width = 477
        message_window_height = 484
        screen_width = message_window.winfo_screenwidth()
        screen_height = message_window.winfo_screenheight()
        center_x = int(screen_width / 2 - message_window_width / 2)
        center_y = int(screen_height / 2 - message_window_height / 2)
        message_window.geometry(f"{message_window_width}x{message_window_height}+{center_x}+{center_y}")
        message_window.title(announcement_object.first_name)
        message_window.resizable(width=True, height=True)
        message_window.config(bg="#B0C4DE")
        message_window.wm_iconphoto(False, PhotoImage(file="Photos/messages_icon.png"))

        Label(message_window, width=68, height=1, text=announcement_object.title, anchor=W).pack()
        Label(message_window, width=68, height=1, text=f"Cena: {announcement_object.price} ZŁ", anchor=W).pack()
        Label(message_window, width=80, height=1, text=f"ID: {announcement_object.announcement_id}", anchor=W,
              font=("Arial", 8)).pack()

        def set_right(event):
            event.widget.configure(tabs=(event.width - 6, "right"))

        text = Text(message_window, width=57, height=26, bg="#D3D3D3")
        text.pack(side=LEFT)

        scrollbar = Scrollbar(message_window, command=text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        text["yscrollcommand"] = scrollbar.set
        text.bind("<Configure>", set_right)

        message_entry = Entry(message_window, width=35, font=("Arial", 14))
        message_entry.place(x=0, y=457)
        message_entry.insert(0, "Napisz wiadomość...")
        message_entry.bind("<Button-1>", lambda event: My_functions.delete_text(message_entry))

        def refresh_messages():
            list_of_message_objects = My_functions.download_messages(announcement_object=announcement_object)
            text["state"] = "normal"
            text.delete("1.0", END)

            i = 1
            for message in list_of_message_objects:
                position = f"{i}.0"
                if message.customer_flag == 1:
                    text.insert(position, f"{message.first_name}\n{message.post_date}\n{message.content}\n\n")
                else:
                    text.insert(position, f"\t{message.first_name}\n\t{message.post_date}"
                                          f"\n\t{message.content}\n\n")
                i += 4

            text["state"] = "disabled"

            Button(message_window, text="Wyślij", width=9, borderwidth=1,
                   command=lambda: My_functions.send_message(list_of_message_objects, message_entry, refresh_messages,
                                                             True, announcement_object)).place(x=389, y=457)

        refresh_messages()

    else:
        messagebox.showwarning("Nie jesteś zalogowany.", f"Aby wysłać wiadomość do użytkownika"
                                                         f" {announcement_object.first_name}, musisz sie zalogować.")
