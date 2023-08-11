from requests import get, post, put, patch, delete, RequestException, Response
import Config_data


def request_to_get_announcements(from_search_engine, content_to_search=None, location=None, category_id=None):
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = "http://127.0.0.1:5000/announcements/search"
        if from_search_engine:
            params = {
                "q": content_to_search,
                "l": location,
                "c": category_id
            }
            response = get(url, params=params)
        else:
            response = get(url)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_login_user(login_or_email, password):
    # Creating endpoint and calling GET method on this endpoint.
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
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_register_user(first_name, last_name, email, login, password, date_of_birth, street, zip_code, city):
    # Creating endpoint and calling GET method on this endpoint.
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
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_update_the_announcement(title, description, price, location, announcement_id):
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/announcements/{announcement_id}"
        request_body = {
            "title": title,
            "description": description,
            "price": price,
            "location": location
        }
        response = put(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_get_user_announcements():
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/announcements"
        response = get(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_add_the_announcement(title, location, category_id, price, description):
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/announcements"
        request_body = {
            "title": title,
            "description": description,
            "price": price,
            "location": location,
            "category_id": category_id
        }
        response = post(url, json=request_body)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_verify_login(login):
    # Creating endpoint and calling GET method on this endpoint.
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
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_update_user_data(column, value):
    # Creating endpoint and calling GET method on this endpoint.
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
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_complete_the_announcement(announcement_id):
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/announcements/{announcement_id}/complete"
        response = patch(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_restore_the_announcement(announcement_id):
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/announcements/{announcement_id}/restore"
        response = patch(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_delete_the_announcement(announcement_id):
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/announcements/{announcement_id}/delete"
        response = patch(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_get_user_favorite_announcements():
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/users/{Config_data.logged_in_user_info.user_id}/favorite-announcements"
        response = get(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_add_announcement_to_favorite(announcement_id):
    # Creating endpoint and calling GET method on this endpoint.
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
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def request_to_delete_announcement_from_favorite(favorite_announcement_id):
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = f"http://127.0.0.1:5000/favorite-announcements/{favorite_announcement_id}"
        response = delete(url)

    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response
