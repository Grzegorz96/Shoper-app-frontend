from io import BytesIO
import base64
from PIL import Image, ImageTk


def convert_image_to_tkinter(base_64_photo):
    """Converts the main photo of an announcement to a tkinter image."""
    # Decoding the base64 string to an image. The image is then resized to 90x67 pixels.
    image_data = base64.b64decode(base_64_photo)

    # Open the image from the binary data using PIL.
    image = Image.open(BytesIO(image_data))

    # Resize the image to fit within the specified dimensions (115x67 pixels), maintaining aspect ratio.
    image.thumbnail((115, 67), resample=Image.LANCZOS)

    # Convert the PIL image to a format suitable for Tkinter.
    main_photo = ImageTk.PhotoImage(image)

    # Return the Tkinter-compatible image.
    return main_photo


def resize_image(image_path, width, height):
    """Resize the image to the specified dimensions and return the resized image as a buffer."""
    # Open the image file.
    with Image.open(image_path) as img:
        # Resize the image using Lanczos resampling algorithm.
        img.thumbnail((width, height), resample=Image.LANCZOS)

        # Convert image to RGB mode if it's not already in RGB.
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Save the resized image to a buffer as JPEG.
        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=85, optimize=True)
        buffer.seek(0)

        # Return the buffer containing the image data.
        return buffer
