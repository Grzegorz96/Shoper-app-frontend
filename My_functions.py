from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from re import match
from User_Class import LoggedUser, Announcement, UserFavoriteAnnouncement, Message, Conversation
import Config_data
import Backend_requests
from requests import codes
from PIL import Image, ImageTk
from datetime import datetime


# User registration function
def register_user(first_name_entry, last_name_entry, email_entry, login_entry, password_entry, combobox_day_var,
                  combobox_day_birthday, combobox_month_var, combobox_month_birthday, combobox_year_var,
                  combobox_year_birthday, street_entry, zip_code_entry, city_entry):
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", first_name_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", last_name_entry.get()):
            if match(
                    "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+"
                    "|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$", email_entry.get()):
                if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login_entry.get()):
                    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password_entry.get()):
                        if combobox_year_var.get() in combobox_year_birthday["values"] \
                                and combobox_month_var.get() in combobox_month_birthday["values"] \
                                and combobox_day_var.get() in combobox_day_birthday["values"]:

                            first_name = first_name_entry.get()
                            last_name = last_name_entry.get()
                            email = email_entry.get()
                            login = login_entry.get()
                            password = password_entry.get()
                            date_of_birth = (f"{combobox_day_var.get()}-{combobox_month_var.get()}-"
                                             f"{combobox_year_var.get()}")
                            street = street_entry.get()
                            zip_code = zip_code_entry.get()
                            city = city_entry.get()

                            response_for_register_user = Backend_requests.request_to_register_user(first_name,
                                                                                                   last_name, email,
                                                                                                   login, password,
                                                                                                   date_of_birth,
                                                                                                   street, zip_code,
                                                                                                   city)
                            if response_for_register_user.status_code == codes.created:
                                messagebox.showinfo("Pomyślna rejestracja konta.", "Możesz sie zalogować.")
                                first_name_entry.delete(0, END)
                                last_name_entry.delete(0, END)
                                email_entry.delete(0, END)
                                login_entry.delete(0, END)
                                password_entry.delete(0, END)
                                combobox_day_var.set("")
                                combobox_month_var.set("")
                                combobox_year_var.set("")
                                street_entry.delete(0, END)
                                zip_code_entry.delete(0, END)
                                city_entry.delete(0, END)

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

                            else:
                                messagebox.showerror("Nie udało sie utworzyć konta.",
                                                     "Wystąpił błąd podczas rejestracji, spróbuj ponownie później.")

                        else:
                            messagebox.showwarning("Wybierz date urodzenia.", "Nie wybrano daty urodzenia.")
                    else:
                        messagebox.showwarning("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")
                else:
                    messagebox.showwarning("Niepoprawny login.", "Wprowadzono niepoprawne dane loginu.")
            else:
                messagebox.showwarning("Niepoprawny email.", "Wprowadzono niepoprawne dane email.")
        else:
            messagebox.showwarning("Niepoprawne nazwisko.", "Wprowadzono niepoprawne dane nazwiska.")
    else:
        messagebox.showwarning("Niepoprawne imię.", "Wprowadzono niepoprawne dane imienia.")


