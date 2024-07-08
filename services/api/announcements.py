from utils import constants, config_data
from requests import get, post, patch, delete, put, Response, RequestException


def request_to_get_announcements(search_engine, page, content_to_search=None, location=None, category_id=None):
    """Function responsible for requests to download announcements for specific parameters."""
    # Creating url, parameters and calling GET method on this endpoint.
    try:
        url = f"{constants.backend_url}/announcements/search"
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


def request_to_update_the_announcement(title, description, price, location, announcement_id, state, mobile_number):
    """Function responsible for requesting an update of a user's announcement."""
    # Creating url, request_body and calling PUT method on this endpoint.
    try:
        url = f"{constants.backend_url}/announcements/{announcement_id}"
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
        url = f"{constants.backend_url}/announcements/users/{config_data.logged_in_user_info.user_id}"
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
        url = f"{constants.backend_url}/announcements/users/{config_data.logged_in_user_info.user_id}"
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


def request_to_complete_the_announcement(announcement_id):
    """Function responsible for requesting to change the user's announcement flag from active to complete."""
    # Creating url and calling PATCH method on this endpoint.
    try:
        url = f"{constants.backend_url}/announcements/{announcement_id}/complete"
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
        url = f"{constants.backend_url}/announcements/{announcement_id}/restore"
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
        url = f"{constants.backend_url}/announcements/{announcement_id}/delete"
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
        url = f"{constants.backend_url}/favorite-announcements/users/{config_data.logged_in_user_info.user_id}"
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
    """Function responsible for requesting that a selected announcement be added to the user's favorites_management."""
    # Creating url, request_body and calling POST method on this endpoint.
    try:
        url = f"{constants.backend_url}/favorite-announcements/users/{config_data.logged_in_user_info.user_id}"
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
    """Function responsible for requesting removal of a selected announcement from the user's favorites_management."""
    # Creating url and calling DELETE method on this endpoint.
    try:
        url = f"{constants.backend_url}/favorite-announcements/{favorite_announcement_id}"
        response = delete(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # When the request is successful, return a response from the function.
    else:
        return response
