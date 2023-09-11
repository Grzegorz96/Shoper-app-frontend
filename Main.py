# Function import for graphical initialization.
from GUI import init_main_window, init_top_panel, init_shopper_page_frame
# Import function to load images
from Functions import loading_images

# Mainloop of SHOPPER application
if __name__ == "__main__":
    """Initialization of the main application window, all changes will be added and removed for this object.
    The application object must be run in the mainloop so that the application does not shut down."""
    root = init_main_window()
    # Loading static files into the project.
    loading_images()
    # Top panel initialization for root object.
    init_top_panel(root)
    # First initialization of shopper_page_frame
    init_shopper_page_frame(root)
    # Calling the mainloop method on the root object.
    root.mainloop()