# User login function
def login_user(entry_login_or_email, entry_password, top_panel_frame, init_shopper_page_frame, root):
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", entry_login_or_email.get()) or match(
            "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+"
            "|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$", entry_login_or_email.get()):

        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", entry_password.get()):
            login_or_email = entry_login_or_email.get()
            password = entry_password.get()

            response_for_login_user = Backend_requests.request_to_login_user(login_or_email, password)

            if response_for_login_user.status_code == codes.ok:

                for window in Config_data.list_of_active_windows:
                    window.destroy()
                Config_data.list_of_active_windows = []

                user_info = response_for_login_user.json()["result"]
                Config_data.is_user_logged_in = True
                Config_data.logged_in_user_info = LoggedUser(
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

                user_name = Config_data.logged_in_user_info.first_name
                messagebox.showinfo("Pomyślnie zalogowano.", f"Użytkownik {user_name} pomyślnie zalogowany.")
                logout_button = Button(top_panel_frame, text="Wyloguj", font=("Arial", 8), borderwidth=0,
                                       bg="#D3D3D3", command=lambda: logout_user(logout_button, user_name,
                                                                                 init_shopper_page_frame, root))
                logout_button.place(x=1196, y=60, height=18, width=56)

            elif response_for_login_user.status_code == codes.bad_request:
                messagebox.showwarning("Nie ma takiego użytkownika.",
                                       "Użytkownik o podanych danych nie istnieje.")
            else:
                messagebox.showerror("Błąd podczas logowania.",
                                     "W chwili obecnej nie możemy Cię zalogować, spróbuj ponownie później.")
        else:
            messagebox.showwarning("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")
    else:
        messagebox.showwarning("Niepoprawny login lub email.",
                               "Wprowadzono niepoprawne dane loginu lub emaila.")


# User logout function
def logout_user(logout_button, user_name, init_shopper_page_frame, root):
    Config_data.is_user_logged_in = False
    Config_data.logged_in_user_info = None

    for window in Config_data.list_of_active_windows:
        window.destroy()
    Config_data.list_of_active_windows = []

    init_shopper_page_frame(root)
    logout_button.destroy()
    messagebox.showinfo("Pomyślnie wylogowano.", f"Użytkownik {user_name} został pomyślnie wylogowany.")


def change_announcement_data(title_entry, location_entry, price_entry, description_text, announcement_object,
                             init_user_page_frame, root, current_var_state, select_state, mobile_number_entry,
                             list_of_photo_button_objects, deleted_photos):

    if match("^.{10,45}$", title_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń ]{3,45}$", location_entry.get()):
            if match("^[0-9]{1,7}$", price_entry.get()):
                if current_var_state.get() in select_state["values"]:
                    if mobile_number_entry.get() == "" or match("^[+]?[0-9]{6,14}$", mobile_number_entry.get()):
                        if (len(description_text.get("1.0", "end-1c")) >= 80 and len(
                                description_text.get("1.0", "end-1c")) <= 400):

                            title = title_entry.get()
                            location = location_entry.get()
                            price = int(price_entry.get())
                            state = current_var_state.get()
                            if mobile_number_entry.get() == "":
                                mobile_number = None
                            else:
                                mobile_number = mobile_number_entry.get()
                            description = description_text.get("1.0", "end-1c")

                            response_for_updating_announcement \
                                = Backend_requests.request_to_update_the_announcement(title, description, price,
                                                                                      location, announcement_object.
                                                                                      announcement_id, state,
                                                                                      mobile_number)
                            if response_for_updating_announcement.status_code == codes.ok:

                                error_with_updating_photos = False
                                committed_operation_on_main_photo = False

                                for path, main_photo_flag in deleted_photos:
                                    response_for_deleting_photo = Backend_requests.request_to_delete_photo(
                                        path, main_photo_flag)
                                    if response_for_deleting_photo.status_code != codes.ok:
                                        error_with_updating_photos = True

                                if not error_with_updating_photos:
                                    for main_photo_from_server in list_of_photo_button_objects:
                                        if main_photo_from_server.photo_from_main:
                                            committed_operation_on_main_photo = True
                                            if not main_photo_from_server.main_photo:
                                                for photo_button_with_main_photo in list_of_photo_button_objects:
                                                    if photo_button_with_main_photo.main_photo:
                                                        if photo_button_with_main_photo.photo_from_media:
                                                            response_for_switching_photos \
                                                                = Backend_requests.request_to_switch_photos(
                                                                    announcement_object.announcement_id,
                                                                    main_photo_from_server.photo_to_upload,
                                                                    photo_button_with_main_photo.photo_to_upload,
                                                                    1, 1)
                                                            if response_for_switching_photos.status_code != codes.ok:
                                                                error_with_updating_photos = True
                                                            break

                                                        else:
                                                            response_for_switching_photos \
                                                                = Backend_requests.request_to_switch_photos(
                                                                    announcement_object.announcement_id,
                                                                    main_photo_from_server.photo_to_upload,
                                                                    None, 1, 0)
                                                            if response_for_switching_photos.status_code == codes.ok:
                                                                response_for_uploading_photo\
                                                                    = Backend_requests.request_to_upload_photo(
                                                                        announcement_object.announcement_id, 1,
                                                                        photo_button_with_main_photo.photo_to_upload)
                                                                if response_for_uploading_photo.status != codes.created:
                                                                    error_with_updating_photos = True
                                                            else:
                                                                error_with_updating_photos = True
                                                            break
                                            break

                                if not committed_operation_on_main_photo and not error_with_updating_photos:
                                    for photo_button in list_of_photo_button_objects:
                                        if photo_button.main_photo:
                                            committed_operation_on_main_photo = True
                                            if photo_button.photo_from_media:
                                                response_for_switching_photos\
                                                    = Backend_requests.request_to_switch_photos(
                                                        announcement_object.announcement_id, None,
                                                        photo_button.photo_to_upload, 0, 1)
                                                if response_for_switching_photos.status_code != codes.ok:
                                                    error_with_updating_photos = True
                                            else:
                                                response_for_uploading_photo\
                                                    = Backend_requests.request_to_upload_photo(
                                                        announcement_object.announcement_id, 1,
                                                        photo_button.photo_to_upload)
                                                if response_for_uploading_photo.status != codes.created:
                                                    error_with_updating_photos = True
                                            break

                                if not committed_operation_on_main_photo and not error_with_updating_photos:
                                    for button in list_of_photo_button_objects:
                                        if button.photo_to_upload:
                                            if button.photo_from_media:
                                                response_for_switching_photos\
                                                    = Backend_requests.request_to_switch_photos(
                                                        announcement_object.announcement_id, None,
                                                        button.photo_to_upload, 0, 1)
                                                if response_for_switching_photos.status_code != codes.ok:
                                                    error_with_updating_photos = True
                                            else:
                                                response_for_uploading_photo\
                                                    = Backend_requests.request_to_upload_photo(
                                                        announcement_object.announcement_id, 1,
                                                        button.photo_to_upload)
                                                if response_for_uploading_photo.status == codes.created:
                                                    button.main_photo = 1
                                                else:
                                                    error_with_updating_photos = True
                                            break

                                if not error_with_updating_photos:

                                    for selected_photo in list_of_photo_button_objects:
                                        if (selected_photo.photo_to_upload
                                                and not selected_photo.photo_from_main
                                                and not selected_photo.photo_from_media
                                                and not selected_photo.main_photo):
                                            response_for_uploading_photo = Backend_requests.request_to_upload_photo(
                                                announcement_object.announcement_id, 0, selected_photo.photo_to_upload)
                                            if response_for_uploading_photo.status != codes.created:
                                                error_with_updating_photos = True

                                if not error_with_updating_photos:
                                    messagebox.showinfo(
                                        f"Pomyślnie zaktualizowano Twoje ogłoszenie,"
                                        f" {Config_data.logged_in_user_info.first_name}.",
                                        f"Twoje ogłoszenie \"{title}\" zostało zaktualizowane!")
                                    init_user_page_frame(root)
                                else:
                                    messagebox.showwarning("Wystąpił błąd podczas edycji zdjęć.",
                                                           "Ogłoszenie zostało pomyślnie zaktualizowane lecz "
                                                           "wystąpił błąd podczas edycji zdjęć, spróbuj później.")
                                    init_user_page_frame(root)

                            elif response_for_updating_announcement.status_code == codes.bad_request:
                                messagebox.showwarning("Nie udało sie zaktualizować ogłoszenia.",
                                                       "Wprowadzono niepoprawne dane do aktualizacji ogłoszenia.")

                            else:
                                messagebox.showerror("Błąd podczas aktualizacji ogłoszenia.",
                                                     "Nie udało sie zaktualizować ogłoszenia, spróbuj później.")
                        else:
                            messagebox.showwarning("Błędny opis ogłoszenia.",
                                                   "Opis ogłoszenia powinien zawierać od 80 do 400 znaków.")
                    else:
                        messagebox.showwarning("Błędny numer kontaktowy ogłoszenia.",
                                               "Podany numer kontaktowy zawiera inne znaki niż cyfry lub"
                                               " jego długość jest nieprawidłowa.")
                else:
                    messagebox.showwarning("Błędny stan ogłoszenia.",
                                           "Nie wybrano stanu ogłoszenia.")

            else:
                messagebox.showwarning("Błędna cena ogłoszenia.",
                                       "Cena ogłoszenia powinna zawierać tylko cyfry, maksymalna kwota "
                                       "ogłoszenia to 9 999 999 zł.")
        else:
            messagebox.showwarning("Błędna lokalizacja ogłoszenia.",
                                   "Lokalizacja ogłoszenia powinna zawierać od 3 do 45 znaków, podaj jedynie "
                                   "miasto lub miejscowość.")
    else:
        messagebox.showwarning("Błędny tytuł ogłoszenia.", "Tytuł ogłoszenia powinien zawierać od 10 do 45 znaków.")


def download_user_announcements(active_flag, page):
    response_for_getting_user_announcements = Backend_requests.request_to_get_user_announcements(active_flag, page)
    if response_for_getting_user_announcements.status_code == codes.ok:

        list_of_objects_user_announcements = []
        for announcement in response_for_getting_user_announcements.json()["result"]:
            user_announcement_object = Announcement(
                announcement["announcement_id"],
                announcement["first_name"],
                announcement["seller_id"],
                announcement["name_category"],
                announcement["category_id"],
                announcement["title"],
                announcement["description"],
                announcement["price"],
                announcement["location"],
                announcement["main_photo"],
                announcement["state"],
                announcement["creation_date"],
                announcement["mobile_number"]
            )
            if user_announcement_object.main_photo:
                response_for_getting_photo = Backend_requests.request_to_get_photo(user_announcement_object.main_photo)
                if response_for_getting_photo.status == codes.ok:
                    main_photo = ImageTk.PhotoImage(Image.open(response_for_getting_photo).resize((90, 67)))
                    user_announcement_object.main_photo = main_photo
                else:
                    user_announcement_object.main_photo = None

            list_of_objects_user_announcements.append(user_announcement_object)

        return list_of_objects_user_announcements

    else:
        messagebox.showerror("Błąd podczas wczytywania ogłoszeń.",
                             "Nie udalo sie wczytać Twoich ogłoszeń, spróbuj później.")
        return []


def add_announcement(title_entry, location_entry, current_var_category, price_entry, description_text,
                     select_categories, list_of_photo_button_objects, select_state, current_var_state,
                     mobile_number_entry):
    if match("^.{10,45}$", title_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń ]{3,45}$", location_entry.get()):
            if current_var_category.get() in select_categories["values"]:
                if match("^[0-9]{1,7}$", price_entry.get()):
                    if current_var_state.get() in select_state["values"]:
                        if mobile_number_entry.get() == "" or match("^[+]?[0-9]{6,14}$", mobile_number_entry.get()):
                            if 80 <= len(description_text.get("1.0", "end-1c")) <= 400:

                                title = title_entry.get()
                                location = location_entry.get()
                                category_id = select_categories["values"].index(current_var_category.get()) + 1
                                state = current_var_state.get()
                                price = int(price_entry.get())
                                if mobile_number_entry.get() == "":
                                    mobile_number = None
                                else:
                                    mobile_number = mobile_number_entry.get()

                                description = description_text.get("1.0", "end-1c")

                                response_for_adding_announcement = Backend_requests.request_to_add_the_announcement(
                                    title, location, category_id, state, price, mobile_number, description)

                                if response_for_adding_announcement.status_code == codes.created:
                                    announcement_id \
                                        = response_for_adding_announcement.json()["result"]["announcement_id"]
                                    error_with_uploading = False
                                    list_of_photo_button_objects_to_upload = []
                                    for button_object in list_of_photo_button_objects:
                                        if button_object.photo_to_upload:
                                            list_of_photo_button_objects_to_upload.append(button_object)

                                    if list_of_photo_button_objects_to_upload:
                                        selected_main_photo = False
                                        for button_object in list_of_photo_button_objects_to_upload:
                                            if button_object.main_photo == 1:
                                                selected_main_photo = True

                                        if not selected_main_photo:
                                            list_of_photo_button_objects_to_upload[0].main_photo = 1

                                        for button_object in list_of_photo_button_objects_to_upload:
                                            response_for_uploading_photo = Backend_requests.request_to_upload_photo(
                                                announcement_id, button_object.main_photo,
                                                button_object.photo_to_upload)

                                            if response_for_uploading_photo.status != codes.created:
                                                error_with_uploading = True

                                        for button_object in list_of_photo_button_objects_to_upload:
                                            button_object.button.config(image=Config_data.images["camera_icon"],
                                                                        state="disabled")
                                            button_object.photo_to_display = None
                                            button_object.photo_to_upload = None

                                            if button_object.main_photo == 1:
                                                button_object.main_photo = 0
                                                button_object.button.config(borderwidth=0)

                                            if button_object.button_delete:
                                                button_object.button_delete.destroy()
                                                button_object.button_delete = None

                                    title_entry.delete(0, END)
                                    location_entry.delete(0, END)
                                    price_entry.delete(0, END)
                                    mobile_number_entry.delete(0, END)
                                    description_text.delete("1.0", END)
                                    current_var_category.set("")
                                    current_var_state.set("")

                                    if error_with_uploading:
                                        messagebox.showerror("Błąd podczas dodawania zdjęć.",
                                                             "Podczas dodawania zdjęć wystąpił błąd, spróbuj"
                                                             " ponownie dodać zdjęcia z poziomu edycji ogłoszenia.")

                                    messagebox.showinfo("Pomyślnie dodano ogłoszenie.",
                                                        f"Twoje ogłoszenie \"{title}\" zostało dodane, możesz dodać "
                                                        f"kolejne ogłoszenia.")

                                elif response_for_adding_announcement.status_code == codes.bad_request:
                                    messagebox.showwarning("Nie udało sie dodać ogłoszenia.",
                                                           "Wprowadzono niepoprawne dane do utworzenia ogłoszenia.")
                                else:
                                    messagebox.showerror("Błąd podczas dodawania ogłoszenia.",
                                                         "Nie udało sie dodać ogłoszenia, spróbuj później.")
                            else:
                                messagebox.showwarning("Błędny opis ogłoszenia.",
                                                       "Opis ogłoszenia powinien zawierać od 80 do 400 znaków.")
                        else:
                            messagebox.showwarning("Błędny numer kontaktowy ogłoszenia.",
                                                   "Podany numer kontaktowy zawiera inne znaki niż cyfry lub"
                                                   " jego długość jest nieprawidłowa.")
                    else:
                        messagebox.showwarning("Błędny stan ogłoszenia.",
                                               "Nie wybrano stanu ogłoszenia.")
                else:
                    messagebox.showwarning("Błędna cena ogłoszenia.",
                                           "Cena ogłoszenia powinna zawierać tylko cyfry, maksymalna "
                                           "kwota ogłoszenia to 9 999 999 zł.")
            else:
                messagebox.showwarning("Błędna kategoria ogłoszenia.", "Nie wybrano kategorii ogłoszenia.")
        else:
            messagebox.showwarning("Błędna lokalizacja ogłoszenia.",
                                   "Lokalizacja ogłoszenia powinna zawierać od 3 do 45 znaków, podaj jedynie "
                                   "miasto lub miejscowość.")
    else:
        messagebox.showwarning("Błędny tytuł ogłoszenia.",
                               "Tytuł ogłoszenia powinien zawierać od 10 do 45 znaków.")


def verify_login(login_entry):
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login_entry.get()):
        response_for_login_verification = Backend_requests.request_to_verify_login(login_entry.get())

        if response_for_login_verification.status_code == codes.ok:
            messagebox.showinfo("Podany login jest dostępny.",
                                f"Nie istnieje jeszcze użytkownik o loginie \"{login_entry.get()}\".")
        elif response_for_login_verification.status_code == codes.bad_request:
            messagebox.showinfo("Podany login jest już zajęty.",
                                f"Istnieje zarejestrowany użytkownik o loginie \"{login_entry.get()}\".")
        else:
            messagebox.showerror("Błąd podczas weryfikacji loginu.",
                                 "Nie udało się zweryfikować loginu, spróbuj później.")

    else:
        messagebox.showwarning("Niepoprawny login",
                               "Nie możesz użyć tego loginu do rejestracji. Sprawdź wzór loginu")


