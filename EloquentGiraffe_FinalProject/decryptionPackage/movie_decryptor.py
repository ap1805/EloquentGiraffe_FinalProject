
from cryptography.fernet import Fernet
import base64
import traceback

class MovieDecryptor:
    """Handles decryption tasks for movie names."""

    def __init__(self, key):
        """
        Initialize the MovieDecryptor with the encryption key.
        @param key: The decryption key.
        """
        # Ensure the key is valid and base64 encoded.
        try:
            if isinstance(key, str):
                key = key.encode()  
            base64.urlsafe_b64decode(key)  
            self.cipher_suite = Fernet(key)
        except Exception as e:
            raise ValueError(f"Invalid decryption key: {e}")

    def decrypt_message(self, encrypted_message):
        """
        Decrypt an encrypted message using Fernet.
        @param encrypted_message: The encrypted message to decrypt.
        @return: The decrypted message or None on failure.
        """
        try:
            if not encrypted_message:
                raise ValueError("The encrypted message is empty or None.")

            # Ensure the message is properly encoded before decryption.
            decrypted = self.cipher_suite.decrypt(encrypted_message.encode()).decode('utf-8')
            return decrypted
        except Exception as e:
            print(f"Error decrypting movie message: {e}")
            traceback.print_exc()  # Add more detailed traceback for debugging
            return None

