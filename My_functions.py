from tkinter import *
from tkinter import messagebox
import mysql.connector
from re import match
from User_Class import LoggedUser, UserAnnouncement, Announcement, UserFavoriteAnnouncement, Message, Conversation
import Config_data
from Database_connection import database_connect


# User registration function
def register_user(first_name_entry, last_name_entry, email_entry, login_entry, password_entry, combobox_day_var,
                  combobox_day_birthday, combobox_month_var, combobox_month_birthday, combobox_year_var,
                  combobox_year_birthday, street_entry, zip_code_entry, city_entry):
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", first_name_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", last_name_entry.get()):
            if match(
                    "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$",
                    email_entry.get()):
                if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login_entry.get()):
                    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password_entry.get()):
                        if combobox_year_var.get() in combobox_year_birthday["values"] \
                                and combobox_month_var.get() in combobox_month_birthday["values"] \
                                and combobox_day_var.get() in combobox_day_birthday["values"]:

                            try:
                                connection = database_connect()
                                cur = connection.cursor()
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

                                query = f"""INSERT INTO users(first_name, last_name, email, login, password, 
                                            date_of_birth, street, zip_code, city, active_flag)
                                            VALUES("{first_name}","{last_name}","{email}","{login}","{password}",
                                            "{date_of_birth}","{street}","{zip_code}","{city}", True)"""

                                cur.execute(query)
                                connection.commit()
                                cur.close()
                                connection.close()

                            except mysql.connector.Error as message:
                                if "email_UNIQUE" in message.args[1]:
                                    messagebox.showerror("Nie udało sie utworzyć konta",
                                                         "Użytkownik o podanym emailu jest już zarejestowany")
                                elif "login_UNIQUE" in message.args[1]:
                                    messagebox.showerror("Nie udało sie utworzyć konta",
                                                         "Użytkownik o podanym loginie jest już zarejestowany")
                                else:
                                    messagebox.showerror("Nie udało sie utworzyć konta",
                                                         "Wystąpił błąd podczas rejestracji")

                            else:
                                messagebox.showinfo("Pomyślna rejestracja konta", "Możesz sie zalogować")
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
                        else:
                            messagebox.showerror("Wybierz date urodzenia", "Nie wybrano daty urodzenia")
                    else:
                        messagebox.showerror("Niepoprawne hasło", "Wprowadzono niepoprawne dane hasła")
                else:
                    messagebox.showerror("Niepoprawny login", "Wprowadzono niepoprawne dane loginu")
            else:
                messagebox.showerror("Niepoprawny email", "Wprowadzono niepoprawne dane email")
        else:
            messagebox.showerror("Niepoprawne nazwisko", "Wprowadzono niepoprawne dane nazwiska")
    else:
        messagebox.showerror("Niepoprawne imię", "Wprowadzono niepoprawne dane imienia")


# User login function
def login_user(entry_login_or_email, entry_password, login_window, top_panel_frame, init_shopper_page_frame, root):
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", entry_login_or_email.get()) or match(
            "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$",
            entry_login_or_email.get()):

        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", entry_password.get()):

            try:
                connection = database_connect()
                cur = connection.cursor()
                query = f"""SELECT user_id, first_name, last_name, email, login, password, date_of_birth, street, 
                            zip_code, city FROM users WHERE 
                            ((login="{entry_login_or_email.get()}" AND password="{entry_password.get()}") 
                            OR (email="{entry_login_or_email.get()}" 
                            AND password="{entry_password.get()}")) AND users.active_flag=True"""

                cur.execute(query)
                is_not_user_info_empty = cur.fetchall()
                if is_not_user_info_empty:
                    Config_data.is_user_logged_in = True
                    Config_data.logged_in_user_info = LoggedUser(is_not_user_info_empty[0][0],
                                                                 is_not_user_info_empty[0][1],
                                                                 is_not_user_info_empty[0][2],
                                                                 is_not_user_info_empty[0][3],
                                                                 is_not_user_info_empty[0][4],
                                                                 is_not_user_info_empty[0][5],
                                                                 is_not_user_info_empty[0][6],
                                                                 is_not_user_info_empty[0][7],
                                                                 is_not_user_info_empty[0][8],
                                                                 is_not_user_info_empty[0][9])

                    user_name = Config_data.logged_in_user_info.first_name
                    messagebox.showinfo("Pomyślnie zalogowano", f"Użytkownik {user_name} pomyślnie zalogowany")
                    logout_button = Button(top_panel_frame, text="Wyloguj", font=("Arial", 8), borderwidth=0,
                                           bg="#D3D3D3", command=lambda: logout_user(logout_button, user_name,
                                                                                     init_shopper_page_frame, root))
                    logout_button.place(x=1196, y=60, height=18, width=56)

                    login_window.destroy()

                else:
                    messagebox.showerror("Nie ma takiego użytkownika", "Użytkownik o podanych danych nie istnieje")

                cur.close()
                connection.close()

            except mysql.connector.Error as m:
                messagebox.showerror("Nie udało sie zalogować spróbuj później",
                                     f"Nie udało sie zalogować\nKod błędu: {m}")

        else:
            messagebox.showerror("Niepoprawne hasło", "Wprowadzono niepoprawne dane hasła")
    else:
        messagebox.showerror("Niepoprawny login lub email", "Wprowadzono niepoprawne dane loginu lub emaila")


