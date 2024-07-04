def set_main_image(selected_button_object, list_of_photo_button_objects):
    """The function responsible for setting a photo as the main one. It accepts parameters of the selected button
    and lists of all buttons."""
    # It will loop through each button and check if any are set as the main photo, if so it will remove them.
    for button_object in list_of_photo_button_objects:
        if button_object.main_photo:
            button_object.main_photo = False
            button_object.button.config(borderwidth=0)

    # Assigning the photo as the main one to the selected button.
    selected_button_object.main_photo = True
    selected_button_object.button.config(borderwidth=4)
