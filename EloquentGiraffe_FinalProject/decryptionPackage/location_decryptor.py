
from subprocess import list2cmdline
from cryptography.fernet import Fernet
import base64
import traceback
import json

class Location_Decryptor:
    """Handles the decryption of Location"""
    def __init__(self,dictionary):
        """
        Initialize with a path to the dictionary file.
        @param dict_file: Path to the text file containing the dictionary.
        """
        if not isinstance(dictionary, list):
            raise ValueError("Dictionary must be provided as a list of words.")
        self.dictionary = dictionary


    
    def decrypt_location(self, hints, dictionary):
        """
        Decrypt the location using the provided hints and dictionary.
        Each hint corresponds to a line number in the dictionary file.
        @param hints: List of indices as strings
        @return: Decrypted location string
        """
        
        decrypted_location = " ".join(self.dictionary[int(hint) - 1] for hint in hints)
        return decrypted_location

