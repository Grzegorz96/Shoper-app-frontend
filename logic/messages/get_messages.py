from tkinter import messagebox
from requests import codes
from models.message import Message
from services.api.messages import request_to_get_messages


def get_messages(announcement_object=None, conversation_object=None):
    """Function responsible for retrieving user's messages using conversation id or announcement id."""
    # If the user has imported a conversation object, the program sends a request with the conversation_id parameter.
    if conversation_object:
        response_for_getting_messages = request_to_get_messages(conversation_id=conversation_object.conversation_id)

    # If the user has not imported the conversation id, it means that he has imported the announcement id,
    # the program will send a request with the announcement_id parameter.
    else:
        response_for_getting_messages = request_to_get_messages(announcement_id=announcement_object.announcement_id)

    # If the returned response has a status of 200, the program will create list of message objects for the downloaded
    # conversation.
    if response_for_getting_messages.status_code == codes.ok:

        list_of_messages_objects = []
        for message in response_for_getting_messages.json()["result"]:
            message_object = Message(
                message["conversation_id"],
                message["message_id"],
                message["customer_flag"],
                message["content"],
                message["post_date"],
                message["user_id"],
                message["first_name"]
            )
            list_of_messages_objects.append(message_object)

        # Return a list of message objects
        return list_of_messages_objects

    # If the returned response has a status of 200, the program will display an error message and return empty list.
    else:
        messagebox.showerror("Błąd podczas wczytywania wiadomości.",
                             "Nie udalo sie wczytać wiadomości, spróbuj później.")
        return []