def verify_password(password_entry):
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password_entry.get()):
        messagebox.showinfo("Poprawne hasło.", "Możesz użyć tego hasła do rejestracji.")
    else:
        messagebox.showinfo("Niepoprawne hasło.",
                            "Nie możesz użyć tego hasła do rejestracji. Sprawdź wzór hasła.")


def show_pattern(arg):
    if arg == "Wzór loginu":
        messagebox.showinfo("Wymogi dotyczące loginu:",
                            "- musi zawierać minimum 5 znaków,\n- może zawierać wielkie oraz małe litery,"
                            "\n- może zawierać cyfry,\n- nie może zawierać znaków specjalnych.")
    elif arg == "Wzór hasła":
        messagebox.showinfo("Wymogi dotyczące hasła:",
                            "- musi zawierać minimum 7 znaków,\n- może zawierać wielkie oraz małe litery,"
                            "\n- może zawierać cyfry,\n- może zawierać znaki specjalne.")


def delete_text(entry_object):
    entry_object.delete(0, END)
    entry_object.unbind("<Button-1>")


def change_user_data(entry, label, hidden_password):
    value = entry.get()
    column = None
    attribute = None
    if "Imie:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", value):
            column = "first_name"
            attribute = "Imie:"
        else:
            messagebox.showwarning("Niepoprawne imię.", "Wprowadzono niepoprawne dane imienia.")

    elif "Nazwisko:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", value):
            column = "last_name"
            attribute = "Nazwisko:"
        else:
            messagebox.showwarning("Niepoprawne nazwisko.", "Wprowadzono niepoprawne dane nazwiska.")

    elif "Email:" in label["text"]:
        if match(
                "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+"
                "|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$",
                value):
            column = "email"
            attribute = "Email:"
        else:
            messagebox.showwarning("Niepoprawny email.", "Wprowadzono niepoprawne dane email.")

    elif "Hasło:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", value):
            column = "password"
            attribute = "Hasło:"
        else:
            messagebox.showwarning("Niepoprawne hasło.", "Wprowadzono niepoprawne dane hasła.")

    elif "Ulica:" in label["text"]:
        column = "street"
        attribute = "Ulica:"

    elif "Kod pocztowy:" in label["text"]:
        column = "zip_code"
        attribute = "Kod pocztowy:"

    elif "Miasto:" in label["text"]:
        column = "city"
        attribute = "Miasto:"

    if column:

        response_for_updating_user = Backend_requests.request_to_update_user_data(column, value)

        if response_for_updating_user.status_code == codes.ok:
            if column == "first_name":
                Config_data.logged_in_user_info.change_user_firstname(value)
            elif column == "last_name":
                Config_data.logged_in_user_info.change_user_lastname(value)
            elif column == "email":
                Config_data.logged_in_user_info.change_user_email(value)
            elif column == "password":
                Config_data.logged_in_user_info.change_user_password(value)
            elif column == "street":
                Config_data.logged_in_user_info.change_user_street(value)
            elif column == "zip_code":
                Config_data.logged_in_user_info.change_user_zip_code(value)
            elif column == "city":
                Config_data.logged_in_user_info.change_user_city(value)

            if column == "password" and hidden_password:
                label.config(text=f"{attribute} {'*'*len(value)}")
            else:
                label.config(text=f"{attribute} {value}")
            entry.delete(0, END)

            messagebox.showinfo("Pomyślnie zaktualizowano profil użytkownika.",
                                f"Twoj profil został zaktualizowany, {Config_data.logged_in_user_info.first_name}.")

        elif response_for_updating_user.status_code == codes.bad_request:
            if "email_error" in response_for_updating_user.json():
                messagebox.showwarning("Nie udało sie zaktualizować emaila.",
                                       "Podany email jest już zarejestrowany.")
            else:
                messagebox.showwarning("Nie udało sie zaktualizować użytkownika.",
                                       "Wprowadzono niepoprawne dane do aktualizacji użytkownika.")
        else:
            messagebox.showerror("Błąd podczas aktualizacji użytkownika.",
                                 "Nie udało sie zaktualizować użytkownika, spróbuj później.")


