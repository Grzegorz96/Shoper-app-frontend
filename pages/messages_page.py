from utils import config_data
from utils.helpers import config_buttons, create_buttons, set_right, delete_text
from tkinter import Frame, Button, Label, Text, Scrollbar, Entry, END, W, E, ttk
from logic.messages.get_messages import get_messages
from logic.messages.send_message import send_message
from logic.messages.get_conversations import get_conversations


def init_messages_page_frame():
    """A function that initializes the user's messages page. The user can select the appropriate conversation
    and reply to the buyer or seller."""
    # Destroying the current page.
    config_data.current_page.destroy()

    # Init messages_page for root.
    messages_page = Frame(config_data.root, bg="#A9A9A9", width=1280, height=640, highlightbackground="black",
                          highlightthickness=2)
    messages_page.pack()

    # Init horizontal separators.
    ttk.Separator(messages_page).place(x=40, y=85, width=240)
    ttk.Separator(messages_page).place(x=360, y=85, width=240)

    # Init vertical separators.
    ttk.Separator(messages_page).place(x=320, y=15, height=600)
    ttk.Separator(messages_page).place(x=640, y=15, height=600)

    # Init labels.
    Label(messages_page, text="Kupujesz", font=("Arial", 27), bg="#A9A9A9").place(x=85, y=30)
    Label(messages_page, text="Sprzedajesz", font=("Arial", 27), bg="#A9A9A9").place(x=378, y=30)

    def config_conversations_page_as_customer(actual_page=1, list_of_objects=None):
        """Pagination function for downloaded conversations as a customer."""
        # Retrieving a list of conversation objects and assigning them to a variable.
        conversations_as_customer = get_conversations(1, actual_page)

        # for first calling of function.
        if not isinstance(list_of_objects, list):
            list_of_objects = []
        else:
            # Destroying list of initialized announcement objects.
            for element in list_of_objects:
                element.destroy()
            # Clearing destroyed objects from list.
            list_of_objects.clear()

        rows = 0
        # init customer_conversation_objects from list to messages_page.
        for customer_conversation_object in conversations_as_customer:
            # Init title_button and adding it to the list of objects.
            title_button = Button(messages_page, text=customer_conversation_object.title, bg="#D3D3D3",
                                  font=("Arial", 10), anchor=W, borderwidth=1,
                                  command=lambda conversation_object=customer_conversation_object:
                                  update_text_of_messages(conversation_object, True))
            title_button.place(x=15, y=(rows * 75) + 100, width=300, height=22)
            list_of_objects.append(title_button)

            # Init id_label and adding it to the list of objects.
            id_label = Label(messages_page, text=f"ID: {customer_conversation_object.announcement_id}", anchor=E,
                             bg="#D3D3D3", font=("Arial", 9))
            id_label.place(x=244, y=(rows * 75) + 123, width=70, height=15)
            list_of_objects.append(id_label)

            # Init name_label and adding it to the list of objects.
            name_label = Label(messages_page, text=f"Sprzedający: {customer_conversation_object.first_name}",
                               anchor=W, bg="#D3D3D3", font=("Arial", 9))
            name_label.place(x=15, y=(rows * 75) + 123, width=227, height=15)
            list_of_objects.append(name_label)

            rows += 1
            if rows == 7:
                break

        # Updating buttons depending on the number of the current page and the number of downloaded conversations.
        config_buttons(actual_page, button_previous_customer, button_next_customer, conversations_as_customer,
                       config_conversations_page_as_customer, list_of_objects, 7)

    def config_conversations_page_as_seller(actual_page=1, list_of_objects=None):
        """Pagination function for downloaded conversations as a seller."""
        # Retrieving a list of conversation objects and assigning them to a variable.
        conversations_as_seller = get_conversations(0, actual_page)

        if not isinstance(list_of_objects, list):
            list_of_objects = []
        else:
            # Destroying list of initialized announcement objects.
            for element in list_of_objects:
                element.destroy()
            # Clearing destroyed objects from list.
            list_of_objects.clear()

        rows = 0
        # init seller_conversation_objects from list to messages_page.
        for seller_conversation_object in conversations_as_seller:
            # Init title_button and adding it to the list of objects.
            title_button = Button(messages_page, text=seller_conversation_object.title, bg="#D3D3D3",
                                  font=("Arial", 10), anchor=W, borderwidth=1,
                                  command=lambda conversation_object=seller_conversation_object:
                                  update_text_of_messages(conversation_object, False))
            title_button.place(x=335, y=(rows * 75) + 100, width=300, height=22)
            list_of_objects.append(title_button)

            # Init id_label and adding it to the list of objects.
            id_label = Label(messages_page, text=f"ID: {seller_conversation_object.announcement_id}", anchor=E,
                             bg="#D3D3D3", font=("Arial", 9))
            id_label.place(x=564, y=(rows * 75) + 123, width=70, height=15)
            list_of_objects.append(id_label)

            # Init name_label and adding it to the list of objects.
            name_label = Label(messages_page, text=f"Kupujący: {seller_conversation_object.first_name}", anchor=W,
                               bg="#D3D3D3", font=("Arial", 9))
            name_label.place(x=335, y=(rows * 75) + 123, width=227, height=15)
            list_of_objects.append(name_label)

            rows += 1
            if rows == 7:
                break

        # Updating buttons depending on the number of the current page and the number of downloaded conversations.
        config_buttons(actual_page, button_previous_seller, button_next_seller, conversations_as_seller,
                       config_conversations_page_as_seller, list_of_objects, 7)

    # Calling the button creation function and assigning the returned objects to variables.
    button_previous_customer, button_next_customer = create_buttons(messages_page, 15, 254)
    button_previous_seller, button_next_seller = create_buttons(messages_page, 335, 574)
    # The first call to the page setup functions.
    config_conversations_page_as_customer()
    config_conversations_page_as_seller()

    choose_conversation_label = Label(messages_page, bg="#A9A9A9", font=("Arial", 20),
                                      text=f"Wybierz konwersacje, {config_data.logged_in_user_info.first_name}")
    choose_conversation_label.place(x=750, y=250)
    # Message window objects will be stored in this list and then deleted when a new window is created.
    list_of_objects_to_destroy = []

    def update_text_of_messages(conversation_object, is_user_customer):
        """The function supports the display of new message windows and the correct destruction of old windows."""
        nonlocal choose_conversation_label
        # Removing the label the first time the function is called.
        if isinstance(choose_conversation_label, Label):
            choose_conversation_label.destroy()
            choose_conversation_label = None

        # Destroying objects of the previous window.
        for element in list_of_objects_to_destroy:
            element.destroy()
        # Clearing objects of the previous window.
        list_of_objects_to_destroy.clear()

        # Init text object for displaying messages and adding it to the list of objects.
        text = Text(messages_page, width=67, height=30, bg="#D3D3D3", borderwidth=0, font=("Arial", 12), wrap="word")
        text.place(x=650, y=50)
        list_of_objects_to_destroy.append(text)

        # Init scrollbar object for scrolling messages and adding it to the list of objects.
        scrollbar = Scrollbar(messages_page, command=text.yview)
        scrollbar.place(x=1258, y=50, height=577)
        list_of_objects_to_destroy.append(scrollbar)

        # Configuration of the scrollbar object with the text object.
        text["yscrollcommand"] = scrollbar.set
        # Configure the message setting function on the right.
        text.bind("<Configure>", set_right)
        person = "Sprzedający" if is_user_customer else "Kupujący"

        # Init title_label and adding it to the list of objects.
        title_label = Label(messages_page, text=conversation_object.title, anchor=W, font=("Arial", 16),
                            bg="#A9A9A9")
        title_label.place(x=650, y=15, width=370)
        list_of_objects_to_destroy.append(title_label)

        # Init person_label and adding it to the list of objects.
        person_label = Label(messages_page, text=f"{person}: {conversation_object.first_name}", anchor=E,
                             font=("Arial", 16), bg="#A9A9A9")
        person_label.place(x=1025, y=15, width=250)
        list_of_objects_to_destroy.append(person_label)

        # Init message_entry to enter message text and adding it to the list of objects.
        message_entry = Entry(messages_page, width=41, font=("Arial", 16))
        message_entry.place(x=650, y=600)
        message_entry.insert(0, "Napisz wiadomość...")
        message_entry.bind("<Button-1>", lambda event: delete_text(message_entry))
        list_of_objects_to_destroy.append(message_entry)

        # Init send_button to send message text and adding it to the list of objects.
        send_button = Button(messages_page, text="Wyślij", width=11, borderwidth=1, font=("Arial", 11))
        send_button.place(x=1150, y=600)
        list_of_objects_to_destroy.append(send_button)

        def refresh_messages():
            """The function is responsible for downloading messages, appropriate text display and configuration
            of the button for sending messages."""
            # Downloading messages from conversation_object and assigning them to a variable.
            list_of_message_objects = get_messages(conversation_object=conversation_object)

            # Setting the default values of the text object before adding the message.
            text["state"] = "normal"
            text.delete("1.0", END)

            i = 1
            # Displaying messages in the appropriate position depending on who sent the message.
            for message in list_of_message_objects:
                position = f"{i}.0"
                if message.customer_flag == 1:
                    text.insert(position, f"{message.first_name}\n{message.post_date}\n{message.content}\n\n")
                else:
                    text.insert(position, f"\t{message.first_name}\n\t{message.post_date}"
                                          f"\n\t{message.content}\n\n")
                i += 4

            # Setting state on disabled.
            text["state"] = "disabled"
            # Setting send_button with correct state and function.
            if list_of_message_objects:
                send_button.config(command=lambda: send_message(list_of_message_objects, message_entry,
                                                                refresh_messages, is_user_customer))
                message_entry.bind("<Return>", lambda event: send_message(list_of_message_objects, message_entry,
                                                                          refresh_messages, is_user_customer))

            else:
                send_button.config(state="disabled")
                message_entry.config(state="disabled")

        # First function call.
        refresh_messages()
    # Assigning a local page to a global variable to be able to destroy it when initializing the next page.
    config_data.current_page = messages_page
