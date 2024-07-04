from utils import config_data, constants
from tkinter import Frame, Label, Entry, Button, Text, StringVar, INSERT, W, ttk
from models.photo_button import PhotoButton
from logic.announcements.user_management.update_announcement import update_announcement
from logic.media.get_images_to_announcement import get_images_to_announcement
from logic.media.select_image import select_image
from logic.media.delete_image import delete_image
from logic.media.set_main_image import set_main_image


def init_edit_user_announcement_page_frame(announcement_object, init_user_page_frame):
    """The function initializing the page for editing the announcement by the user. The user can update the data for
    the announcement, remove the photo, add a photo or Modify the main photo."""
    # Destroying the current page.
    config_data.current_page.destroy()
    # Init edit_user_announcement_page for root.
    edit_user_announcement_page = Frame(config_data.root, bg="#A9A9A9", width=1280, height=640,
                                        highlightbackground="black", highlightthickness=2)
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
    ttk.Combobox(edit_user_announcement_page, textvariable=current_var_state, font=("Arial", 13), state="readonly",
                 values=constants.states).place(x=560, y=40, width=170)
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
        photo_button = Button(edit_user_announcement_page, bg="#D3D3D3", image=config_data.images["camera_icon"],
                              state="disabled", borderwidth=0)
        photo_button.place(x=40 + (columns * 175), y=250 + (rows * 100), width=115, height=75)
        photo_button_object = PhotoButton(photo_button, None, None, 40 + (columns * 175),
                                          250 + (rows * 100), False, None, False,
                                          False)

        list_of_photo_button_objects.append(photo_button_object)
        # Inserting the main photo selection function into the photo button.
        photo_button.config(command=lambda selected_button_object=photo_button_object: set_main_image(
            selected_button_object, list_of_photo_button_objects))

        rows += 1
        if rows == 3:
            rows = 0
            columns += 1

    # Downloading photos for the announcement and information about whether there was any error with downloading the
    # photos.
    photos_to_edit, error_with_getting_photos = get_images_to_announcement(announcement_object.announcement_id, True,
                                                                           115, 75)
    # Declaring a list of photos to be removed from the server.
    deleted_photos = []

    # Depending on what values are in the downloaded photos_to_edit, the program modifies the objects in the
    # list_of_photo_button_objects in an appropriate way.
    # If there was no error with downloading photos, it assigns data from downloaded photos to PhotoButton objects.
    if not error_with_getting_photos:
        for index, (photo, filename, is_main_photo) in enumerate(photos_to_edit):
            list_of_photo_button_objects[index].button.config(state="normal", image=photo)
            list_of_photo_button_objects[index].photo_to_display = photo
            list_of_photo_button_objects[index].photo_to_upload = filename
            if is_main_photo:
                list_of_photo_button_objects[index].button.config(borderwidth=4)
                list_of_photo_button_objects[index].photo_from_main = True
                list_of_photo_button_objects[index].main_photo = True
            else:
                list_of_photo_button_objects[index].photo_from_media = True

            # Creating a delete photo button for the downloaded photo and assigning it to the PhotoButton object field.
            delete_button = Button(edit_user_announcement_page, text="Usuń zdjęcie", font=("Arial", 8), borderwidth=0,
                                   bg="#D3D3D3", command=lambda button_object=list_of_photo_button_objects[index]:
                                   delete_image(button_object, deleted_photos))
            delete_button.place(x=list_of_photo_button_objects[index].position_x + 25,
                                y=list_of_photo_button_objects[index].position_y + 75)

            list_of_photo_button_objects[index].button_delete = delete_button

    Label(edit_user_announcement_page, text="Naciśnij na obraz, aby wybrać zdjęcie główne."
                                            " W razie niewybrania, pierwsze zdjęcie będzie zdjęciem głównym.",
          bg="#D3D3D3", font=("Arial", 7), anchor=W).place(x=40, y=228, width=465)

    # Init add_photo_button for edited announcement.
    add_photo_button = Button(edit_user_announcement_page, bg="#D3D3D3", text="Dodaj zdjęcie", font=("Arial", 10),
                              command=lambda: select_image(list_of_photo_button_objects, edit_user_announcement_page))
    add_photo_button.place(x=390, y=450, width=115, height=75)
    # If was error_with_getting_photos, add_photo_button will be disabled.
    if error_with_getting_photos:
        add_photo_button.config(text="Brak możliwości\ndodania zdjęcia", state="disabled")

    # Init change_announcement_button for edit_user_announcement_page.
    Button(edit_user_announcement_page, bg="#00BFFF", text="Zmień ogłoszenie!", borderwidth=0, font=("Arial", 15),
           command=lambda: update_announcement(title_entry, location_entry, price_entry, description_text,
                                               announcement_object, init_user_page_frame, current_var_state,
                                               mobile_number_entry, list_of_photo_button_objects,
                                               deleted_photos)).place(x=40, y=550, width=465, height=50)

    # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
    config_data.current_page = edit_user_announcement_page
