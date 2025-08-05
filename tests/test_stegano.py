import sys
import os

# Add project root to sys.path so imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_utils import encrypt_message, decrypt_message
from stegano_utils import hide_text_in_image, reveal_text_from_image

def test_stegano_encrypt_hide_reveal_decrypt():
    original_message = "Testing steganography with AES encryption!"
    password = "KiaStrongPassword"

    # Encrypt message
    encrypted_msg = encrypt_message(original_message, password)

    # Hide encrypted message in sample image
    output_image_path = hide_text_in_image("assets/sample_image.jpeg", encrypted_msg)

    # Reveal encrypted message from image
    revealed_msg = reveal_text_from_image(output_image_path)

    # Decrypt revealed message
    decrypted_msg = decrypt_message(revealed_msg, password)

    # Assert final decrypted message matches original
    assert decrypted_msg == original_message
