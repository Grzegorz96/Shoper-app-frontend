class PhotoButton:
    """PhotoButton class used to create photo_button objects and performing operations on them related to adding,
    modifying,deleting and displaying user's announcement photos."""
    def __init__(self, button, photo_to_display, photo_to_upload, position_x, position_y, main_photo, button_delete,
                 photo_from_main, photo_from_media):
        """Constructor for the PhotoButton class."""
        self.button = button
        self.photo_to_display = photo_to_display
        self.photo_to_upload = photo_to_upload
        self.position_x = position_x
        self.position_y = position_y
        self.main_photo = main_photo
        self.button_delete = button_delete
        self.photo_from_main = photo_from_main
        self.photo_from_media = photo_from_media