def move_active_announcement_to_completed_announcements(user_active_announcement_object, init_user_page_frame, root):
    response_for_end_of_announcement\
        = Backend_requests.request_to_complete_the_announcement(user_active_announcement_object.announcement_id)

    if response_for_end_of_announcement.status_code == codes.ok:
        messagebox.showinfo(f"Pomyślnie zakończono ogłoszenie.",
                            f"{Config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_active_announcement_object.title}\" zostało przeniesione do zakończonych.")
        init_user_page_frame(root)

    else:
        messagebox.showerror("Błąd podczas zakańczania ogłoszenia.",
                             f"Nie udalo sie zakończyć Twojego ogłoszenia "
                             f"\"{user_active_announcement_object.title}\", spróbuj później.")


def move_completed_announcement_to_active_announcements(user_completed_announcement_object, init_user_page_frame, root):
    response_for_restore_of_announcement\
        = Backend_requests.request_to_restore_the_announcement(user_completed_announcement_object.announcement_id)

    if response_for_restore_of_announcement.status_code == codes.ok:
        messagebox.showinfo("Pomyślnie aktywowano ogłoszenie.",
                            f"{Config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_completed_announcement_object.title}\" zostało aktywowane.")
        init_user_page_frame(root)

    else:
        messagebox.showerror("Błąd podczas aktywowania ogłoszenia.",
                             f"Nie udalo sie aktywować Twojego ogłoszenia "
                             f"\"{user_completed_announcement_object.title}\", spróbuj później.")


