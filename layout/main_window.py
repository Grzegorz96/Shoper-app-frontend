from tkinter import Tk, PhotoImage, TclError


def init_main_window():
    """The function that initializes the main application window, this is a function that is called from the main.py
    module once and then returns the created root object to the main.py module."""
    # Creating root.
    root = Tk()
    # Creating geometry, title and setting resizable.
    window_width = 1280
    window_height = 720
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.title("SHOPER.PL")
    root.resizable(width=False, height=False)
    # Creating background color and icon of app.
    root.config(bg="#B0C4DE")

    try:
        root.wm_iconphoto(False, PhotoImage(file="./assets/images/home_icon.png"))
    except TclError:
        pass

    # Returning root into main.py.
    return root
