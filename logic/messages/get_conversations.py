from tkinter import messagebox
from requests import codes
from models.conversation import Conversation
from services.api.messages import request_to_get_conversations


def get_conversations(customer_flag, page):
    """Function responsible for downloading user conversations, specifying the customer_flag and page parameters.
    The function can download conversations for the user as a customer and as a seller."""
    # Calling the function sending a request to download the conversation.
    response_for_getting_conversations = request_to_get_conversations(customer_flag, page)

    # If the returned response has a status of 200, the program will create list of conversation objects.
    if response_for_getting_conversations.status_code == codes.ok:

        list_of_conversations = []
        for conversation in response_for_getting_conversations.json()["result"]:
            conv_object = Conversation(
                conversation["conversation_id"],
                conversation["announcement_id"],
                conversation["title"],
                conversation["first_name"]
            )
            list_of_conversations.append(conv_object)

        # Return list of conversations.
        return list_of_conversations

    # If the returned response has a status of 200, the program will display an error message and return an empty list.
    else:
        messagebox.showerror("Błąd podczas wczytywania konwersacji.",
                             "Nie udalo sie wczytać konwersacji, spróbuj później.")
        return []
