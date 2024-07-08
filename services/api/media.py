from io import BytesIO, UnsupportedOperation
import os
import zipfile
from requests import get, post, delete, put, Response, RequestException
from PIL import UnidentifiedImageError
from utils import constants, config_data
from utils.formating import resize_image


def request_to_get_images(announcement_id):
    """Function responsible for requesting to download images from the server."""
    # Creating url and calling GET method on this endpoint.
    try:
        url = f"{constants.backend_url}/media/download/announcements/{announcement_id}"
        response = get(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_upload_images(announcement_id, images):
    """Function responsible for requesting to upload photos to the server."""
    # Creating url, request_body, files and calling POST method on this endpoint.
    try:
        url = f"{constants.backend_url}/media/upload/users/{config_data.logged_in_user_info.user_id}"

        request_body = {
            "announcement_id": announcement_id
        }

        # Creating a buffer for the zip file.
        zip_buffer = BytesIO()

        # Creating a zip file with images and sending it to the server.
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Iterate over the images and add them to the zip file.
            for index, (image_path, main_photo) in enumerate(images):
                # Resize the image to 600x400 pixels.
                resized_image = resize_image(image_path, 600, 400)
                # Add the resized image to the zip file.
                zip_file.writestr(os.path.basename(image_path), resized_image.read())
                if main_photo:
                    # Add the index of the main photo to the request body.
                    request_body["main_photo_index"] = index

        # Seek to the beginning of the BytesIO buffer
        zip_buffer.seek(0)

        # Creating the files parameter for the POST request
        files = {'file': ('images.zip', zip_buffer, 'application/zip')}

        # Sending the POST request
        response = post(url, data=request_body, files=files)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    # If the file is not found, the operation is not supported, or the image is not recognized, return a 400 response.
    except (FileNotFoundError, UnsupportedOperation, UnidentifiedImageError, zipfile.BadZipFile):
        response = Response()
        response.status_code = 400
        return response

    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_delete_images(images_to_delete):
    """The function responsible for requesting the removal of a graphic files from the server and its path from
       the database."""
    # Creating url, request body and calling DELETE method on this endpoint.
    try:
        url = f"{constants.backend_url}/media/delete/users/{config_data.logged_in_user_info.user_id}"

        # Creating a list of images to delete.
        request_body = {
            "files":
                [
                    {"filename": filename,
                     "is_main_photo": is_main_photo}
                    for filename, is_main_photo in images_to_delete
                ]
        }

        response = delete(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_switch_images(request_body):
    """The function responsible for requesting swapping file paths in the database, deleting from one table,
    adding to another and vice versa."""
    # Creating url and calling PUT method on this endpoint.
    try:
        url = f"{constants.backend_url}/media/switch/users/{config_data.logged_in_user_info.user_id}"

        response = put(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response
