class LoggedUser:
    def __init__(self, user_id, first_name, last_name, email, login, password, date_of_birth, street, zip_code, city):
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

    def change_user_firstname(self, updated_name):
        self.first_name = updated_name

    def change_user_lastname(self, updated_lastname):
        self.last_name = updated_lastname

    def change_user_email(self, updated_email):
        self.email = updated_email

    def change_user_password(self, updated_password):
        self.password = updated_password

    def change_user_street(self, updated_street):
        self.street = updated_street

    def change_user_zip_code(self, updated_zip_code):
        self.zip_code = updated_zip_code

    def change_user_city(self, updated_city):
        self.city = updated_city


class Announcement:
    def __init__(self, announcement_id, first_name, seller_id, name_category, category_id, title, description, price,
                 location, main_photo):
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


class UserFavoriteAnnouncement:
    def __init__(self, favorite_announcement_id, announcement_id, first_name, seller_id, title, description,
                 name_category, price, location, main_photo):
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


class Message:
    def __init__(self, conversation_id, message_id, customer_flag, content, date, time, user_id, first_name):
        self.conversation_id = conversation_id
        self.message_id = message_id
        self.customer_flag = customer_flag
        self.content = content
        self.date = date
        self.time = time
        self.user_id = user_id
        self.first_name = first_name


class Conversation:
    def __init__(self, conversation_id, announcement_id, title, first_name):
        self.conversation_id = conversation_id
        self.announcement_id = announcement_id
        self.title = title
        self.first_name = first_name


class PhotoButton:
    def __init__(self, button, photo_to_display, photo_to_upload, position_x, position_y, main_photo, button_delete):
        self.button = button
        self.photo_to_display = photo_to_display
        self.photo_to_upload = photo_to_upload
        self.position_x = position_x
        self.position_y = position_y
        self.main_photo = main_photo
        self.button_delete = button_delete
