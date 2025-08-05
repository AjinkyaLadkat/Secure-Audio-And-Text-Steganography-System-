from stegano import lsb
from PIL import Image
import os

def convert_to_png(input_path: str) -> str:
    """
    Convert any image to PNG format and return the PNG file path.
    """
    img = Image.open(input_path)
    png_path = os.path.splitext(input_path)[0] + ".png"
    img.save(png_path, "PNG")
    return png_path

def hide_text_in_image(image_path: str, secret_text: str) -> str:
    """
    Hide secret_text inside the image at image_path.
    Converts image to PNG internally if needed.
    Returns the path to the new image with hidden data.
    """
    # Convert image to PNG first
    png_image_path = convert_to_png(image_path)

    output_path = "assets/hidden_image.png"
    secret_image = lsb.hide(png_image_path, secret_text)
    secret_image.save(output_path)
    return output_path

def reveal_text_from_image(stego_image_path: str) -> str:
    """
    Extract hidden text from the stego image.
    """
    hidden_message = lsb.reveal(stego_image_path)
    return hidden_message