def delete_from_completed_announcements(user_completed_announcement_object, init_user_page_frame, root):
    response_for_delete_of_announcement\
        = Backend_requests.request_to_delete_the_announcement(user_completed_announcement_object.announcement_id)

    if response_for_delete_of_announcement.status_code == codes.ok:
        messagebox.showinfo(f"Pomyślnie usunięto ogłoszenie.",
                            f"{Config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_completed_announcement_object.title}\" zostało usunięte.")
        init_user_page_frame(root)

    else:
        messagebox.showerror("Błąd podczas usuwania ogłoszenia.",
                             f"Nie udalo sie usunąć Twojego ogłoszenia "
                             f"\"{user_completed_announcement_object.title}\", spróbuj później.")


def download_announcements(from_search_engine, page, first_init, search_engine=None, search_location=None,
                           current_var=None, categories=None):
    if from_search_engine:
        content_to_search = search_engine.get()
        location = search_location.get()
        category_id = ""
        if current_var.get() in categories["values"]:
            category_id = categories["values"].index(current_var.get()) + 1

        response_for_getting_announcements = Backend_requests.request_to_get_announcements(from_search_engine, page,
                                                                                           content_to_search, location,
                                                                                           category_id)
    else:
        response_for_getting_announcements = Backend_requests.request_to_get_announcements(from_search_engine, page)

    if response_for_getting_announcements.status_code == codes.ok:

        if response_for_getting_announcements.json()["result"]:
            list_of_objects_announcements = []
            for announcement in response_for_getting_announcements.json()["result"]:
                announcement_object = Announcement(
                    announcement["announcement_id"],
                    announcement["first_name"],
                    announcement["seller_id"],
                    announcement["name_category"],
                    announcement["category_id"],
                    announcement["title"],
                    announcement["description"],
                    announcement["price"],
                    announcement["location"],
                    announcement["main_photo"],
                    announcement["state"],
                    announcement["creation_date"],
                    announcement["mobile_number"]
                )

                if announcement_object.main_photo:
                    response_for_getting_photo = Backend_requests.request_to_get_photo(announcement_object.main_photo)
                    if response_for_getting_photo.status == codes.ok:
                        main_photo = ImageTk.PhotoImage(Image.open(response_for_getting_photo).resize((90, 67)))
                        announcement_object.main_photo = main_photo
                    else:
                        announcement_object.main_photo = None

                list_of_objects_announcements.append(announcement_object)

            return list_of_objects_announcements

        else:
            if first_init:
                messagebox.showwarning("Nie znaleźliśmy żadnych ogłoszeń.",
                                       "Przykro nam, nie znaleźliśmy wyników dla Twoich kryteriów wyszukiwania.")
            return []

    else:
        messagebox.showerror("Błąd podczas wczytywania ogłoszeń.",
                             "Nie udalo sie pobrać ogłoszeń, spróbuj ponownie później.")
        return []


