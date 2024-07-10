from tkinter import END, Button, Label, W, E
from utils import config_data
from PIL import Image, ImageTk


def set_right(event):
    """A function that configures the text in the Text object so that it can be displayed on the right."""
    event.widget.configure(tabs=(event.width - 6, "right"))


def delete_text(entry_object):
    """A function that removes text from the entry object and unbinds the function from the object."""
    entry_object.delete(0, END)
    entry_object.unbind("<Button-1>")


def config_buttons(actual_page, button_previous, button_next, collection, function, list_of_objects, objects_on_page):
    """The function responsible for configuring buttons for switching pages in the program."""
    # If the imported page number is greater than 1, the program updates the page back function.
    if 1 < actual_page:
        button_previous.config(command=lambda: function(actual_page - 1, list_of_objects))
    # Otherwise, it will update the button functions by assigning None.
    else:
        button_previous.config(command=lambda: None)

    # If the length of the retrieved object collection is equal to the number of objects displayed on the page,
    # the program updates the next page function.
    if len(collection) == objects_on_page:
        button_next.config(command=lambda: function(actual_page + 1, list_of_objects))
    # Otherwise, it will update the button functions by assigning None.
    else:
        button_next.config(command=lambda: None)


def create_buttons(page, x1, x2):
    """The function responsible for creating page change button objects for given page objects and returning them to
    the function."""
    # Creating buttons for a specific page and a specific x value.
    button_previous = Button(page, image=config_data.images["arrows"][2], text="Poprzednia", font=("Arial", 8),
                             borderwidth=0, bg="#A9A9A9")

    button_previous.place(x=x1, y=600, width=60)
    button_next = Button(page, image=config_data.images["arrows"][3], text="Następna", font=("Arial", 8),
                         borderwidth=0, bg="#A9A9A9")
    button_next.place(x=x2, y=600, width=60)

    # Returning button objects.
    return button_previous, button_next


def create_labels(page, announcement_object, x1, x2, x3, y1, y2, y3, list_of_objects):
    """Function responsible for the initialization of label objects on switched announcement pages. It accepts the
    position parameters of the created objects, the announcement object, the page object and the list of objects to be
    deleted."""
    # Init photo_label and adding it to the list of objects.
    photo_label = Label(page, bg="#D3D3D3", image=announcement_object.main_photo)
    photo_label.place(x=x1, y=y1, width=115, height=67)
    list_of_objects.append(photo_label)

    # Init category_label and adding it to the list of objects.
    category_label = Label(page, text=announcement_object.name_category, anchor=W, font=("Arial", 8), bg="#D3D3D3")
    category_label.place(x=x2, y=y1, width=114, height=13)
    list_of_objects.append(category_label)

    # Init location_label and adding it to the list of objects.
    location_label = Label(page, text=announcement_object.location, anchor=W, font=("Arial", 8), bg="#D3D3D3")
    location_label.place(x=x2, y=y2, width=114, height=13)
    list_of_objects.append(location_label)

    # Init price_label and adding it to the list of objects.
    price_label = Label(page, text=f"{announcement_object.price} ZŁ", anchor=E, font=("Arial", 10), bg="#D3D3D3")
    price_label.place(x=x3, y=y1, width=114, height=13)
    list_of_objects.append(price_label)

    # Init state_label and adding it to the list of objects.
    state_label = Label(page, text=announcement_object.state, anchor=E, font=("Arial", 8), bg="#D3D3D3")
    state_label.place(x=x3, y=y2, width=114, height=13)
    list_of_objects.append(state_label)

    # Init date_label and adding it to the list of objects.
    date_label = Label(page, text=f"Dodano: {announcement_object.creation_date}", anchor=W, font=("Arial", 8),
                       bg="#D3D3D3")
    date_label.place(x=x2, y=y3, width=231, height=13)
    list_of_objects.append(date_label)


def loading_images():
    """The function is launched when the program starts from the main.py module. The function is responsible for loading
    static graphic files and assigning them to the global dictionary."""
    # The program tries to load photos from your computer.
    try:
        config_data.images["arrows"] = [ImageTk.PhotoImage(Image.open(
                                            "./assets/images/image_left.png").resize((50, 50))),
                                        ImageTk.PhotoImage(Image.open(
                                            "./assets/images/image_right.png").resize((50, 50))),
                                        ImageTk.PhotoImage(Image.open(
                                            "./assets/images/announcement_left.png").resize((40, 30))),
                                        ImageTk.PhotoImage(Image.open(
                                            "./assets/images/announcement_right.png").resize((40, 30)))]
    # If an error occurs while loading, the program will assign the value None to the dictionary keys.
    except FileNotFoundError:
        config_data.images["arrows"] = [None, None, None, None]

    try:
        config_data.images["eyes"] = [ImageTk.PhotoImage(Image.open("./assets/images/eye.png").resize((16, 16))),
                                      ImageTk.PhotoImage(Image.open("./assets/images/hidden.png").resize((16, 16)))]

    except FileNotFoundError:
        config_data.images["eyes"] = [None, None]

    try:
        config_data.images["camera_icon"] = ImageTk.PhotoImage(Image.open(
            "./assets/images/camera_icon.png").resize((50, 50)))
    except FileNotFoundError:
        config_data.images["camera_icon"] = None

    try:
        config_data.images["close"] = ImageTk.PhotoImage(Image.open(
            "./assets/images/close.png").resize((10, 10)))
    except FileNotFoundError:
        config_data.images["close"] = None

    try:
        config_data.images["logout"] = ImageTk.PhotoImage(Image.open(
            "./assets/images/logout.png").resize((20, 16)))
    except FileNotFoundError:
        config_data.images["logout"] = None

    try:
        config_data.images["logo"] = ImageTk.PhotoImage(Image.open(
            "./assets/images/shoper_logo.png").resize((220, 60)))
    except FileNotFoundError:
        config_data.images["logo"] = None

    try:
        config_data.images["delete"] = ImageTk.PhotoImage(Image.open(
            "./assets/images/delete.png").resize((20, 20)))
    except FileNotFoundError:
        config_data.images["delete"] = None


def toggle_password(entry_password, toggle_button, password_label=None):
    """The function responsible for changing the visibility of the password in the entry object."""
    if entry_password.cget('show') == '*':
        entry_password.config(show='')
        toggle_button.config(image=config_data.images["eyes"][0])
        if password_label:
            password_label.config(text=f"Hasło: {config_data.logged_in_user_info.password}")

    else:
        entry_password.config(show='*')
        toggle_button.config(image=config_data.images["eyes"][1])
        if password_label:
            password_label.config(text=f"Hasło: {'*' * len(config_data.logged_in_user_info.password)}")
