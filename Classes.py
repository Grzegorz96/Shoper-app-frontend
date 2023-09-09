class LoggedUser:
    """ The class of the logged-in user. When the user successfully logs in, the program will create a logged-in user
    object from the LoggedUser class and assign it to the global variable. The program will have access to user
    information from every level."""
    def __init__(self, user_id, first_name, last_name, email, login, password, date_of_birth, street, zip_code, city,
                 creation_account_date):
        """ Constructor for the LoggedUser class."""
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login = login
        self.password = password
        self.date_of_birth = date_of_birth
        self.street = street
        self.zip_code = zip_code
        self.city = city
        self.creation_account_date = creation_account_date

    def change_user_firstname(self, updated_name):
        """ setter for the first_name field."""
        self.first_name = updated_name

    def change_user_lastname(self, updated_lastname):
        """ setter for the last_name field."""
        self.last_name = updated_lastname

    def change_user_email(self, updated_email):
        """ setter for the email field."""
        self.email = updated_email

    def change_user_password(self, updated_password):
        """ setter for the password field."""
        self.password = updated_password

    def change_user_street(self, updated_street):
        """ setter for the street field."""
        self.street = updated_street

    def change_user_zip_code(self, updated_zip_code):
        """ setter for the zip_code field."""
        self.zip_code = updated_zip_code

    def change_user_city(self, updated_city):
        """ setter for the city field."""
        self.city = updated_city


class Announcement:
    """ Announcement class used to create announcements objects displayed on the main page and the user's page."""
    def __init__(self, announcement_id, first_name, seller_id, name_category, category_id, title, description, price,
                 location, main_photo, state, creation_date, mobile_number):
        """ Constructor for the Announcement class."""
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


class UserFavoriteAnnouncement:
    """ UserFavoriteAnnouncement class used to create announcements objects displayed on the favorite page."""
    def __init__(self, favorite_announcement_id, announcement_id, first_name, seller_id, title, description,
                 name_category, price, location, main_photo, state, creation_date, mobile_number):
        """ Constructor for the UserFavoriteAnnouncement class."""
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


class Message:
    """ Message class used to create message objects and display them in the message window and messages page."""
    def __init__(self, conversation_id, message_id, customer_flag, content, post_date, user_id, first_name):
        """ Constructor for the Message class."""
        self.conversation_id = conversation_id
        self.message_id = message_id
        self.customer_flag = customer_flag
        self.content = content
        self.post_date = post_date
        self.user_id = user_id
        self.first_name = first_name


class Conversation:
    """ Conversation class used to create conversation objects and display them in messages page."""
    def __init__(self, conversation_id, announcement_id, title, first_name):
        """ Constructor for the Conversation class."""
        self.conversation_id = conversation_id
        self.announcement_id = announcement_id
        self.title = title
        self.first_name = first_name


class PhotoButton:
    """ PhotoButton class used to create photo_button objects and performing operations on them related to adding,
    modifying,deleting and displaying user's announcement photos."""
    def __init__(self, button, photo_to_display, photo_to_upload, position_x, position_y, main_photo, button_delete,
                 photo_from_main, photo_from_media):
        """ Constructor for the PhotoButton class."""
        self.button = button
        self.photo_to_display = photo_to_display
        self.photo_to_upload = photo_to_upload
        self.position_x = position_x
        self.position_y = position_y
        self.main_photo = main_photo
        self.button_delete = button_delete
        self.photo_from_main = photo_from_main
        self.photo_from_media = photo_from_media
