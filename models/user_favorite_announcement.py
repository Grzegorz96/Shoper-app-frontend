class UserFavoriteAnnouncement:
    """UserFavoriteAnnouncement class used to create announcements objects displayed on the favorite page."""
    def __init__(self, favorite_announcement_id, announcement_id, first_name, seller_id, title, description,
                 name_category, price, location, main_photo, state, creation_date, mobile_number):
        """Constructor for the UserFavoriteAnnouncement class."""
        self.favorite_announcement_id = favorite_announcement_id
        self.announcement_id = announcement_id
        self.first_name = first_name
        self.seller_id = seller_id
        self.title = title
        self.description = description
        self.name_category = name_category
        self.price = price
        self.location = location
        self.main_photo = main_photo
        self.state = state
        self.creation_date = creation_date
        self.mobile_number = mobile_number
