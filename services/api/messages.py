from utils import constants, config_data
from requests import get, post, Response, RequestException


def request_to_get_messages(announcement_id=None, conversation_id=None):
    """Function responsible for requesting to download a message using the conversation id or announcement id."""
    # Creating url, request_body and calling GET method on this endpoint.
    try:
        url = f"{constants.backend_url}/users/{config_data.logged_in_user_info.user_id}/messages"
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
        url = f"{constants.backend_url}/users/{config_data.logged_in_user_info.user_id}/messages"
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
        url = f"{constants.backend_url}/users/{config_data.logged_in_user_info.user_id}/conversations"
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
