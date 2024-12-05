from cryptography.fernet import Fernet
import base64
import traceback
import json

class Location_Decryptor:
    """Handles the decryption of Location"""
    def __init__(self, dict_file):
        """
        Initialize with a path to the dictionary file.
        @param dict_file: Path to the text file containing the dictionary.
        """
        try:
            with open(dict_file, 'r') as file:
                self.dictionary = [line.strip() for line in file]
        except:
            print("Error loading dictionary file")
    
    def decrypt_location(self, hints):
        """
        Decrypt the location using the provided hints and dictionary.
        Each hint corresponds to a line number in the dictionary file.
        @param hints: List of indices as strings
        @return: Decrypted location string
        """
        with open(hints, 'r') as file:
                hints = json.load(file)
        decrypted_location = " ".join(self.dictionary[int(hint) - 1] for hint in hints)
        return decrypted_location

