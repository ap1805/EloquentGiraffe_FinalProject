from cryptography.fernet import Fernet

class movie_decryptor:
    """Handles decryption tasks for movie name."""

    def __init__(self, key):
        """
        Initialize the Decryptor with the encryption key.
        @param Parameter bytes key: The decryption key.
        """
        try:
            if isinstance(key, str):
                key = key.encode() 
            self.cipher_suite = Fernet(key)
        except Exception as e:
            raise ValueError(f"Invalid decryption key: {e}")

    def decrypt_message(self, encrypted_message):
        """
        Decrypt an encrypted message using Fernet.
        @param Parameter str encrypted_message: The encrypted message to decrypt.
        @return str or None: The decrypted message or None on failure.
        """
        try:
            if not encrypted_message:
                raise ValueError("The encrypted message is empty or None.")
            
            decrypted = self.cipher_suite.decrypt(encrypted_message.encode()).decode('utf-8')
            return decrypted
        except Exception as e:
            print(f"Error decrypting message: {e}")
            return None