def download_user_favorite_announcements(active_flag, page, per_page):
    response_for_getting_user_favorite_announcements = Backend_requests.request_to_get_user_favorite_announcements(
        active_flag, page, per_page)

    if response_for_getting_user_favorite_announcements.status_code == codes.ok:
        # Making list of fav_announcements objects
        list_of_user_fav_announcement_objects = []
        for favorite_announcement in response_for_getting_user_favorite_announcements.json()["result"]:
            user_fav_announcement_object = UserFavoriteAnnouncement(
                favorite_announcement["favorite_announcement_id"],
                favorite_announcement["announcement_id"],
                favorite_announcement["first_name"],
                favorite_announcement["seller_id"],
                favorite_announcement["title"],
                favorite_announcement["description"],
                favorite_announcement["name_category"],
                favorite_announcement["price"],
                favorite_announcement["location"],
                favorite_announcement["main_photo"],
                favorite_announcement["state"],
                favorite_announcement["creation_date"],
                favorite_announcement["mobile_number"]
            )

            if user_fav_announcement_object.main_photo:
                response_for_getting_photo = Backend_requests.request_to_get_photo(user_fav_announcement_object.
                                                                                   main_photo)
                if response_for_getting_photo.status == codes.ok:
                    main_photo = ImageTk.PhotoImage(Image.open(response_for_getting_photo).resize((90, 67)))
                    user_fav_announcement_object.main_photo = main_photo
                else:
                    user_fav_announcement_object.main_photo = None

            list_of_user_fav_announcement_objects.append(user_fav_announcement_object)

        return list_of_user_fav_announcement_objects

    else:
        messagebox.showerror("Błąd podczas wczytywania ulubionych ogłoszeń.",
                             "Nie udalo sie wczytać ulubionych ogłoszeń, spróbuj później.")
        return []


