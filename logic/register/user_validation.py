from re import match
from tkinter import messagebox
from requests import codes
import backend_requests


def verify_login(login_entry):
    """Function responsible for checking in the database whether the given login is already taken and informing the
    user about the result of the operation."""
    # Validation entered data.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login_entry.get()):

        # If validation is successful, call a function to send a login verification request.
        response_for_login_verification = backend_requests.request_to_verify_login(login_entry.get())

        # If response status is 200 then display the availability message.
        if response_for_login_verification.status_code == codes.ok:
            messagebox.showinfo("Podany login jest dostępny.",
                                f"Nie istnieje jeszcze użytkownik o loginie \"{login_entry.get()}\".")

        # If response status is 400 then display an unavailability message.
        elif response_for_login_verification.status_code == codes.bad_request:
            messagebox.showinfo("Podany login jest już zajęty.",
                                f"Istnieje zarejestrowany użytkownik o loginie \"{login_entry.get()}\".")

        # If response status is other than 200 and 400, display error message.
        else:
            messagebox.showerror("Błąd podczas weryfikacji loginu.",
                                 "Nie udało się zweryfikować loginu, spróbuj później.")

    # Incorrect login message.
    else:
        messagebox.showwarning("Niepoprawny login",
                               "Nie możesz użyć tego loginu do rejestracji. Sprawdź wzór loginu")


def verify_password(password_entry):
    """Function responsible for verifying the password entered by the user and informing him of the result."""
    # If the password entered by the user passes validation, display an acceptance message.
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password_entry.get()):
        messagebox.showinfo("Poprawne hasło.", "Możesz użyć tego hasła do rejestracji.")

    # If the password entered by the user does not pass validation, display a message about non-acceptance.
    else:
        messagebox.showinfo("Niepoprawne hasło.",
                            "Nie możesz użyć tego hasła do rejestracji. Sprawdź wzór hasła.")


def show_pattern(arg):
    """A feature that displays login and password requirements to the user during registration."""
    # If the transmitted argument is equal to the login pattern string, then display a message.
    if arg == "Wzór loginu":
        messagebox.showinfo("Wymogi dotyczące loginu:",
                            "- musi zawierać minimum 5 znaków,\n- może zawierać wielkie oraz małe litery,"
                            "\n- może zawierać cyfry,\n- nie może zawierać znaków specjalnych.")

    # If the transmitted argument is equal to the password pattern string, then display a message.
    elif arg == "Wzór hasła":
        messagebox.showinfo("Wymogi dotyczące hasła:",
                            "- musi zawierać minimum 7 znaków,\n- może zawierać wielkie oraz małe litery,"
                            "\n- może zawierać cyfry,\n- może zawierać znaki specjalne.")
