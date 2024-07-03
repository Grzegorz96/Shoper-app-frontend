from utils import config_data


def delete_image(button_object, deleted_photos=None):
    """Function responsible for removing a photo from the PhotoButton object and restoring the initial values
    to the PhotoButton object."""
    # If the function is called with the deleted_photos parameter, which is a list, then the program additionally
    # clears the necessary fields of the object and adds the photo to the list.
    if isinstance(deleted_photos, list):
        if button_object.photo_from_main:
            button_object.photo_from_main = False
            deleted_photos.append((button_object.photo_to_upload, True))
        elif button_object.photo_from_media:
            deleted_photos.append((button_object.photo_to_upload, False))
            button_object.photo_from_media = False

    # Clearing the remaining fields.
    button_object.button.config(image=config_data.images["camera_icon"], state="disabled")
    button_object.photo_to_display = None
    button_object.photo_to_upload = None
    # If the photo being deleted was the main photo, change additional fields.
    if button_object.main_photo:
        button_object.main_photo = False
        button_object.button.config(borderwidth=0)
    # Destruction and removal of the delete button object from the field.
    if button_object.button_delete:
        button_object.button_delete.destroy()
        button_object.button_delete = None
