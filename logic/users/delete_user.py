from tkinter import messagebox
from requests import codes
from services.api.users import request_to_delete_user
from logic.users.login.logout_user import logout_user


def delete_user():
    """Function responsible for deleting the user's account. The function asks the user for confirmation of the action,
    and then sends a request to the backend to delete the user's account. If the request is successful."""

    confirm = messagebox.askyesno("Potwierdzenie usunięcia konta", "Czy na pewno chcesz usunąć swoje konto?")

    if confirm:
        response = request_to_delete_user()
        if response.status_code == codes.ok:
            messagebox.showinfo("Konto usunięte", "Twoje konto zostało pomyślnie usunięte.")
            logout_user()

        else:
            messagebox.showerror("Błąd", "Wystąpił problem podczas usuwania konta. Spróbuj ponownie później.")