# User logout function
def logout_user(logout_button, user_name, init_shopper_page_frame, root):
    Config_data.is_user_logged_in = False
    Config_data.logged_in_user_info = None
    Config_data.user_announcements = []
    Config_data.user_favorite_announcements = []
    init_shopper_page_frame(root)
    logout_button.destroy()
    messagebox.showinfo("Pomyślnie wylogowano", f"Użytkownik {user_name} został pomyślnie wylogowany")


def change_announcement_data(list_of_entries, description_text, user_active_announcement_object, init_user_page_frame,
                             root):
    if match("^.{10,45}$", list_of_entries[0].get()) or list_of_entries[0].get() == "":
        if list_of_entries[0].get() == "":
            title = user_active_announcement_object.title
        else:
            title = list_of_entries[0].get()

        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń ]{3,45}$", list_of_entries[1].get()) or list_of_entries[1].get() == "":
            if list_of_entries[1].get() == "":
                location = user_active_announcement_object.location
            else:
                location = list_of_entries[1].get()

            if ((match("^[0-9]+$", list_of_entries[2].get()) and len(list_of_entries[2].get()) <= 7)
                    or list_of_entries[2].get() == ""):
                if list_of_entries[2].get() == "":
                    price = user_active_announcement_object.price
                else:
                    price = int(list_of_entries[2].get())

                if (len(description_text.get("1.0", "end-1c")) >= 80 and len(
                        description_text.get("1.0", "end-1c")) <= 400):
                    description = description_text.get("1.0", "end-1c")

                    try:
                        connection = database_connect()
                        cur = connection.cursor()
                        query = f"""UPDATE announcements 
                                    SET announcements.title="{title}", announcements.description="{description}",
                                    announcements.price={price}, announcements.location="{location}"
                                    WHERE announcements.announcement_id=
                                    {user_active_announcement_object.announcement_id} """

                        cur.execute(query)
                        connection.commit()
                        cur.close()
                        connection.close()

                    except mysql.connector.Error as m:
                        messagebox.showerror("Nie udało sie zaktualizować ogłoszenia spróbuj później",
                                             f"Kod błędu: {m}")

                    else:
                        messagebox.showinfo(
                            f"Pomyślnie zaktualizowano twoje ogłoszenie, {Config_data.logged_in_user_info.first_name}",
                            f"Twoje ogłoszenie \"{title}\" zostało zaktualizowane!")
                        init_user_page_frame(root)

                else:
                    messagebox.showwarning("Błędny opis ogłoszenia",
                                           "Długość opisu ogłoszenia powinna zawierać od 80 do 400 znaków")
            else:
                messagebox.showwarning("Błędna cena",
                                       "Cena powinna zawierać tylko cyfry od 0 do 9 oraz maksymalna"
                                       " kwota ogłoszenia to 9 999 999")

        else:
            messagebox.showwarning("Błędna lokalizacja",
                                   "Długość lokalizacji powinna zawierać od 3 do 45 znaków, podaj jedynie miasto lub "
                                   "miejscowość")
    else:
        messagebox.showwarning("Błędny tytuł ogłoszenia", "Tytuł ogłoszenia powinien zawierać od 10 do 45 znaków")