def add_announcement_to_favorite(announcement_object):
    if Config_data.is_user_logged_in:
        response_for_adding_to_favorite\
            = Backend_requests.request_to_add_announcement_to_favorite(announcement_object.announcement_id)

        if response_for_adding_to_favorite.status_code == codes.created:
            messagebox.showinfo("Pomyślnie dodano do ulubionych.",
                                f"Ogłoszenie \"{announcement_object.title}\" zostało dodane do ulubionych.")
        elif response_for_adding_to_favorite.status_code == codes.bad_request:
            messagebox.showwarning(
                f"{Config_data.logged_in_user_info.first_name}, wybrane ogłoszenie znajduję sie już w ulubionych.",
                f"Ogłoszenie \"{announcement_object.title}\" znajduje się na Twojej liście ulubionych.")
        else:
            messagebox.showerror("Błąd podczas dodawania do ulubionych.",
                                 "Nie udalo sie dodać do ulubionych, spróbuj później.")

    else:
        messagebox.showwarning("Nie jesteś zalogowany.",
                               "Aby dodać ogłoszenie do ulubionych musisz sie zalogować.")


def delete_announcement_from_favorite(user_fav_announcement_object, init_favorite_page_frame, root):
    response_for_deleting_announcement_from_favorite\
        = Backend_requests.request_to_delete_announcement_from_favorite(user_fav_announcement_object.
                                                                        favorite_announcement_id)

    if response_for_deleting_announcement_from_favorite.status_code == codes.ok:
        messagebox.showinfo("Pomyślnie usunięto z ulubionych.",
                            f"Ogłoszenie \"{user_fav_announcement_object.title}\" zostało usunięte z ulubionych.")
        init_favorite_page_frame(root)

    else:
        messagebox.showerror("Błąd podczas usuwania z ulubionych.",
                             "Nie udalo sie usunąć z ulubionych.")


def download_messages(announcement_object=None, conversation_object=None):
    if conversation_object:
        response_for_getting_messages\
            = Backend_requests.request_to_get_messages(conversation_id=conversation_object.conversation_id)
    else:
        response_for_getting_messages\
            = Backend_requests.request_to_get_messages(announcement_id=announcement_object.announcement_id)
    if response_for_getting_messages.status_code == codes.ok:
        list_of_messages_objects = []
        for message in response_for_getting_messages.json()["result"]:
            message_object = Message(
                message["conversation_id"],
                message["message_id"],
                message["customer_flag"],
                message["content"],
                message["post_date"],
                message["user_id"],
                message["first_name"]
            )
            list_of_messages_objects.append(message_object)

        return list_of_messages_objects

    else:
        messagebox.showerror("Błąd podczas wczytywania wiadomości.",
                             "Nie udalo sie wczytać wiadomości, spróbuj później.")
        return []


def send_message(list_of_message_objects, message_entry, refresh_messages, is_user_customer, announcement_object=None):
    if message_entry.get() != "":
        if message_entry.get() != "Napisz wiadomość...":

            if list_of_message_objects:
                conversation_id = list_of_message_objects[0].conversation_id
                response_for_sending_message = Backend_requests.request_to_send_message(message_entry.get(),
                                                                                        is_user_customer,
                                                                                        conversation_id=conversation_id)

            else:
                announcement_id = announcement_object.announcement_id
                response_for_sending_message = Backend_requests.request_to_send_message(message_entry.get(),
                                                                                        is_user_customer,
                                                                                        announcement_id=announcement_id)

            if response_for_sending_message.status_code == codes.created:
                message_entry.delete(0, END)
                refresh_messages()

            else:
                messagebox.showerror("Błąd podczas wysyłania wiadomości.",
                                     "Nie udalo sie wysłać wiadomości, spróbuj później.")

        else:
            messagebox.showwarning("Błądna wiadomość.", "Aby wysłać, najpierw napisz wiadomość.")
    else:
        messagebox.showwarning("Błędna wiadomość.", "Nie możesz wysłać pustej wiadomości.")


def download_conversations(customer_flag, page):
    response_for_getting_conversations = Backend_requests.request_to_get_conversations(customer_flag, page)
    if response_for_getting_conversations.status_code == codes.ok:
        list_of_conversations = []
        for conversation in response_for_getting_conversations.json()["result"]:
            conv_object = Conversation(
                conversation["conversation_id"],
                conversation["announcement_id"],
                conversation["title"],
                conversation["first_name"]
            )
            list_of_conversations.append(conv_object)

        return list_of_conversations

    else:
        messagebox.showerror("Błąd podczas wczytywania konwersacji.",
                             "Nie udalo sie wczytać konwersacji, spróbuj później.")
        return []


