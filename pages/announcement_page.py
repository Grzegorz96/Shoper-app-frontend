import config_data
import functions
from tkinter import *
from tkinter import ttk
from windows.message_window import init_message_window


def init_announcement_page_frame(page, announcement_object, block_fav, block_mess):
    """The function initializing the announcement page, displays all data for a given announcement. It also downloads
    photos and displays them in the gallery. From this page, the user can like the announcement, send a message
    or unlock the seller's mobile number."""
    # Initialization of the local tmp_page, this object will not be assigned to the config_data.current_page because it
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
                        command=lambda: functions.add_announcement_to_favorite(announcement_object))
    button_fav.place(x=1037, y=594)
    button_fav["state"] = "disabled" if block_fav else "normal"

    # Init photo_label for displaying photos of announcement.
    photo_label = Label(tmp_page, text="Brak zdjęć do ogłoszenia.", font=("Arial", 12), borderwidth=3, bg="#D3D3D3")
    photo_label.place(x=20, y=112, width=700, height=466)

    # Init button_back for destroying tmp_page and returning to previous page.
    Button(tmp_page, text="Wróć", font=("Arial", 12), borderwidth=0, bg="#D3D3D3", width=10,
           command=lambda: tmp_page.destroy()).place(x=1141, y=594)

    # Downloading list of photos to announcement.
    photos, error_with_getting_photos = functions.download_photos_to_announcement(
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
        button_previous = Button(tmp_page, text="prev", image=config_data.images["arrows"][0], borderwidth=0,
                                 bg="#D3D3D3")
        button_previous.place(x=20, y=325, width=50, height=50)
        button_next = Button(tmp_page, text="next", image=config_data.images["arrows"][1], borderwidth=0, bg="#D3D3D3")
        button_next.place(x=670, y=325, width=50, height=50)
        init_photo()