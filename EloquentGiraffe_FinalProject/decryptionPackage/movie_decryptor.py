##############################################################################################################################################################################
# Name: Aryan Patel, Will Padgett, Heitor Previatti                                                                                                                          #
# email: patel7aj@mail.uc.edu, padgetwg@mail.uc.edu, previahc@mail.uc.edu                                                                                                    #
# Assignment Number: Final Project                                                                                                                                           #
# Due Date: 12/10/2024                                                                                                                                                       #
# Course #/Section: IS4010/001                                                                                                                                               #
# Semester/Year: Fall/2024                                                                                                                                                   #
# Brief Description of the assignment: Collaborate with team members to develop a python application to go on a scavenger hunt.                                              #  
# Brief Description of what this module does: This module decrypts the movie using the cryptography Package                                                                  #
# Citations: https://stackoverflow.com/questions/48729915/how-to-read-images-into-a-script-without-using-using-imageio-or-scikit-image                                       #
#https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/                                                                                                 #
# Anything else that's relevant:                                                                                                                                             #
##############################################################################################################################################################################




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
        
        if isinstance(key, str):
            key = key.encode()  
        base64.urlsafe_b64decode(key)  
        self.cipher_suite = Fernet(key)
        
    def decrypt_message(self, encrypted_message):
        """
        Decrypt an encrypted message using Fernet.
        @param encrypted_message: The encrypted message to decrypt.
        @return: The decrypted message or None on failure.
        """
        decrypted = self.cipher_suite.decrypt(encrypted_message.encode()).decode('utf-8')
        return decrypted
        