def download_user_announcements():
    try:
        connection = database_connect()
        cur = connection.cursor()
        query = f""" SELECT announcements.announcement_id, users.first_name, 
                     announcements.seller_id, categories.name_category,  
                     announcements.category_id, announcements.title,
                     announcements.description, announcements.price, announcements.location,
                     announcements.active_flag
                     FROM announcements 
                     JOIN categories ON announcements.category_id=categories.category_id
                     JOIN users ON announcements.seller_id=users.user_id
                     WHERE announcements.seller_id={Config_data.logged_in_user_info.user_id} 
                     AND (announcements.active_flag=True OR announcements.completed_flag=True)
                     ORDER BY announcements.announcement_id DESC
                     LIMIT 16"""
        cur.execute(query)
        list_of_user_announcements = cur.fetchall()
        cur.close()
        connection.close()

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas wczytywania ogłoszeń",
                             f"Nie udalo sie wczytać Twoich ogłoszeń, spróbuj później\nKod błędu: {m}")

    else:
        list_of_objects_user_announcements = []
        for (announcement_id, first_name, seller_id, name_category, category_id, title, description, price, location,
             active_flag) in list_of_user_announcements:
            user_announcement_object = UserAnnouncement(announcement_id, first_name, seller_id, name_category,
                                                        category_id, title, description, price, location, active_flag)
            list_of_objects_user_announcements.append(user_announcement_object)

        Config_data.user_announcements = list_of_objects_user_announcements


def add_announcement(title_entry, location_entry, current_var_category, price_entry, description_text,
                     select_categories):
    if match("^.{10,45}$", title_entry.get()):
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń ]{3,45}$", location_entry.get()):
            if current_var_category.get() != "" and current_var_category.get() in select_categories["values"]:
                if match("^[0-9]+$", price_entry.get()) and len(price_entry.get()) <= 7:
                    if len(description_text.get("1.0", "end-1c")) >= 80 and len(
                            description_text.get("1.0", "end-1c")) <= 400:

                        title = title_entry.get()
                        location = location_entry.get()
                        category_id = select_categories["values"].index(current_var_category.get()) + 1
                        price = int(price_entry.get())
                        description = description_text.get("1.0", "end-1c")

                        try:
                            connection = database_connect()
                            cur = connection.cursor()
                            query = f"""INSERT INTO announcements(seller_id, category_id, title, description, price,
                                        location, active_flag, completed_flag, deleted_flag)
                                        VALUES({Config_data.logged_in_user_info.user_id}, {category_id}, "{title}",
                                         "{description}", {price}, "{location}", True, False, False)"""
                            cur.execute(query)
                            connection.commit()
                            cur.close()
                            connection.close()

                        except mysql.connector.Error as m:
                            messagebox.showerror("Nie udało sie dodać ogłoszenia spróbuj później", f"Kod błędu: {m}")

                        else:
                            title_entry.delete(0, END)
                            location_entry.delete(0, END)
                            price_entry.delete(0, END)
                            description_text.delete("1.0", END)
                            current_var_category.set("")
                            messagebox.showinfo("Pomyślnie dodano ogłoszenie",
                                                f"Twoje ogłoszenie \"{title}\" zostało dodane, możesz dodać kolejne "
                                                f"ogłoszenia")

                    else:
                        messagebox.showwarning("Błędny opis ogłoszenia",
                                               "Długość opisu ogłoszenia powinna zawierać od 80 do 400 znaków")
                else:
                    messagebox.showwarning("Błędna cena",
                                           "Cena powinna zawierać tylko cyfry od 0 do 9 oraz maksymalna"
                                           " kwota ogłoszenia to 9 999 999")
            else:
                messagebox.showwarning("Błędna kategoria", "Nie wybrano kategorii produktu")
        else:
            messagebox.showwarning("Błędna lokalizacja",
                                   "Długość lokalizacji powinna zawierać od 3 do 45 znaków, podaj jedynie miasto lub "
                                   "miejscowość")
    else:
        messagebox.showwarning("Błędny tytuł ogłoszenia", "Tytuł ogłoszenia powinien zawierać od 10 do 45 znaków")


