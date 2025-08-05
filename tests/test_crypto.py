import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_utils import encrypt_message, decrypt_message

def test_encryption_and_decryption():
    message = "Top secret project 007"
    password = "KiaStrongPassword"

    encrypted = encrypt_message(message, password)
    decrypted = decrypt_message(encrypted, password)

    assert decrypted == message
