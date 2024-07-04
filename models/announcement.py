class Announcement:
    """Announcement class used to create announcements objects displayed on the main page and the user's page."""
    def __init__(self, announcement_id, first_name, seller_id, name_category, category_id, title, description, price,
                 location, main_photo, state, creation_date, mobile_number):
        """Constructor for the Announcement class."""
        self.announcement_id = announcement_id
        self.first_name = first_name
        self.seller_id = seller_id
        self.name_category = name_category
        self.category_id = category_id
        self.title = title
        self.description = description
        self.price = price
        self.location = location
        self.main_photo = main_photo
        self.state = state
        self.creation_date = creation_date
        self.mobile_number = mobile_number
