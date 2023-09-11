# Import of modules needed to create http queries.
import urllib3
from requests import get, post, put, patch, delete, RequestException, Response
# Import global variables.
import Config_data


def request_to_get_announcements(from_search_engine, page, content_to_search=None, location=None, category_id=None):
    """Function responsible for requests to download announcements for specific parameters."""
    # Creating url, parameters and calling GET method on this endpoint.
    try:
        url = "http://127.0.0.1:5000/announcements/search"
        params = {
            "per_page": 15,
            "page": page
        }
        if from_search_engine:
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
        url = "http://127.0.0.1:5000/users/login"
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
        url = "http://127.0.0.1:5000/users/register"
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
        url = f"http://127.0.0.1:5000/announcements/{announcement_id}"
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
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/announcements"
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
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/announcements"
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
        url = "http://127.0.0.1:5000/users/login-verification"
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
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}"
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
        url = f"http://127.0.0.1:5000/announcements/{announcement_id}/complete"
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
        url = f"http://127.0.0.1:5000/announcements/{announcement_id}/restore"
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
        url = f"http://127.0.0.1:5000/announcements/{announcement_id}/delete"
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
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/favorite-announcements"
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
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/favorite-announcements"
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
        url = f"http://127.0.0.1:5000/favorite-announcements/{favorite_announcement_id}"
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
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/messages"
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
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/messages"
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
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/conversations"
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


def request_to_get_photo(path):
    """Function responsible for requesting to download a graphic file when specifying the path."""
    # Creating url, request_body and calling GET method on this endpoint.
    try:
        url = "http://127.0.0.1:5000/media/download"
        request_body = {
            "path": path
        }
        response = get(url, json=request_body, stream=True).raw

    # If cant connect with endpoint, making HTTPResponse object with 404 status code and return response.
    except urllib3.exceptions.HTTPError:
        response = urllib3.response.HTTPResponse()
        response.status = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_get_media_paths(announcement_id, main_photo):
    """Function responsible for requesting downloading paths to graphic files for a given announcement when specifying
    announcement_id and the main_photo flag."""
    # Creating url, parameters and calling GET method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/announcements/{announcement_id}/media/paths"
        params = {
            "main_photo_flag": main_photo
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


def request_to_upload_photo(announcement_id, main_photo, photo_to_upload):
    """The function responsible for requesting the upload of a graphic file on the server and saving its path in the
    database."""
    # Creating url and parameters.
    try:
        url = f"http://127.0.0.1:5000/media/upload/{Config_data.logged_in_user_info.user_id}"
        params = {
            "announcement_id": announcement_id,
            "main_photo_flag": main_photo
        }
        # Binary opening of a file from the user's computer and assigning it as a file to be sent.
        # Execution of the request.
        with open(photo_to_upload, "rb") as file:
            files = {
                "file": file
            }
            response = post(url, params=params, files=files, stream=True).raw

    # If cant connect with endpoint, making HTTPResponse object with 404 status code and return response.
    except urllib3.exceptions.HTTPError:
        response = urllib3.response.HTTPResponse()
        response.status = 404
        return response

    # If the photo previously selected by the user is not already in the saved path, then make HTTPResponse object and
    # return it with status 404.
    except FileNotFoundError:
        response = urllib3.response.HTTPResponse()
        response.status = 404
        return response

    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_delete_photo(path, main_photo):
    """The function responsible for requesting the removal of a graphic file from the server and its path from
    the database."""
    # Creating url, parameters and calling DELETE method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/media/delete"
        params = {
            "main_photo_flag": main_photo,
            "path": path
        }
        response = delete(url, params=params)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response


def request_to_switch_photos(announcement_id, main_photo_path, media_photo_path, to_media_flag, to_main_flag):
    """The function responsible for requesting swapping file paths in the database, deleting from one table,
    adding to another and vice versa."""
    # Creating url, request_body, parameters and calling PUT method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/media/switch/{Config_data.logged_in_user_info.user_id}"
        request_body = {
            "main_photo_path": main_photo_path,
            "media_photo_path": media_photo_path,
            "announcement_id": announcement_id
        }
        params = {
            "to_media_flag": to_media_flag,
            "to_main_flag": to_main_flag
        }
        response = put(url, json=request_body, params=params)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response
