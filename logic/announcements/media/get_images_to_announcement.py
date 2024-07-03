import backend_requests
from tkinter import messagebox
from requests import codes
from PIL import Image, ImageTk
from io import BytesIO
import zipfile


def get_images_to_announcement(announcement_id, to_edit, px, py):
    """A function that downloads photos for a given announcement."""
    list_of_photos = []
    error_with_getting_photos = False
    main_photo_filename = None

    try:
        # Calling the function sending a request to download photos for a given announcement.
        response = backend_requests.request_to_get_images(announcement_id)
        # If the returned response has a status of 200, the program will create a list of photo objects.
        if response.status_code == codes.ok:
            # If the response contains the 'X-Main-Photo' header, the program will assign the value to the variable.
            if 'X-Main-Photo' in response.headers:
                main_photo_filename = response.headers['X-Main-Photo']

            # Create a BytesIO buffer from the response content (ZIP file).
            zip_buffer = BytesIO(response.content)

            # Open the ZIP file for reading.
            with zipfile.ZipFile(zip_buffer, 'r') as zip_file:
                # Iterate through each file in the ZIP archive.
                for file_name in zip_file.namelist():
                    # Open the file within the ZIP archive.
                    with zip_file.open(file_name) as file:
                        # Read the file content into a BytesIO object.
                        img_data = BytesIO(file.read())
                        # Open the image using PIL.
                        image = Image.open(img_data)
                        # Resize the image to the specified dimensions, maintaining aspect ratio.
                        image.thumbnail((px, py), resample=Image.LANCZOS)
                        # Convert the image to a format suitable for use with Tkinter.
                        photo = ImageTk.PhotoImage(image)
                        # If editing is enabled, append a tuple with photo, filename, and main photo flag.
                        if to_edit:
                            list_of_photos.append((photo, file_name, main_photo_filename == file_name))
                        else:
                            # Otherwise, just append the photo.
                            list_of_photos.append(photo)

        else:
            # If the response status is not OK, set error flag and show error message.
            error_with_getting_photos = True
            messagebox.showerror("Błąd podczas wczytywania zdjęć.",
                                 "Nie udało się wczytać zdjęć lub ich części, spróbuj później.")

    except (zipfile.BadZipFile, IOError, FileNotFoundError, OSError, ValueError, KeyError, EOFError):
        # If an error occurs while downloading photos, the program will display an error message.
        error_with_getting_photos = True
        messagebox.showerror("Błąd podczas wczytywania zdjęć.",
                             "Nie udało się wczytać zdjęć lub ich części, spróbuj później.")

    # Return the list of photos and the error flag.
    return list_of_photos, error_with_getting_photos
