# Import function to load images.
from layout.main_window import init_main_window
from layout.top_panel import init_top_panel
from pages.home_page import init_shoper_page_frame
from functions import loading_images
import config_data

# Mainloop of SHOPER application.
if __name__ == "__main__":
    """Initialization of the main application window, all changes will be added and removed for this object.
    The application object must be run in the mainloop so that the application does not shut down."""
    config_data.root = init_main_window()
    # Loading static files into the project.
    loading_images()
    # Top panel initialization for root object.
    init_top_panel()
    # First initialization of shoper_page_frame.
    init_shoper_page_frame()
    # Calling the mainloop method on the root object.
    # root.mainloop(
    config_data.root.mainloop()
