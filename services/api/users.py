from utils import constants, config_data
from requests import get, post, patch, Response, RequestException


def request_to_login_user(login_or_email, password):
    """Function responsible for asking to download user information using a password and login or email."""
    # Creating url, request_body and calling GET method on this endpoint.
    try:
        url = f"{constants.backend_url}/users/login"
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
        url = f"{constants.backend_url}/users/register"
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


def request_to_verify_login(login):
    """Function responsible for requesting login verification."""
    # Creating url, request_body and calling GET method on this endpoint.
    try:
        url = f"{constants.backend_url}/users/login-verification"
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
        url = f"{constants.backend_url}/users/{config_data.logged_in_user_info.user_id}"
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
