import backend_requests
from re import match
from tkinter import messagebox, END
from requests import codes
from utils import constants


def register_user(first_name_entry, last_name_entry, email_entry, login_entry, password_entry, current_var_day,
                  current_var_month, current_var_year, street_entry, zip_code_entry, city_entry):
    """The function responsible for frontend validation of the entered data - if the data is successfully validated,
    the function from the backend_request module will be called, which will send the entered data to the backend,
    depending on what status code is returned, the function will perform the appropriate actions and display the
    appropriate message."""
    # Validations of entered data.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", first_name_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", last_name_entry.get()):
            if match(
                    "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+"
                    "|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$", email_entry.get()):
                if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login_entry.get()):
                    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password_entry.get()):

                        if (current_var_year.get() in constants.years
                                and current_var_month.get() in constants.months
                                and current_var_day.get() in constants.days):

                            # If validation is successful, the data will be assigned to variables, which will then be
                            # placed as arguments to the request function.
                            first_name = first_name_entry.get()
                            last_name = last_name_entry.get()
                            email = email_entry.get()
                            login = login_entry.get()
                            password = password_entry.get()
                            date_of_birth = (f"{current_var_day.get()}-{current_var_month.get()}-"
                                             f"{current_var_year.get()}")
                            street = street_entry.get()
                            zip_code = zip_code_entry.get()
                            city = city_entry.get()
                            # Calling the user registration request function.
                            response_for_register_user = backend_requests.request_to_register_user(first_name,
                                                                                                   last_name, email,
                                                                                                   login, password,
                                                                                                   date_of_birth,
                                                                                                   street, zip_code,
                                                                                                   city)

                            # If the returned response status is 201, the program will delete all entered data from
                            # the entry and combobox objects and display an appropriate message.
                            if response_for_register_user.status_code == codes.created:
                                first_name_entry.delete(0, END)
                                last_name_entry.delete(0, END)
                                email_entry.delete(0, END)
                                login_entry.delete(0, END)
                                password_entry.delete(0, END)
                                current_var_day.set("")
                                current_var_month.set("")
                                current_var_year.set("")
                                street_entry.delete(0, END)
                                zip_code_entry.delete(0, END)
                                city_entry.delete(0, END)
                                messagebox.showinfo("Pomyślna rejestracja konta.", "Możesz sie zalogować.")

                            # If the returned response status is 400, the program will display a message that
                            # registration is not possible due to existing users with the provided data.
                            elif response_for_register_user.status_code == codes.bad_request:
                                if "login_error" in response_for_register_user.json():
                                    messagebox.showwarning("Nie udało sie utworzyć konta.",
                                                           "Użytkownik o podanym loginie jest już zarejestowany.")
                                elif "email_error" in response_for_register_user.json():
                                    messagebox.showwarning("Nie udało sie utworzyć konta.",
                                                           "Użytkownik o podanym emailu jest już zarejestowany.")
                                else:
                                    messagebox.showwarning("Nie udało sie utworzyć konta.",
                                                           "Niepoprawne dane do rejestracji konta.")

                            # If a status other than 201 or 400 is returned, an error message will be displayed.
                            else:
                                messagebox.showerror("Nie udało sie utworzyć konta.",
                                                     "Wystąpił błąd podczas rejestracji, spróbuj ponownie później.")

                        # Incorrect date of birth message.
                        else:
                            messagebox.showwarning("Wybierz date urodzenia.", "Nie wybrano daty urodzenia.")

                    # Incorrect password message.
                    else:
                        messagebox.showwarning("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")

                # Incorrect login message.
                else:
                    messagebox.showwarning("Niepoprawny login.", "Wprowadzono niepoprawne dane loginu.")

            # Incorrect email message.
            else:
                messagebox.showwarning("Niepoprawny email.", "Wprowadzono niepoprawne dane email.")

        # Incorrect last_name message.
        else:
            messagebox.showwarning("Niepoprawne nazwisko.", "Wprowadzono niepoprawne dane nazwiska.")

    # Incorrect first_name message.
    else:
        messagebox.showwarning("Niepoprawne imię.", "Wprowadzono niepoprawne dane imienia.")