def verify_login(login_entry):
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9]{5,45}$", login_entry.get()):
        try:
            connection = database_connect()
            cur = connection.cursor()
            query = f"""SELECT user_id FROM users WHERE login="{login_entry.get()}" """

            cur.execute(query)
            login_used = cur.fetchall()
            if login_used:
                messagebox.showinfo("Podany login jest już zajęty",
                                    f"Istnieje już zarejestrowany użytkownik o loginie {login_entry.get()}")

            else:
                messagebox.showinfo("Podany login jest dostępny",
                                    f"Nie istnieje jeszcze użytkownik o loginie {login_entry.get()}")

            cur.close()
            connection.close()

        except mysql.connector.Error:
            pass
    else:
        messagebox.showinfo("Niepoprawny login", "Nie możesz użyć tego loginu do rejestracji\nSprawdź wzór loginu")


def verify_password(password_entry):
    if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", password_entry.get()):
        messagebox.showinfo("Poprawne hasło", "Możesz użyć tego hasła do rejestracji")
    else:
        messagebox.showinfo("Niepoprawne hasło", "Nie możesz użyć tego hasła do rejestracji\nSprawdź wzór hasła")


def show_pattern(arg):
    if arg == "Wzór loginu":
        messagebox.showinfo("Wymogi dotyczące loginu",
                            "- musi zawierać minimum 5 znaków\n- może zawierać wielkie oraz małe litery\n- może "
                            "zawierać cyfry\n- nie może zawierać znaków specjalnych")
    elif arg == "Wzór hasła":
        messagebox.showinfo("Wymogi dotyczące hasła",
                            "- musi zawierać minimum 7 znaków\n- może zawierać wielkie oraz małe litery\n- może "
                            "zawierać cyfry\n- może zawierać znaki specjalne")


def delete_text(entry_object):
    entry_object.delete(0, END)
    entry_object.unbind("<Button-1>")


def change_user_info(entry, label):
    column = None
    attribute = None
    if "Imie:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", entry.get()):
            column = "first_name"
            attribute = "Imie:"
        else:
            messagebox.showerror("Niepoprawne imię", "Wprowadzono niepoprawne dane imienia")

    elif "Nazwisko:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń]{2,45}$", entry.get()):
            column = "last_name"
            attribute = "Nazwisko:"
        else:
            messagebox.showerror("Niepoprawne nazwisko", "Wprowadzono niepoprawne dane nazwiska")

    elif "Email:" in label["text"]:
        if match(
                "^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9._-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9._-]+[A-Za-z0-9])\.[A-Za-z0-9]+$",
                entry.get()):
            column = "email"
            attribute = "Email:"
        else:
            messagebox.showerror("Niepoprawny email", "Wprowadzono niepoprawne dane email")

    elif "Hasło:" in label["text"]:
        if match("^[A-ZĘÓĄŚŁŻŹĆŃa-zęóąśłżźćń0-9!@#$%^&*]{7,45}$", entry.get()):
            column = "password"
            attribute = "Hasło:"
        else:
            messagebox.showerror("Niepoprawne hasło", "Wprowadzono niepoprawne dane hasła")

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
        try:
            connection = database_connect()
            cur = connection.cursor()
            query = f"""UPDATE users SET {column}="{entry.get()}"
                        WHERE user_id={Config_data.logged_in_user_info.user_id} """
            cur.execute(query)
            connection.commit()

            cur.close()
            connection.close()

        except mysql.connector.Error as m:
            if "email_UNIQUE" in m.args[1]:
                messagebox.showerror("Nie udało sie zaktualizować emaila",
                                     "Podany email jest już zarejestrowany")
            else:
                messagebox.showerror(f"Kod błędu: {m}", "Nie udało sie zaktualizować, spróbuj później")

        else:
            if column == "first_name":
                Config_data.logged_in_user_info.change_user_firstname(entry.get())
            elif column == "last_name":
                Config_data.logged_in_user_info.change_user_lastname(entry.get())
            elif column == "email":
                Config_data.logged_in_user_info.change_user_email(entry.get())
            elif column == "password":
                Config_data.logged_in_user_info.change_user_password(entry.get())
            elif column == "street":
                Config_data.logged_in_user_info.change_user_street(entry.get())
            elif column == "zip_code":
                Config_data.logged_in_user_info.change_user_zip_code(entry.get())
            elif column == "city":
                Config_data.logged_in_user_info.change_user_city(entry.get())

            label.config(text=f"{attribute} {entry.get()}")
            messagebox.showinfo("Pomyślna aktualizacja",
                                f"Twoj profil został zaktualizowany, {Config_data.logged_in_user_info.first_name}")


