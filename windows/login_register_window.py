from tkinter import ttk
from tkinter import *
from utils import config_data, constants
from pages.home_page import init_shoper_page_frame
from logic.register.user_registration import register_user
from logic.login.user_login import login_user
from logic.register.user_validation import verify_login, verify_password, show_pattern


def init_login_register_window(top_panel_frame):
    """A function that initializes an additional window with a login and registration form. Using it,
    the user can log in or register a new account."""
    # Init login_window from Top_Level() Class.
    login_window = Toplevel()
    # Adding the created window object to the global list to be able to destroy the created objects at the right moment.
    config_data.list_of_active_windows.append(login_window)
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
    login_window.resizable(width=False, height=False)
    login_window.config(bg="#B0C4DE")

    try:
        login_window.wm_iconphoto(False, PhotoImage(file="./assets/images/login_icon.png"))
    except TclError:
        pass

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
           command=lambda: login_user(entry_login_or_email, entry_password, top_panel_frame,
                                      init_shoper_page_frame)).grid(row=3, column=1, ipadx=10, ipady=8, pady=(10, 0))

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
           command=lambda: verify_login(login_entry)).grid(row=10, column=0, sticky=E, pady=(0, 10), padx=(0, 8))

    # Init login_pattern_button for login_window_label.
    login_pattern = Button(login_window_label, text="Wzór loginu", borderwidth=0, bg="#D3D3D3",
                           command=lambda: show_pattern(login_pattern["text"]))
    login_pattern.grid(row=10, column=0, sticky=W, pady=(0, 10), padx=(26, 0))

    # Init password_entry for login_window_label.
    Label(login_window_label, text="Hasło*", font="Arial").grid(row=11, column=1)
    password_entry = Entry(login_window_label, font=("Arial", 12), borderwidth=0, bg="#D3D3D3")
    password_entry.grid(row=11, column=0, pady=(10, 4), ipadx=25, padx=(20, 0))

    # Init verify_password_button for login_window_label.
    Button(login_window_label, text="Zweryfikuj hasło", borderwidth=0, bg="#D3D3D3",
           command=lambda: verify_password(password_entry)).grid(row=12, column=0, sticky=E, pady=(0, 10), padx=(0, 8))

    # Init password_pattern_button for login_window_label.
    password_pattern = Button(login_window_label, text="Wzór hasła", borderwidth=0, bg="#D3D3D3",
                              command=lambda: show_pattern(password_pattern["text"]))
    password_pattern.grid(row=12, column=0, sticky=W, pady=(0, 10), padx=(26, 0))

    # Init combobox days for login_window_label.
    Label(login_window_label, text="Data urodzenia*", font="Arial").grid(row=13, column=1)
    current_var_day = StringVar()
    ttk.Combobox(login_window_label, textvariable=current_var_day, width=6, state="readonly",
                 values=constants.days).grid(row=13, column=0, sticky=W, pady=10, padx=(26, 0))

    # Init combobox months for login_window_label.
    current_var_month = StringVar()
    ttk.Combobox(login_window_label, textvariable=current_var_month, width=10, state="readonly",
                 values=constants.months).grid(row=13, column=0, padx=(20, 0))

    # Init combobox years for login_window_label.
    current_var_year = StringVar()
    ttk.Combobox(login_window_label, textvariable=current_var_year, width=6, state="readonly",
                 values=constants.years).grid(row=13, column=0, sticky=E, padx=(0, 7))

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
           command=lambda: register_user(first_name_entry, last_name_entry, email_entry, login_entry,
                                         password_entry, current_var_day, current_var_month, current_var_year,
                                         street_entry, zip_code_entry, city_entry)).grid(row=17, column=1, ipadx=10,
                                                                                         ipady=8, pady=10)

    Label(login_window_label, text="*Pole wymagane").grid(row=17, column=0, pady=(0, 10), sticky=SW)
