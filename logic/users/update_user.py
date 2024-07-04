from utils import config_data
from re import match
from tkinter import messagebox, END
from requests import codes
from services.api.users import request_to_update_user_data


def update_user(entry, label, hidden_password):
    """The function responsible for changing user data, validating the entered data, determining what the user wants
    to change, sending it to the backend and changing the value in the user object."""
    # Assigning the entered data to variables.
    value = entry.get()
    column = None
    attribute = None

    # If the given string is included in the imported label object, then the program validates the entered data for
    # this key. Overwrites the column and attribute variables.
    if "Imie:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", value):
            column = "first_name"
            attribute = "Imie:"
        else:
            messagebox.showwarning("Niepoprawne imię.", "Wprowadzono niepoprawne dane imienia.")

    # If the given string is included in the imported label object, then the program validates the entered data for
    # this key. Overwrites the column and attribute variables.
    elif "Nazwisko:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", value):
            column = "last_name"
            attribute = "Nazwisko:"
        else:
            messagebox.showwarning("Niepoprawne nazwisko.", "Wprowadzono niepoprawne dane nazwiska.")

    # If the given string is included in the imported label object, then the program validates the entered data for
    # this key. Overwrites the column and attribute variables.
    elif "Email:" in label["text"]:
        if match(
                "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+"
                "|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$",
                value):
            column = "email"
            attribute = "Email:"
        else:
            messagebox.showwarning("Niepoprawny email.", "Wprowadzono niepoprawne dane email.")

    # If the given string is included in the imported label object, then the program validates the entered data for
    # this key. Overwrites the column and attribute variables.
    elif "Hasło:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", value):
            column = "password"
            attribute = "Hasło:"
        else:
            messagebox.showwarning("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")

    # If the given string is included in the imported label object, overwrites the column and attribute variables.
    elif "Ulica:" in label["text"]:
        column = "street"
        attribute = "Ulica:"

    # If the given string is included in the imported label object, overwrites the column and attribute variables.
    elif "Kod pocztowy:" in label["text"]:
        column = "zip_code"
        attribute = "Kod pocztowy:"

    # If the given string is included in the imported label object, overwrites the column and attribute variables.
    elif "Miasto:" in label["text"]:
        column = "city"
        attribute = "Miasto:"

    # If it entered a block and created a column.
    if column:
        # Calling the function to send a user update request for a specific column with a validated value.
        response_for_updating_user = request_to_update_user_data(column, value)

        # If the status code is 200 then update the given field in the user object.
        if response_for_updating_user.status_code == codes.ok:
            if column == "first_name":
                config_data.logged_in_user_info.change_user_firstname(value)
            elif column == "last_name":
                config_data.logged_in_user_info.change_user_lastname(value)
            elif column == "email":
                config_data.logged_in_user_info.change_user_email(value)
            elif column == "password":
                config_data.logged_in_user_info.change_user_password(value)
            elif column == "street":
                config_data.logged_in_user_info.change_user_street(value)
            elif column == "zip_code":
                config_data.logged_in_user_info.change_user_zip_code(value)
            elif column == "city":
                config_data.logged_in_user_info.change_user_city(value)

            # Label update on the user's website.
            if column == "password" and hidden_password:
                label.config(text=f"{attribute} {'*'*len(value)}")
            else:
                label.config(text=f"{attribute} {value}")
            # Delete the entered text in the imported object.
            entry.delete(0, END)
            # Display success message.
            messagebox.showinfo("Pomyślnie zaktualizowano profil użytkownika.",
                                f"Twoj profil został zaktualizowany, {config_data.logged_in_user_info.first_name}.")

        # If response satus is 400.
        elif response_for_updating_user.status_code == codes.bad_request:
            # When the user wants to change the email address to one already in the database.
            if "email_error" in response_for_updating_user.json():
                messagebox.showwarning("Nie udało sie zaktualizować emaila.",
                                       "Podany email jest już zarejestrowany.")

            # If the user enters unvalidated data, it is impossible in this program because the frontend validates
            # everything.
            else:
                messagebox.showwarning("Nie udało sie zaktualizować użytkownika.",
                                       "Wprowadzono niepoprawne dane do aktualizacji użytkownika.")

        # If we receive a response with a status other than 200 or 400, display error message.
        else:
            messagebox.showerror("Błąd podczas aktualizacji użytkownika.",
                                 "Nie udało sie zaktualizować użytkownika, spróbuj później.")