def move_active_announcement_to_completed_announcements(user_active_announcement_object, init_user_page_frame, root):
    try:
        connection = database_connect()
        cur = connection.cursor()

        query = f"""UPDATE announcements SET completed_flag=True, active_flag=False
                    WHERE announcements.announcement_id={user_active_announcement_object.announcement_id}"""

        cur.execute(query)
        connection.commit()
        cur.close()
        connection.close()
    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas zakańczania ogłoszenia",
                             f"Nie udalo sie zakończyć Twojego ogłoszenia \"{user_active_announcement_object.title}\""
                             f", spróbuj później\nKod błędu: {m}")

    else:
        messagebox.showinfo(f"Pomyślnie zakończono ogłoszenie",
                            f"{Config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_active_announcement_object.title}\" zostało przeniesione do zakończonych")
        init_user_page_frame(root)


def move_completed_announcement_to_active_announcements(user_completed_announcement_object, init_user_page_frame, root):
    try:
        connection = database_connect()
        cur = connection.cursor()
        query = f"""UPDATE announcements SET active_flag=True, completed_flag=False
                    WHERE announcements.announcement_id={user_completed_announcement_object.announcement_id}"""

        cur.execute(query)
        connection.commit()
        cur.close()
        connection.close()

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas aktywowania ogłoszenia",
                             f"Nie udalo sie aktywować Twojego ogłoszenia "
                             f"\"{user_completed_announcement_object.title}\", spróbuj później\nKod błędu: {m}")

    else:
        messagebox.showinfo(f"Pomyślnie Aktywowano ogłoszenie",
                            f"{Config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_completed_announcement_object.title}\" zostało aktywowane")
        init_user_page_frame(root)


def delete_from_completed_announcements(user_completed_announcement_object, init_user_page_frame, root):
    try:
        connection = database_connect()
        cur = connection.cursor()
        query = f"""UPDATE announcements SET deleted_flag=True, completed_flag=False
                    WHERE announcements.announcement_id={user_completed_announcement_object.announcement_id}"""

        cur.execute(query)
        connection.commit()
        cur.close()
        connection.close()

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas usuwania ogłoszenia",
                             f"Nie udalo sie usunąć Twojego ogłoszenia "
                             f"\"{user_completed_announcement_object.title}\", spróbuj później\nKod błędu: {m}")

    else:
        messagebox.showinfo(f"Pomyślnie usunięto ogłoszenie",
                            f"{Config_data.logged_in_user_info.first_name}, Twoje ogłoszenie "
                            f"\"{user_completed_announcement_object.title}\" zostało usunięte")
        init_user_page_frame(root)


def download_all_announcements():
    try:
        connection = database_connect()
        cur = connection.cursor()
        query = f""" SELECT announcements.announcement_id, users.first_name,
                     announcements.seller_id, categories.name_category, 
                     announcements.title, announcements.description, 
                     announcements.price, announcements.location
                     FROM announcements 
                     JOIN categories ON announcements.category_id=categories.category_id
                     JOIN users ON announcements.seller_id=users.user_id
                     WHERE announcements.active_flag=True
                     ORDER BY announcements.announcement_id DESC """

        cur.execute(query)
        list_of_announcements = cur.fetchall()
        cur.close()
        connection.close()

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas wczytywania wszystkich ogłoszeń",
                             f"Nie udalo sie wczytać ogłoszeń wszystkich użytkowników\nKod błędu: {m}")

    else:
        making_list_of_pages(list_of_announcements)
        return True


def download_user_favorite_announcements():
    try:
        connection = database_connect()
        cur = connection.cursor()
        query = f"""SELECT favorite_announcements.favorite_announcement_id, announcements.announcement_id,
                    users.first_name, announcements.seller_id, announcements.title,   
                    announcements.description, categories.name_category, announcements.price,
                    announcements.location, announcements.active_flag
                    FROM favorite_announcements 
                    JOIN announcements ON favorite_announcements.announcement_id=announcements.announcement_id
                    JOIN categories ON announcements.category_id=categories.category_id
                    JOIN users ON announcements.seller_id=users.user_id
                    WHERE favorite_announcements.user_id={Config_data.logged_in_user_info.user_id} 
                    AND (announcements.active_flag=1 OR announcements.completed_flag=1)
                    ORDER BY favorite_announcements.favorite_announcement_id DESC"""

        cur.execute(query)
        list_of_favorite_announcements = cur.fetchall()
        cur.close()
        connection.close()

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas wczytywania ulubionych ogłoszeń",
                             f"Nie udalo sie wczytać ulubionych ogłoszeń\nKod błędu: {m}")

    else:
        # Making list of fav_announcements objects
        list_of_user_fav_announcement_objects = []
        for (favorite_announcement_id, announcement_id, first_name, seller_id, title, description, name_category,
             price, location, active_flag) in list_of_favorite_announcements:
            user_fav_announcement_object = UserFavoriteAnnouncement(favorite_announcement_id, announcement_id,
                                                                    first_name, seller_id, title, description,
                                                                    name_category, price, location, active_flag)
            list_of_user_fav_announcement_objects.append(user_fav_announcement_object)

        Config_data.user_favorite_announcements = list_of_user_fav_announcement_objects


