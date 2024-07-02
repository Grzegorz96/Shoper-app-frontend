import config_data
from tkinter import messagebox
from re import match
from requests import codes
import backend_requests


def change_announcement_data(title_entry, location_entry, price_entry, description_text, announcement_object,
                             init_user_page_frame, current_var_state, mobile_number_entry, list_of_photo_button_objects,
                             deleted_photos):
    """The function responsible for validating the announcement data, calling the function that sends data to the
    backend, modifying multimedia files on the server and their paths in the database."""
    # Validations entered data.
    if match("^.{10,45}$", title_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń ]{3,45}$", location_entry.get()):
            if match("^[0-9]{1,7}$", price_entry.get()):
                if current_var_state.get() in config_data.states:
                    if mobile_number_entry.get() == "" or match("^[+]?[0-9]{6,14}$", mobile_number_entry.get()):
                        if (len(description_text.get("1.0", "end-1c")) >= 80 and len(
                                description_text.get("1.0", "end-1c")) <= 400):

                            # If validation is successful, the data is assigned to the variables.
                            title = title_entry.get()
                            location = location_entry.get()
                            price = int(price_entry.get())
                            state = current_var_state.get()
                            description = description_text.get("1.0", "end-1c")

                            if mobile_number_entry.get() == "":
                                mobile_number = None
                            else:
                                mobile_number = mobile_number_entry.get()

                            # Calling the function to send a request to change the announcement for the given arguments.
                            response_for_updating_announcement \
                                = backend_requests.request_to_update_the_announcement(title, description, price,
                                                                                      location, announcement_object.
                                                                                      announcement_id, state,
                                                                                      mobile_number)

                            # If the function returns a response with status 200, the attached photos will be added.
                            if response_for_updating_announcement.status_code == codes.ok:
                                # Assigning variables thanks to which the program knows when to enter certain blocks
                                # of code.
                                error_with_updating_photos = False
                                committed_operation_on_main_photo = False

                                # Deleting all selected photos from list, if the returned status is not other than
                                # 200 then the error_with_updating_photos flag will change its value to True.
                                if deleted_photos:
                                    response_for_deleting_photos = backend_requests.request_to_delete_images(
                                        deleted_photos
                                    )
                                    if response_for_deleting_photos.status_code != codes.ok:
                                        error_with_updating_photos = True

                                # If no error occurred while deleting photos from the server, the program will determine
                                # what to do with the main photo.
                                if not error_with_updating_photos:
                                    for main_photo_from_server in list_of_photo_button_objects:
                                        if main_photo_from_server.photo_from_main:
                                            committed_operation_on_main_photo = True
                                            if not main_photo_from_server.main_photo:
                                                for photo_button_with_main_photo in list_of_photo_button_objects:
                                                    if photo_button_with_main_photo.main_photo:
                                                        if photo_button_with_main_photo.photo_from_media:
                                                            response_for_switching_photos \
                                                                = backend_requests.request_to_switch_images({
                                                                    "main_photo_filename": main_photo_from_server.photo_to_upload,
                                                                    "media_photo_filename": photo_button_with_main_photo.photo_to_upload,
                                                                    "announcement_id": announcement_object.announcement_id,
                                                                })
                                                            if response_for_switching_photos.status_code != codes.ok:
                                                                error_with_updating_photos = True
                                                            break

                                                        else:
                                                            response_for_switching_photos \
                                                                = backend_requests.request_to_switch_images({
                                                                    "main_photo_filename": main_photo_from_server.photo_to_upload,
                                                                    "announcement_id": announcement_object.announcement_id,
                                                                })
                                                            if response_for_switching_photos.status_code == codes.ok:
                                                                response_for_uploading_photo\
                                                                    = backend_requests.request_to_upload_images(
                                                                        announcement_object.announcement_id,
                                                                        [(photo_button_with_main_photo.photo_to_upload,
                                                                            True)])
                                                                if response_for_uploading_photo.status_code != codes.created:
                                                                    error_with_updating_photos = True
                                                            else:
                                                                error_with_updating_photos = True
                                                            break
                                            break

                                # If there is a case that the main photo still needs to be modified and no error has
                                # occurred previously, the program will want to modify the main photo and check whether
                                # the user has manually selected any photo for the main photo.
                                if not committed_operation_on_main_photo and not error_with_updating_photos:
                                    for photo_button in list_of_photo_button_objects:
                                        if photo_button.main_photo:
                                            committed_operation_on_main_photo = True
                                            if photo_button.photo_from_media:
                                                response_for_switching_photos\
                                                    = backend_requests.request_to_switch_images({
                                                        "announcement_id": announcement_object.announcement_id,
                                                        "media_photo_filename": photo_button.photo_to_upload,
                                                    })

                                                if response_for_switching_photos.status_code != codes.ok:
                                                    error_with_updating_photos = True
                                            else:
                                                response_for_uploading_photo\
                                                    = backend_requests.request_to_upload_images(
                                                        announcement_object.announcement_id,
                                                        [(photo_button.photo_to_upload, True)])

                                                if response_for_uploading_photo.status_code != codes.created:
                                                    error_with_updating_photos = True
                                            break

                                # If the profile photo has not been changed, the program will set the main photo to the
                                # first one on the list.
                                if not committed_operation_on_main_photo and not error_with_updating_photos:
                                    for button in list_of_photo_button_objects:
                                        if button.photo_to_upload:
                                            if button.photo_from_media:
                                                response_for_switching_photos\
                                                    = backend_requests.request_to_switch_images({
                                                        "announcement_id": announcement_object.announcement_id,
                                                        "media_photo_filename": button.photo_to_upload,
                                                    })

                                                if response_for_switching_photos.status_code != codes.ok:
                                                    error_with_updating_photos = True
                                            else:
                                                response_for_uploading_photo\
                                                    = backend_requests.request_to_upload_images(
                                                        announcement_object.announcement_id,
                                                        [(button.photo_to_upload, True)])

                                                if response_for_uploading_photo.status_code == codes.created:
                                                    button.main_photo = True
                                                else:
                                                    error_with_updating_photos = True
                                            break

                                # If there was no upload error anywhere, the program will add all new photos added by
                                # the user.
                                if not error_with_updating_photos:
                                    # Creating a list of tuples with photos to upload.
                                    images_to_upload = [
                                        (selected_photo.photo_to_upload, False) for selected_photo
                                        in list_of_photo_button_objects if (selected_photo.photo_to_upload
                                                                            and not selected_photo.photo_from_main
                                                                            and not selected_photo.photo_from_media
                                                                            and not selected_photo.main_photo)]

                                    if images_to_upload:
                                        # Sending a request to add photos to the server.
                                        response_for_uploading_images = backend_requests.request_to_upload_images(
                                            announcement_object.announcement_id, images_to_upload)

                                        if response_for_uploading_images.status_code != codes.created:
                                            error_with_updating_photos = True

                                # If all photo-changing operations were completed successfully, a message will be
                                # displayed and the user page will be initialized.
                                if not error_with_updating_photos:
                                    messagebox.showinfo(
                                        f"Pomyślnie zaktualizowano Twoje ogłoszenie,"
                                        f" {config_data.logged_in_user_info.first_name}.",
                                        f"Twoje ogłoszenie \"{title}\" zostało zaktualizowane!")
                                    init_user_page_frame()

                                # If any error occurs while modifying the photo, an appropriate message will be
                                # displayed and the user's page will be initialized.
                                else:
                                    messagebox.showwarning("Wystąpił błąd podczas edycji zdjęć.",
                                                           "Ogłoszenie zostało pomyślnie zaktualizowane lecz "
                                                           "wystąpił błąd podczas edycji zdjęć, spróbuj później.")
                                    init_user_page_frame()

                            # If error 400 occurs while changing the data for the advertisement, a message about
                            # incorrect data will be displayed. In this case, such a message cannot be displayed
                            # because everything is validated in the program.
                            elif response_for_updating_announcement.status_code == codes.bad_request:
                                messagebox.showwarning("Nie udało sie zaktualizować ogłoszenia.",
                                                       "Wprowadzono niepoprawne dane do aktualizacji ogłoszenia.")

                            # If a response with a status other than 200 or 400 is returned, an error will be displayed.
                            else:
                                messagebox.showerror("Błąd podczas aktualizacji ogłoszenia.",
                                                     "Nie udało sie zaktualizować ogłoszenia, spróbuj później.")

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
                                       "Cena ogłoszenia powinna zawierać tylko cyfry, maksymalna kwota "
                                       "ogłoszenia to 9 999 999 zł.")

        # Incorrect location message.
        else:
            messagebox.showwarning("Błędna lokalizacja ogłoszenia.",
                                   "Lokalizacja ogłoszenia powinna zawierać od 3 do 45 znaków, podaj jedynie "
                                   "miasto lub miejscowość.")

    # Incorrect title message.
    else:
        messagebox.showwarning("Błędny tytuł ogłoszenia.", "Tytuł ogłoszenia powinien zawierać od 10 do 45 znaków.")