def download_photos_to_announcement(announcement_id, to_edit, px, py):
    list_of_photos = []
    error_with_getting_photos = False

    response_for_getting_paths_to_main_photo = Backend_requests.request_to_get_media_paths(announcement_id, 1)
    if response_for_getting_paths_to_main_photo.status_code == codes.ok:
        for dictionary in response_for_getting_paths_to_main_photo.json()["result"]:
            response_for_getting_main_photo = Backend_requests.request_to_get_photo(dictionary["path"])
            if response_for_getting_main_photo.status == codes.ok:
                photo = ImageTk.PhotoImage(Image.open(response_for_getting_main_photo).resize((px, py)))
                if to_edit:
                    list_of_photos.append((photo, dictionary["path"], 1))
                else:
                    list_of_photos.append(photo)
            else:
                error_with_getting_photos = True
    else:
        error_with_getting_photos = True

    response_for_getting_paths_to_photos = Backend_requests.request_to_get_media_paths(announcement_id, 0)
    if response_for_getting_paths_to_photos.status_code == codes.ok:
        for dictionary in response_for_getting_paths_to_photos.json()["result"]:
            response_for_getting_photos = Backend_requests.request_to_get_photo(dictionary["path"])
            if response_for_getting_photos.status == codes.ok:
                photo = ImageTk.PhotoImage(Image.open(response_for_getting_photos).resize((px, py)))
                if to_edit:
                    list_of_photos.append((photo, dictionary["path"], 0))
                else:
                    list_of_photos.append(photo)
            else:
                error_with_getting_photos = True
    else:
        error_with_getting_photos = True

    if error_with_getting_photos:
        messagebox.showerror("Błąd podczas wczytywania zdjęć.",
                             "Nie udalo sie wczytać zdjęć lub ich części, spróbuj później.")

    return list_of_photos, error_with_getting_photos


def loading_images():
    try:
        Config_data.images["arrows"] = [ImageTk.PhotoImage(Image.open("Photos/left.png").resize((50, 50))),
                                        ImageTk.PhotoImage(Image.open("Photos/right.png").resize((50, 50)))]
        Config_data.images["camera_icon"] = ImageTk.PhotoImage(Image.open("Photos/camera_icon.png").resize((50, 50)))
    except FileNotFoundError:
        messagebox.showerror("Błąd podczas wczytywania statycznych plików graficznych.",
                             "Nie udało się wczytać statycznych plików graficznych.")
        Config_data.images["arrows"] = [None, None]
        Config_data.images["camera_icon"] = None


def config_buttons(actual_page, button_previous, button_next, collection, function, list_of_objects, objects_on_page):
    if 1 < actual_page:
        button_previous.config(command=lambda: function(actual_page - 1, list_of_objects))
    else:
        button_previous.config(command=lambda: None)

    if len(collection) == objects_on_page:
        button_next.config(command=lambda: function(actual_page + 1, list_of_objects))
    else:
        button_next.config(command=lambda: None)


def create_buttons(page, x1, x2):
    button_previous = Button(page, text="Poprzednia", font=("Arial", 8), borderwidth=0, bg="#D3D3D3")
    button_previous.place(x=x1, y=600, width=60, height=32)
    button_next = Button(page, text="Następna", font=("Arial", 8), borderwidth=0, bg="#D3D3D3")
    button_next.place(x=x2, y=600, width=60, height=32)
    return button_previous, button_next


def select_photo(list_of_photo_button_objects, page, deleted_photos=None):
    filename = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("Pliki PNG", "*.png"),
                                                                           ("Pliki JPG", "*.jpg")))
    if filename:
        try:
            photo = ImageTk.PhotoImage(Image.open(filename).resize((115, 75)))
        except FileNotFoundError:
            messagebox.showwarning("Błąd podczas otwierania pliku.",
                                   "Plik który chcesz otworzyć nie istnieje.")
            return
        else:
            available_image_button = False
            for button_object in list_of_photo_button_objects:
                if not button_object.photo_to_upload:
                    available_image_button = True
                    button_object.button.config(image=photo, state="normal")
                    button_object.photo_to_display = photo
                    button_object.photo_to_upload = filename

                    delete_button = Button(page, text="Usuń zdjęcie", font=("Arial", 8), borderwidth=0, bg="#D3D3D3",
                                           command=lambda: delete_photo(button_object, deleted_photos))
                    delete_button.place(x=button_object.position_x+25, y=button_object.position_y+75)
                    button_object.button_delete = delete_button

                    break

            if not available_image_button:
                messagebox.showwarning("Brak możliwości dodania kolejnego zdjęcia.",
                                       "Twój limit dodanych zdjęć został osiągnięty.")


def delete_photo(button_object, deleted_photos):
    if isinstance(deleted_photos, list):
        if button_object.photo_from_main:
            button_object.photo_from_main = False
            deleted_photos.append((button_object.photo_to_upload, 1))
        elif button_object.photo_from_media:
            deleted_photos.append((button_object.photo_to_upload, 0))
            button_object.photo_from_media = False

    button_object.button.config(image=Config_data.images["camera_icon"], state="disabled")
    button_object.photo_to_display = None
    button_object.photo_to_upload = None
    if button_object.main_photo == 1:
        button_object.main_photo = 0
        button_object.button.config(borderwidth=0)

    if button_object.button_delete:
        button_object.button_delete.destroy()
        button_object.button_delete = None


def set_main_photo(selected_button_object, list_of_photo_button_objects):
    for button_object in list_of_photo_button_objects:
        if button_object.main_photo == 1:
            button_object.main_photo = 0
            button_object.button.config(borderwidth=0)
    selected_button_object.main_photo = 1
    selected_button_object.button.config(borderwidth=4)


def set_right(event):
    event.widget.configure(tabs=(event.width - 6, "right"))