def add_announcement_to_favorite(announcement_object):
    if Config_data.is_user_logged_in:
        try:
            connection = database_connect()
            cur = connection.cursor()
            query_check = f""" SELECT favorite_announcement_id FROM favorite_announcements
                               WHERE user_id={Config_data.logged_in_user_info.user_id} 
                               AND announcement_id={announcement_object.announcement_id} """

            cur.execute(query_check)
            is_liked = cur.fetchall()
            if not is_liked:
                query_add = f""" INSERT INTO favorite_announcements(user_id, announcement_id)
                                 VALUES({Config_data.logged_in_user_info.user_id},
                                 {announcement_object.announcement_id}) """
                cur.execute(query_add)
                connection.commit()
                messagebox.showinfo("Pomyślnie dodano do ulubionych",
                                    f"Ogłoszenie \"{announcement_object.title}\" zostało dodane do ulubionych")
            else:
                messagebox.showwarning(
                    f"{Config_data.logged_in_user_info.first_name}, wybrane ogłoszenie jest już polubione",
                    f"Ogłoszenie \"{announcement_object.title}\" znajduje się na Twojej liście ulubionych")
            cur.close()
            connection.close()

        except mysql.connector.Error as m:
            messagebox.showerror("Błąd podczas dodawania do ulubionych",
                                 f"Nie udalo sie dodać do ulubionych\nKod błędu: {m}")

    else:
        messagebox.showwarning("Nie jesteś zalogowany", "Aby dodać ogłoszenie do ulubionych musisz sie zalogować")


def delete_announcement_from_favorite(user_fav_announcement_object, init_favorite_page_frame, root):
    try:
        connection = database_connect()
        cur = connection.cursor()
        query = f""" DELETE FROM favorite_announcements
                     WHERE favorite_announcement_id={user_fav_announcement_object.favorite_announcement_id} """
        cur.execute(query)
        connection.commit()
        cur.close()
        connection.close()

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas usuwania z ulubionych",
                             f"Nie udalo sie usunąć z ulubionych\nKod błędu: {m}")

    else:
        messagebox.showinfo("Pomyślnie usunięto z ulubionych",
                            f"Ogłoszenie \"{user_fav_announcement_object.title}\" zostało usunięte z ulubionych")
        init_favorite_page_frame(root)


def download_from_search_engine(search_engine, search_location, current_var, categories):
    search_field = search_engine.get()
    location_filed = search_location.get()

    query = f""" SELECT announcements.announcement_id, users.first_name,
                 announcements.seller_id, categories.name_category,
                 announcements.title, announcements.description, 
                 announcements.price, announcements.location
                 FROM announcements 
                 JOIN categories ON announcements.category_id=categories.category_id
                 JOIN users ON announcements.seller_id=users.user_id
                 WHERE announcements.active_flag=True """

    # Init query for search field
    query = making_query(search_field, query, "announcements.title")
    # Init query for location field
    query = making_query(location_filed, query, "announcements.location")
    # Init query for category id
    if current_var.get() in categories["values"]:
        category_id = categories["values"].index(current_var.get()) + 1
        query += f"""AND categories.category_id={category_id} """

    query += "ORDER BY announcements.announcement_id DESC"

    try:
        connection = database_connect()
        cur = connection.cursor()
        cur.execute(query)
        list_of_searched_announcements = cur.fetchall()
        cur.close()
        connection.close()

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas wyszukiwania ogłoszeń",
                             f"Nie udalo sie wyszukać ogłoszeń\nKod błędu: {m}")

    else:
        if list_of_searched_announcements:
            making_list_of_pages(list_of_searched_announcements)
            return True
        else:
            messagebox.showwarning(
                "Znaleźliśmy 0 ogłoszeń",
                "Nie znaleźliśmy żadnych wyników dla Twoich kryteriów wyszukiwania")
            return False


