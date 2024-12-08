##############################################################################################################################################################################
# Name: Aryan Patel, Will Padgett, Heitor Previatti                                                                                                                          #
# email: patel7aj@mail.uc.edu, padgetwg@mail.uc.edu, previahc@mail.uc.edu                                                                                                    #
# Assignment Number: Final Project                                                                                                                                           #
# Due Date: 12/10/2024                                                                                                                                                       #
# Course #/Section: IS4010/001                                                                                                                                               #
# Semester/Year: Fall/2024                                                                                                                                                   #
# Brief Description of the assignment: Collaborate with team members to develop a python application to go on a scavenger hunt.                                              #  
# Brief Description of what this module does: Decrypts the location using the provided hints and dictionary                                                                  #
# Citations: https://stackoverflow.com/questions/48729915/how-to-read-images-into-a-script-without-using-using-imageio-or-scikit-image                                       #
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/                                                                                                 #
# Anything else that's relevant:                                                                                                                                             #
##############################################################################################################################################################################



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
        
        self.dictionary = dictionary


    
    def decrypt_location(self, hints, dictionary):
        """
        Decrypt the location using the provided hints and dictionary.
        Each hint corresponds to a line number in the dictionary file.
        @param hints: List of indices as strings
        @return: Decrypted location string
        """
        
        decrypted_location = " ".join(self.dictionary[int(hint)] for hint in hints)
        return decrypted_location

