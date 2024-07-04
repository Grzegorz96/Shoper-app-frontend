class LoggedUser:
    """The class of the logged-in user. When the user successfully logs in, the program will create a logged-in user
    object from the LoggedUser class and assign it to the global variable. The program will have access to user
    information from every level."""
    def __init__(self, user_id, first_name, last_name, email, login, password, date_of_birth, street, zip_code, city,
                 creation_account_date):
        """Constructor for the LoggedUser class."""
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
        """Setter for the first_name field."""
        self.first_name = updated_name

    def change_user_lastname(self, updated_lastname):
        """Setter for the last_name field."""
        self.last_name = updated_lastname

    def change_user_email(self, updated_email):
        """Setter for the email field."""
        self.email = updated_email

    def change_user_password(self, updated_password):
        """Setter for the password field."""
        self.password = updated_password

    def change_user_street(self, updated_street):
        """Setter for the street field."""
        self.street = updated_street

    def change_user_zip_code(self, updated_zip_code):
        """Setter for the zip_code field."""
        self.zip_code = updated_zip_code

    def change_user_city(self, updated_city):
        """Setter for the city field."""
        self.city = updated_city