def making_query(field, query, column):
    collection = []
    for element in field.split(" "):
        if element != "":
            collection.append(element)

    for i in range(len(collection)):
        if len(collection) == 1:
            query += f"""AND {column} LIKE "%{collection[i]}%" """
        else:
            if i == 0:
                query += f"""AND ({column} LIKE "%{collection[i]}%" """
            elif i < (len(collection) - 1):
                query += f"""OR {column} LIKE "%{collection[i]}%" """
            else:
                query += f"""OR {column} LIKE "%{collection[i]}%") """
    return query


def making_list_of_pages(list_of_announcements):
    # Making list of announcements objects
    list_of_objects_announcements = []
    for (announcement_id, first_name, seller_id, name_category, title, description, price,
         location) in list_of_announcements:
        announcement_object = Announcement(announcement_id, first_name, seller_id, name_category, title,
                                           description, price, location)
        list_of_objects_announcements.append(announcement_object)

    # Grouping list of announcements by announcements on page
    full_pages = len(list_of_objects_announcements) // 15
    object_of_last_page = len(list_of_objects_announcements) % 15
    list_of_objects_announcements_grouped_by_page = []
    for i in range(full_pages):
        tmp2 = []
        for j in range(15):
            index = i * 15 + j
            tmp2.append(list_of_objects_announcements[index])

        list_of_objects_announcements_grouped_by_page.append(tmp2)

    if object_of_last_page > 0:
        tmp3 = []
        for k in range((15 * full_pages), (15 * full_pages + object_of_last_page)):
            tmp3.append(list_of_objects_announcements[k])

        list_of_objects_announcements_grouped_by_page.append(tmp3)

    Config_data.all_announcements = list_of_objects_announcements_grouped_by_page


def download_messages(announcement_object):
    try:
        connection = database_connect()
        cur = connection.cursor()
        query_check = f"""SELECT conversation_id FROM conversations
                          WHERE conversations.announcement_id={announcement_object.announcement_id}
                          AND conversations.user_id={Config_data.logged_in_user_info.user_id}"""
        cur.execute(query_check)
        is_conversation_exists = cur.fetchall()
        if is_conversation_exists:
            query_download = f"""SELECT messages.conversation_id, messages.message_id,
                                 messages.customer_flag, messages.content, DATE(date) as date,
                                 TIME(date) as time, messages.user_id, users.first_name
                                 FROM messages
                                 JOIN users ON messages.user_id=users.user_id
                                 WHERE messages.conversation_id={is_conversation_exists[0][0]}
                                 ORDER BY messages.message_id DESC"""

            cur.execute(query_download)
            list_of_messages = cur.fetchall()
            list_of_messages_objects = []
            for conv_id, mess_id, customer_flag, content, date, time, user_id, first_name in list_of_messages:
                message_object = Message(conv_id, mess_id, customer_flag, content, date, time, user_id, first_name)
                list_of_messages_objects.append(message_object)

        else:
            list_of_messages_objects = []

        cur.close()
        connection.close()

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas wczytywania wiadomości",
                             f"Nie udalo sie wczytać wiadomości\nKod błędu: {m}")

    else:
        return list_of_messages_objects


