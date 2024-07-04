from utils import config_data
from utils.helpers import set_right, delete_text
from logic.messages.get_messages import get_messages
from logic.messages.send_message import send_message
from tkinter import (Toplevel, Label, Text, Scrollbar, LEFT, RIGHT, Y, Entry, Button, messagebox, PhotoImage, TclError,
                     W, END)


def init_message_window(announcement_object):
    """A function that initializes an additional message window, the user can use it to display and send a message to
    another user's announcement. Then sent message will be displayed on the message page of both the buyer and the
    seller."""
    # Checking if user is logged in.
    if config_data.logged_in_user_info:
        # When user is logged in, program checking if selected announcement isn't user's announcement.
        if config_data.logged_in_user_info.user_id != announcement_object.seller_id:
            # Init message_window from Toplevel class.
            message_window = Toplevel()
            # Adding a window to the global list so that if the window is not closed, the window will automatically
            # close when logging out.
            config_data.list_of_active_windows.append(message_window)
            # Determining the window dimensions.
            message_window_width = 477
            message_window_height = 484
            screen_width = message_window.winfo_screenwidth()
            screen_height = message_window.winfo_screenheight()
            center_x = int(screen_width / 2 - message_window_width / 2)
            center_y = int(screen_height / 2 - message_window_height / 2)
            # Setting the dimensions and position of the window.
            message_window.geometry(f"{message_window_width}x{message_window_height}+{center_x}+{center_y}")
            # Setting the title, resizable, background color and icon-photo.
            message_window.title(announcement_object.first_name)
            message_window.resizable(width=False, height=False)
            message_window.config(bg="#B0C4DE")

            try:
                message_window.wm_iconphoto(False, PhotoImage(file="./assets/images/messages_icon.png"))
            except TclError:
                pass

            # Init labels with information.
            Label(message_window, width=68, height=1, text=announcement_object.title, anchor=W).pack()
            Label(message_window, width=68, height=1, text=f"Cena: {announcement_object.price} ZŁ", anchor=W).pack()
            Label(message_window, width=80, height=1, text=f"ID: {announcement_object.announcement_id}", anchor=W,
                  font=("Arial", 8)).pack()

            # Init text object for displaying messages.
            text = Text(message_window, width=57, height=26, bg="#D3D3D3")
            text.pack(side=LEFT)

            # Init scrollbar object.
            scrollbar = Scrollbar(message_window, command=text.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Connecting a scrollbar object to a text object.
            text["yscrollcommand"] = scrollbar.set
            # Configure the text object to display messages on the right side.
            text.bind("<Configure>", set_right)

            # Init the message_entry object for entering the message text.
            message_entry = Entry(message_window, font=("Arial", 14))
            message_entry.place(x=0, y=457, width=385)
            message_entry.insert(0, "Napisz wiadomość...")
            message_entry.bind("<Button-1>", lambda event: delete_text(message_entry))

            # Init send_button to send messages.
            send_button = Button(message_window, text="Wyślij", width=9, borderwidth=1)
            send_button.place(x=389, y=457)

            def refresh_messages():
                """The function is responsible for downloading messages, appropriate text display and configuration of
                the button for sending messages."""
                # Downloading list of messages from announcement object.
                list_of_message_objects = get_messages(announcement_object=announcement_object)
                # Setting default values for text object.
                text["state"] = "normal"
                text.delete("1.0", END)

                i = 1
                # Appropriate positioning of the message on the text object depending on who sent the message.
                for message in list_of_message_objects:
                    position = f"{i}.0"
                    if message.customer_flag == 1:
                        text.insert(position, f"{message.first_name}\n{message.post_date}\n{message.content}\n\n")
                    else:
                        text.insert(position, f"\t{message.first_name}\n\t{message.post_date}"
                                              f"\n\t{message.content}\n\n")
                    i += 4

                # Setting text state on disabled.
                text["state"] = "disabled"
                # Setting the correct function for the button
                send_button.config(command=lambda: send_message(list_of_message_objects, message_entry,
                                                                refresh_messages, True, announcement_object))
                message_entry.bind("<Return>", lambda event: send_message(list_of_message_objects, message_entry,
                                                                          refresh_messages, True, announcement_object))

            # First function call.
            refresh_messages()

        # Displaying correct warning.
        else:
            messagebox.showwarning("Nie możesz wysłać wiadomości do samego siebie.",
                                   "Próbujesz wysłać wiadomość do własnego ogłoszenia.")
    # Displaying correct warning.
    else:
        messagebox.showwarning("Nie jesteś zalogowany.", "Aby wysłać wiadomość, musisz sie zalogować.")
