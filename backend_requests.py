# Import of modules needed to create http queries.
from requests import get, post, put, patch, delete, RequestException, Response
# Import global variables.
import config_data
# Import of modules needed to converting and sending image files.
from PIL import UnidentifiedImageError
from io import BytesIO, UnsupportedOperation
import os
import zipfile
from helpers import resize_image


def request_to_get_announcements(search_engine, page, content_to_search=None, location=None, category_id=None):
    """Function responsible for requests to download announcements for specific parameters."""
    # Creating url, parameters and calling GET method on this endpoint.
    try:
        url = f"{config_data.backend_url}/announcements/search"
        params = {
            "per_page": 15,
            "page": page
        }
        if search_engine:
            params["q"] = content_to_search
            params["l"] = location
            params["c"] = category_id

        response = get(url, params=params)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_login_user(login_or_email, password):
    """Function responsible for asking to download user information using a password and login or email."""
    # Creating url, request_body and calling GET method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/login"
        request_body = {
            "login_or_email": login_or_email,
            "password": password
        }
        response = get(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_register_user(first_name, last_name, email, login, password, date_of_birth, street, zip_code, city):
    """Function responsible for requesting information about a new user to be entered into the database."""
    # Creating url with request_body and calling POST method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/register"
        request_body = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "login": login,
            "password": password,
            "date_of_birth": date_of_birth,
            "street": street,
            "zip_code": zip_code,
            "city": city
        }
        response = post(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_update_the_announcement(title, description, price, location, announcement_id, state, mobile_number):
    """Function responsible for requesting an update of a user's announcement."""
    # Creating url, request_body and calling PUT method on this endpoint.
    try:
        url = f"{config_data.backend_url}/announcements/{announcement_id}"
        request_body = {
            "title": title,
            "description": description,
            "price": price,
            "location": location,
            "state": state,
            "mobile_number": mobile_number
        }
        response = put(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_get_user_announcements(active_flag, page):
    """The function responsible for downloading user's announcements when the active flag and page are specified."""
    # Creating url, parameters and calling GET method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/{config_data.logged_in_user_info.user_id}/announcements"
        params = {
            "active_flag": active_flag,
            "per_page": 4,
            "page": page
        }
        response = get(url, params=params)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_add_the_announcement(title, location, category_id, state, price, mobile_number, description):
    """Function responsible for requesting to add a new announcement."""
    # Creating url, request_body and calling POST method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/{config_data.logged_in_user_info.user_id}/announcements"
        request_body = {
            "title": title,
            "description": description,
            "price": price,
            "location": location,
            "category_id": category_id,
            "state": state,
            "mobile_number": mobile_number

        }
        response = post(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_verify_login(login):
    """Function responsible for requesting login verification."""
    # Creating url, request_body and calling GET method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/login-verification"
        request_body = {
            "login": login
        }
        response = get(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_update_user_data(column, value):
    """Function responsible for requesting update of user data, using a specific column and value."""
    # Creating url, request_body and calling PATCH method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/{config_data.logged_in_user_info.user_id}"
        request_body = {
            "column": column,
            "value": value
        }
        response = patch(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_complete_the_announcement(announcement_id):
    """Function responsible for requesting to change the user's announcement flag from active to complete."""
    # Creating url and calling PATCH method on this endpoint.
    try:
        url = f"{config_data.backend_url}/announcements/{announcement_id}/complete"
        response = patch(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_restore_the_announcement(announcement_id):
    """Function responsible for requesting to change the user's announcement flag from complete to active."""
    # Creating url and calling PATCH method on this endpoint.
    try:
        url = f"{config_data.backend_url}/announcements/{announcement_id}/restore"
        response = patch(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_delete_the_announcement(announcement_id):
    """Function responsible for requesting to change the user's announcement flag from complete to delete."""
    # Creating url and calling PATCH method on this endpoint.
    try:
        url = f"{config_data.backend_url}/announcements/{announcement_id}/delete"
        response = patch(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_get_user_favorite_announcements(active_flag, page, per_page):
    """Function responsible for requesting to download the user's favorite announcements by specifying active flag,
    page and per page params."""
    # Creating url, params and calling GET method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/{config_data.logged_in_user_info.user_id}/favorite-announcements"
        params = {
            "active_flag": active_flag,
            "page": page,
            "per_page": per_page
        }
        response = get(url, params=params)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_add_announcement_to_favorite(announcement_id):
    """Function responsible for requesting that a selected announcement be added to the user's favorites."""
    # Creating url, request_body and calling POST method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/{config_data.logged_in_user_info.user_id}/favorite-announcements"
        request_body = {
            "announcement_id": announcement_id
        }
        response = post(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_delete_announcement_from_favorite(favorite_announcement_id):
    """Function responsible for requesting removal of a selected announcement from the user's favorites."""
    # Creating url and calling DELETE method on this endpoint.
    try:
        url = f"{config_data.backend_url}/favorite-announcements/{favorite_announcement_id}"
        response = delete(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_get_messages(announcement_id=None, conversation_id=None):
    """Function responsible for requesting to download a message using the conversation id or announcement id."""
    # Creating url, request_body and calling GET method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/{config_data.logged_in_user_info.user_id}/messages"
        if conversation_id:
            request_body = {
                "conversation_id": conversation_id
            }
        else:
            request_body = {
                "announcement_id": announcement_id
            }
        response = get(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_send_message(content, is_user_customer, conversation_id=None, announcement_id=None):
    """Function responsible for requesting to send a message."""
    # Creating url, request_body and calling POST method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/{config_data.logged_in_user_info.user_id}/messages"
        if conversation_id:
            request_body = {
                "conversation_id": conversation_id,
                "content": content,
                "customer_flag": is_user_customer
            }
        else:
            request_body = {
                "announcement_id": announcement_id,
                "content": content,
                "customer_flag": is_user_customer
            }
        response = post(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_get_conversations(customer_flag, page):
    """Function responsible for requesting download of the user's conversation, specifying whether to download for
    the buyer or seller and the page."""
    # Creating url, parameters and calling GET method on this endpoint.
    try:
        url = f"{config_data.backend_url}/users/{config_data.logged_in_user_info.user_id}/conversations"
        params = {
            "customer_flag": customer_flag,
            "page": page,
            "per_page": 7
        }
        response = get(url, params=params)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_get_images(announcement_id):
    """Function responsible for requesting to download images from the server."""
    # Creating url and calling GET method on this endpoint.
    try:
        url = f"{config_data.backend_url}/announcements/{announcement_id}/media"
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
        url = f"{config_data.backend_url}/media/upload/{config_data.logged_in_user_info.user_id}"

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
        url = f"{config_data.backend_url}/media/delete/{config_data.logged_in_user_info.user_id}"

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
        url = f"{config_data.backend_url}/media/switch/{config_data.logged_in_user_info.user_id}"

        response = put(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response