def send_message(list_of_message_objects, message_entry, refresh_messages, is_user_customer, announcement_object=None):
    if message_entry.get() != "":
        if message_entry.get() != "Napisz wiadomość...":
            try:
                connection = database_connect()
                cur = connection.cursor()
                if list_of_message_objects:
                    query = f"""INSERT INTO messages(conversation_id, user_id, customer_flag, content, date)
                            VALUES({list_of_message_objects[0].conversation_id}, 
                            {Config_data.logged_in_user_info.user_id}, {is_user_customer},
                            "{message_entry.get()}", now())"""
                    cur.execute(query)
                    connection.commit()

                else:
                    query_make_conv = f"""INSERT INTO conversations(announcement_id, user_id)
                                          VALUES({announcement_object.announcement_id}, 
                                {Config_data.logged_in_user_info.user_id})"""
                    cur.execute(query_make_conv)
                    query_check_conv_id = f"""SELECT conversation_id FROM conversations
                                              WHERE conversations.announcement_id={announcement_object.announcement_id}
                                              AND conversations.user_id={Config_data.logged_in_user_info.user_id}"""
                    cur.execute(query_check_conv_id)
                    conversation_id = cur.fetchall()
                    query_add_message = f"""INSERT INTO messages(conversation_id, user_id, customer_flag, content, date)
                                            VALUES({conversation_id[0][0]}, {Config_data.logged_in_user_info.user_id},
                                            True, "{message_entry.get()}", now())"""
                    cur.execute(query_add_message)
                    connection.commit()
                connection.close()
                cur.close()

            except mysql.connector.Error as m:
                messagebox.showerror("Błąd podczas wysyłania wiadomości",
                                     f"Nie udalo sie wysłać wiadomości\nKod błędu: {m}")
            else:
                message_entry.delete(0, END)
                refresh_messages()
        else:
            messagebox.showwarning("Błąd wiadomości", "Aby wysłać, najpierw napisz wiadomość")
    else:
        messagebox.showwarning("Błąd wiadomości", "Aby wysłać, najpierw napisz wiadomość")


def download_conversations():
    try:
        connection = database_connect()
        cur = connection.cursor()
        query_download_conversations_as_customer = f"""SELECT conversations.conversation_id, 
                                                       conversations.announcement_id, announcements.title,
                                                       users.first_name FROM conversations 
                                                       JOIN announcements ON conversations.announcement_id=
                                                       announcements.announcement_id
                                                       JOIN users ON announcements.seller_id=users.user_id
                                                       WHERE conversations.user_id=
                                                       {Config_data.logged_in_user_info.user_id}"""
        cur.execute(query_download_conversations_as_customer)
        list_of_conversations_as_customer = cur.fetchall()
        if list_of_conversations_as_customer:
            list_of_conversations_as_customer_objects = []
            for conv_id, ann_id, title, seller_name in list_of_conversations_as_customer:
                conv_object = Conversation(conv_id, ann_id, title, seller_name)
                list_of_conversations_as_customer_objects.append(conv_object)
        else:
            list_of_conversations_as_customer_objects = []

        query_download_conversations_as_seller = f"""SELECT conversations.conversation_id, 
                                                     conversations.announcement_id, announcements.title,
                                                     users.first_name FROM conversations
                                                     JOIN announcements ON conversations.announcement_id=
                                                     announcements.announcement_id
                                                     JOIN users ON conversations.user_id=users.user_id
                                                     WHERE announcements.seller_id=
                                                     {Config_data.logged_in_user_info.user_id}"""
        cur.execute(query_download_conversations_as_seller)
        list_of_conversations_as_seller = cur.fetchall()
        if list_of_conversations_as_seller:
            list_of_conversations_as_seller_objects = []
            for conv_id, ann_id, title, customer_name in list_of_conversations_as_seller:
                conv_object = Conversation(conv_id, ann_id, title, customer_name)
                list_of_conversations_as_seller_objects.append(conv_object)
        else:
            list_of_conversations_as_seller_objects = []

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas wczytywania konwersacji",
                             f"Nie udalo sie wczytać konwersacji\nKod błędu: {m}")

    else:
        return list_of_conversations_as_customer_objects, list_of_conversations_as_seller_objects


def download_messages_from_conv_object(conversation_object):
    try:
        connection = database_connect()
        cur = connection.cursor()
        query = f"""SELECT messages.conversation_id, messages.message_id,
                    messages.customer_flag, messages.content, DATE(date) as date,
                    TIME(date) as time, messages.user_id, users.first_name
                    FROM messages
                    JOIN users ON messages.user_id=users.user_id
                    WHERE messages.conversation_id={conversation_object.conversation_id}
                    ORDER BY messages.message_id DESC"""
        cur.execute(query)
        list_of_messages = cur.fetchall()
        list_of_messages_objects = []
        for conv_id, mess_id, customer_flag, content, date, time, user_id, first_name in list_of_messages:
            message_object = Message(conv_id, mess_id, customer_flag, content, date, time, user_id, first_name)
            list_of_messages_objects.append(message_object)

        cur.close()
        connection.close()

    except mysql.connector.Error as m:
        messagebox.showerror("Błąd podczas wczytywania wiadomości",
                             f"Nie udalo sie wczytać wiadomości\nKod błędu: {m}")
    else:
        return list_of_messages_objects
