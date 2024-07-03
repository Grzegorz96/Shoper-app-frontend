from tkinter import *
from tkinter import ttk
from utils.helpers import delete_text
from utils import config_data, constants
from windows.login_register_window import init_login_register_window
from pages.home_page import init_shoper_page_frame
from pages.add_announcement_page import init_add_announcement_page_frame
from pages.user_page import init_user_page_frame
from pages.favorite_page import init_favorite_page_frame
from pages.messages_page import init_messages_page_frame


def is_user_logged_to_user_page(top_panel_frame):
    """The function to check if the user is logged in, if logged in, I call the init_user_page_frame function,
    if not already logged in, it calls the init_login_window function so that the user can log in."""
    if config_data.is_user_logged_in:
        init_user_page_frame()
    else:
        init_login_register_window(top_panel_frame)


def init_top_panel():
    """The function initializing the top panel of the application is called once from main.py and attaches the top
    panel objects to the main application window, which are later used by the user to initialize subsequent pages."""
    # Init top_panel_frame for root.
    top_panel_frame = Frame(config_data.root, width=1280, height=80)
    top_panel_frame.pack()

    # Init SHOPER_button for top_panel_frame.
    Button(top_panel_frame, text="SHOPER", width=30, height=2, borderwidth=0, bg="#D3D3D3",
           command=lambda: init_shoper_page_frame()).place(x=20, y=20)

    # Init search_engine for top_panel_frame.
    search_engine = Entry(top_panel_frame, font=("Arial", 11), width=36, borderwidth=0, bg="#D3D3D3")
    search_engine.place(x=280, y=10)
    search_engine.insert(0, "Czego szukasz ?")
    search_engine.bind("<Button-1>", lambda event: delete_text(search_engine))

    # Init search_location for top_panel_frame.
    Label(top_panel_frame, text="Wpisz lokalizacje").place(x=580, y=30)
    search_location = Entry(top_panel_frame, font=("Arial", 11), width=36, borderwidth=0, bg="#D3D3D3")
    search_location.place(x=280, y=30)

    # Init categories for top_panel_frame.
    Label(top_panel_frame, text="Wybierz kategorie").place(x=580, y=50)
    style = ttk.Style()
    style.theme_use('clam')
    style.map(
        "TCombobox",
        fieldbackground=[("readonly", "#D3D3D3")],
        selectbackground=[("readonly", "#D3D3D3")],
        selectforeground=[("readonly", "black")]
    )

    current_var_category = StringVar()
    ttk.Combobox(top_panel_frame, textvariable=current_var_category, width=45, values=constants.categories,
                 state="readonly").place(x=280, y=50)

    Button(top_panel_frame, text="X",  borderwidth=0, bg="#D3D3D3", command=lambda: current_var_category.set("")).place(
        x=536, y=51, height=19, width=20)

    # Init search_button for top_panel_frame.
    Button(top_panel_frame, text="Wyszukaj produkt", borderwidth=0, bg="#D3D3D3",
           command=lambda: init_shoper_page_frame(search_engine, search_location, current_var_category)).place(x=580,
                                                                                                               y=6)
    search_engine.bind("<Return>", lambda event: init_shoper_page_frame(search_engine, search_location,
                                                                        current_var_category))

    # Init favorite_button for top_panel_frame.
    Button(top_panel_frame, text="Ulubione", width=16, height=2, borderwidth=0, bg="#D3D3D3",
           command=lambda: init_favorite_page_frame()).place(x=730, y=20)

    # Init messages_button for top_panel_frame.
    Button(top_panel_frame, text="Wiadomości", width=16, height=2, borderwidth=0, bg="#D3D3D3",
           command=lambda: init_messages_page_frame()).place(x=865, y=20)

    # Init add_announcement button for top_panel_frame.
    Button(top_panel_frame, text="Dodaj ogłoszenie", width=16, height=2, borderwidth=0,
           bg="#D3D3D3", command=lambda: init_add_announcement_page_frame()).place(x=1000, y=20)

    # Init account_button for top_panel_frame.
    Button(top_panel_frame, text="Twoje konto", width=16, height=2, borderwidth=0, bg="#D3D3D3",
           command=lambda: is_user_logged_to_user_page(top_panel_frame)).place(x=1135, y=20)
