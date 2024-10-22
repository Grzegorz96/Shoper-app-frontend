from utils import config_data
from re import match
from tkinter import messagebox, Button
from requests import codes
from datetime import datetime
from models.logged_user import LoggedUser
from logic.users.login.logout_user import logout_user
from services.api.users import request_to_login_user


def login_user(entry_login_or_email, entry_password, top_panel_frame):
    """The function responsible for logging in the user, validating the entered data, changing the global
    is_user_logged_in flag and creating a user object."""
    # Validations of entered data.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", entry_login_or_email.get()) or match(
            "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+"
            "|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$", entry_login_or_email.get()):

        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", entry_password.get()):
            login_or_email = entry_login_or_email.get()
            password = entry_password.get()

            # If validation is successful, the program will call the function of sending a user login request with
            # the provided data.
            response_for_login_user = request_to_login_user(login_or_email, password)

            # If the returned status is 200, then the program destroys all previously created login windows, changes
            # the login flag to True, creates a user object with the data retrieved from the database, creates a logout
            # button and displays the appropriate message.
            if response_for_login_user.status_code == codes.ok:

                for window in config_data.list_of_active_windows:
                    window.destroy()

                config_data.list_of_active_windows.clear()
                user_info = response_for_login_user.json()["result"]
                config_data.logged_in_user_info = LoggedUser(
                    user_info["user_id"],
                    user_info["first_name"],
                    user_info["last_name"],
                    user_info["email"],
                    user_info["login"],
                    user_info["password"],
                    user_info["date_of_birth"],
                    user_info["street"],
                    user_info["zip_code"],
                    user_info["city"],
                    datetime.strptime(user_info["creation_account_date"], '%Y-%m-%d %H:%M:%S')
                )

                config_data.logout_button = Button(top_panel_frame, image=config_data.images["logout"], text="Wyloguj",
                                                   font=("Arial", 8), borderwidth=0, bg="#D3D3D3", command=logout_user)

                config_data.logout_button.place(x=1208, y=58, height=20, width=45)
                messagebox.showinfo("Pomyślnie zalogowano.",
                                    f"Użytkownik {config_data.logged_in_user_info.first_name} pomyślnie zalogowany.")

            # If it returns a status of 400, a message about the lack of a user in the database will be displayed.
            elif response_for_login_user.status_code == codes.bad_request:
                messagebox.showwarning("Błędne dane logowania.", "Wprowadzone dane logowania są nieprawidłowe.")

            # If a status other than 200 or 400 is returned, an error message will be displayed.
            else:
                messagebox.showerror("Błąd podczas logowania.",
                                     "W chwili obecnej nie możemy Cię zalogować, spróbuj ponownie później.")

        # Incorrect password message.
        else:
            messagebox.showwarning("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")

    # Incorrect login or email message.
    else:
        messagebox.showwarning("Niepoprawny login lub email.",
                               "Wprowadzono niepoprawne dane loginu lub emaila.")
