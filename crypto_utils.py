from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os
import base64

backend = default_backend()
KEY_LENGTH = 32  # 256-bit AES
IV_LENGTH = 16   # 128-bit IV
SALT_LENGTH = 16

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    return kdf.derive(password.encode())

def encrypt_message(message: str, password: str) -> str:
    salt = os.urandom(SALT_LENGTH)
    iv = os.urandom(IV_LENGTH)
    key = derive_key(password, salt)

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    combined = salt + iv + ciphertext
    return base64.b64encode(combined).decode()

def decrypt_message(encrypted_b64: str, password: str) -> str:
    combined = base64.b64decode(encrypted_b64.encode())

    salt = combined[:SALT_LENGTH]
    iv = combined[SALT_LENGTH:SALT_LENGTH + IV_LENGTH]
    ciphertext = combined[SALT_LENGTH + IV_LENGTH:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()
