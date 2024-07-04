from tkinter import messagebox, END
from re import match
from requests import codes
from utils import config_data, constants
from services.api.announcements import request_to_add_the_announcement
from services.api.media import request_to_upload_images


def add_announcement(title_entry, location_entry, current_var_category, price_entry, description_text,
                     list_of_photo_button_objects, current_var_state, mobile_number_entry):
    """The function responsible for adding advertisements and photos, validates the entered data, sends it to
    the server and handles the response returned from the server."""
    # Validations entered data.
    if match("^.{10,45}$", title_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń ]{3,45}$", location_entry.get()):
            if current_var_category.get() in constants.categories:
                if match("^[0-9]{1,7}$", price_entry.get()):
                    if current_var_state.get() in constants.states:
                        if mobile_number_entry.get() == "" or match("^[+]?[0-9]{6,14}$", mobile_number_entry.get()):
                            if 80 <= len(description_text.get("1.0", "end-1c")) <= 400:

                                # If the validation passes correctly, the data will be assigned to the variables.
                                title = title_entry.get()
                                location = location_entry.get()
                                category_id = constants.categories.index(current_var_category.get()) + 1
                                state = current_var_state.get()
                                price = int(price_entry.get())
                                description = description_text.get("1.0", "end-1c")

                                if mobile_number_entry.get() == "":
                                    mobile_number = None
                                else:
                                    mobile_number = mobile_number_entry.get()

                                # Calling the function to send a request to add an advertisement to the server.
                                response_for_adding_announcement = request_to_add_the_announcement(
                                    title, location, category_id, state, price, mobile_number, description)

                                # If the response is 201, the photos are added to the server.
                                if response_for_adding_announcement.status_code == codes.created:

                                    # Assigning the returned id of the created announcement to a variable.
                                    announcement_id \
                                        = response_for_adding_announcement.json()["result"]["announcement_id"]

                                    # Creating a list of tuples with photos to upload and the main photo.
                                    images_to_upload = [
                                        (button_object.photo_to_upload, button_object.main_photo) for button_object in
                                        list_of_photo_button_objects if button_object.photo_to_upload
                                    ]

                                    if images_to_upload:
                                        # If the user has not selected the main photo, set the first photo.
                                        if not any(main_photo for _, main_photo in images_to_upload):
                                            images_to_upload[0] = (images_to_upload[0][0], True)

                                        # Sending a request to add photos to the server.
                                        response_for_uploading_images = request_to_upload_images(
                                            announcement_id, images_to_upload
                                        )

                                        # If there was an error sending photos, display a message.
                                        if response_for_uploading_images.status_code != codes.created:
                                            messagebox.showwarning("Błąd podczas dodawania zdjęć.",
                                                                   "Podczas dodawania zdjęć wystąpił błąd, spróbuj "
                                                                   "ponownie dodać zdjęcia z poziomu edycji ogłoszenia.")

                                    # Clearing fields for modified objects.
                                    for button_object in list_of_photo_button_objects:
                                        button_object.button.config(image=config_data.images["camera_icon"],
                                                                    state="disabled")
                                        button_object.photo_to_display = None
                                        button_object.photo_to_upload = None

                                        if button_object.main_photo:
                                            button_object.main_photo = False
                                            button_object.button.config(borderwidth=0)

                                        if button_object.button_delete:
                                            button_object.button_delete.destroy()
                                            button_object.button_delete = None

                                        # Cleaning data entry objects.
                                        title_entry.delete(0, END)
                                        location_entry.delete(0, END)
                                        price_entry.delete(0, END)
                                        mobile_number_entry.delete(0, END)
                                        description_text.delete("1.0", END)
                                        current_var_category.set("")
                                        current_var_state.set("")

                                    # Display a success message.
                                    messagebox.showinfo("Pomyślnie dodano ogłoszenie.",
                                                        f"Twoje ogłoszenie \"{title}\" zostało dodane, możesz dodać "
                                                        f"kolejne ogłoszenia.")

                                # If the status 400 occurred when adding an advertisement, display a message about
                                # incorrect data.
                                elif response_for_adding_announcement.status_code == codes.bad_request:
                                    messagebox.showwarning("Nie udało sie dodać ogłoszenia.",
                                                           "Wprowadzono niepoprawne dane do utworzenia ogłoszenia.")

                                # If a status other than 201 and 400 occurred, display an error.
                                else:
                                    messagebox.showerror("Błąd podczas dodawania ogłoszenia.",
                                                         "Nie udało sie dodać ogłoszenia, spróbuj później.")

                            # Incorrect description message.
                            else:
                                messagebox.showwarning("Błędny opis ogłoszenia.",
                                                       "Opis ogłoszenia powinien zawierać od 80 do 400 znaków.")

                        # Incorrect mobile number message.
                        else:
                            messagebox.showwarning("Błędny numer kontaktowy ogłoszenia.",
                                                   "Podany numer kontaktowy zawiera inne znaki niż cyfry lub"
                                                   " jego długość jest nieprawidłowa.")

                    # Incorrect state of announcement message.
                    else:
                        messagebox.showwarning("Błędny stan ogłoszenia.",
                                               "Nie wybrano stanu ogłoszenia.")

                # Incorrect price message.
                else:
                    messagebox.showwarning("Błędna cena ogłoszenia.",
                                           "Cena ogłoszenia powinna zawierać tylko cyfry, maksymalna "
                                           "kwota ogłoszenia to 9 999 999 zł.")

            # Incorrect category message.
            else:
                messagebox.showwarning("Błędna kategoria ogłoszenia.", "Nie wybrano kategorii ogłoszenia.")

        # Incorrect location message.
        else:
            messagebox.showwarning("Błędna lokalizacja ogłoszenia.",
                                   "Lokalizacja ogłoszenia powinna zawierać od 3 do 45 znaków, podaj jedynie "
                                   "miasto lub miejscowość.")

    # Incorrect title message.
    else:
        messagebox.showwarning("Błędny tytuł ogłoszenia.",
                               "Tytuł ogłoszenia powinien zawierać od 10 do 45 znaków.")
