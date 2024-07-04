from tkinter import messagebox, END
from requests import codes
from services.api.messages import request_to_send_message


def send_message(list_of_message_objects, message_entry, refresh_messages, is_user_customer, announcement_object=None):
    """Function responsible for sending the entered message text to the database."""
    # Validation of entered data.
    if message_entry.get() != "":
        if message_entry.get() != "Napisz wiadomość...":

            # If validation is successful, the program checks whether the imported message list contains any objects,
            # if so it will retrieve the conversation id from the object and send the request.
            if list_of_message_objects:
                conversation_id = list_of_message_objects[0].conversation_id
                response_for_sending_message = request_to_send_message(
                    message_entry.get(), is_user_customer, conversation_id=conversation_id)

            # If the user does not yet have a message for a given announcement, a request will be sent with the given
            # announcement_id to first create conversations for a given announcement and then create a message for the
            # conversation.
            else:
                announcement_id = announcement_object.announcement_id
                response_for_sending_message = request_to_send_message(
                    message_entry.get(), is_user_customer, announcement_id=announcement_id)

            # If the returned response has a status of 201, the program will clear message_entry object and will trigger
            # the message refresh function.
            if response_for_sending_message.status_code == codes.created:
                message_entry.delete(0, END)
                refresh_messages()

            # If the returned response has a status of 201, the program will display an error message.
            else:
                messagebox.showerror("Błąd podczas wysyłania wiadomości.",
                                     "Nie udalo sie wysłać wiadomości, spróbuj później.")

        # Validation failure message.
        else:
            messagebox.showwarning("Błądna wiadomość.", "Aby wysłać, najpierw napisz wiadomość.")

    # Validation failure message.
    else:
        messagebox.showwarning("Błędna wiadomość.", "Nie możesz wysłać pustej wiadomości.")
