import os
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from tkinter import Button
from logic.announcements.media.delete_image import delete_image


def select_image(list_of_photo_button_objects, page):
    """The function responsible for selecting a graphic file from the user's computer, displaying it and assigning
    appropriate values to the PhotoButton object."""
    # Assigning the path of the file that was selected by the user. The program allows you to select JPG files.
    filename = filedialog.askopenfilename(
        title="Wybierz plik",
        filetypes=(
            ("Pliki graficzne", "*.jpg;*.jpeg;*.png;"),
            ("Pliki JPG", "*.jpg"),
            ("Pliki JPEG", "*.jpeg"),
            ("Pliki PNG", "*.png")
        )
    )

    # If the user selects a file, the program will try to open it and assign it to a variable.
    if filename:
        # Checking whether the selected file is not larger than 10MB.
        if os.path.getsize(filename) > 10 * 1024 * 1024:
            messagebox.showwarning("Zbyt duży plik.", "Plik który chcesz dodać jest zbyt duży,"
                                                      " maksymalny rozmiar pliku to 10MB.")
            return

        try:
            # Opening and converting the selected file.
            image = Image.open(filename)
            image.thumbnail((115, 75), resample=Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

        # If such a file is missing, an error will be displayed and the function will terminate.
        except FileNotFoundError:
            messagebox.showwarning("Błąd podczas otwierania pliku.",
                                   "Plik który chcesz otworzyć nie istnieje.")
            return

        # If the file is opened and assigned correctly, the program will check whether it can add a photo to the
        # PhotoButton object.
        else:
            available_image_button = False
            for button_object in list_of_photo_button_objects:
                if not button_object.photo_to_upload:
                    available_image_button = True
                    button_object.button.config(image=photo, state="normal")
                    button_object.photo_to_display = photo
                    button_object.photo_to_upload = filename
                    # Creating a button object for deleting a photo with parameters of the PhotoButton object and
                    # deleted_photos.
                    delete_button = Button(page, text="Usuń zdjęcie", font=("Arial", 8), borderwidth=0, bg="#D3D3D3",
                                           command=lambda: delete_image(button_object))
                    delete_button.place(x=button_object.position_x+25, y=button_object.position_y+75)
                    button_object.button_delete = delete_button

                    # Loop break.
                    break

            # If the loop did not find any free buttons, an appropriate message will be displayed.
            if not available_image_button:
                messagebox.showwarning("Brak możliwości dodania kolejnego zdjęcia.",
                                       "Twój limit dodanych zdjęć został osiągnięty.")
