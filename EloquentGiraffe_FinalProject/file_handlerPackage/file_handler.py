##############################################################################################################################################################################
# Name: Aryan Patel, Will Padgett, Heitor Previatti                                                                                                                          #
# email: patel7aj@mail.uc.edu, padgetwg@mail.uc.edu, previahc@mail.uc.edu                                                                                                    #
# Assignment Number: Final Project                                                                                                                                           #
# Due Date: 12/10/2024                                                                                                                                                       #
# Course #/Section: IS4010/001                                                                                                                                               #
# Semester/Year: Fall/2024                                                                                                                                                   #
# Brief Description of the assignment: Collaborate with team members to develop a python application to go on a scavenger hunt.                                              #  
# Brief Description of what this module does: This module loads the json file and text file.                                                                                 #
# Citations: https://stackoverflow.com/questions/48729915/how-to-read-images-into-a-script-without-using-using-imageio-or-scikit-image                                       #
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/                                                                                                 #
# Anything else that's relevant:                                                                                                                                             #
##############################################################################################################################################################################



import json
import os

class FileHandler:
    """Handles file operations like loading and saving JSON and plain text."""

    
    def load_json(file_path):
        """
        Load a JSON file and return its content.
        @param Parameter str file_path: Path to the JSON file.
        @return dict: The JSON content as a dictionary.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        if os.path.getsize(file_path) == 0:
            raise ValueError(f"The file {file_path} is empty.")
        with open(file_path, 'r') as file:
            return json.load(file)

    
    def load_plain_text(file_path):
        """
        Load a plain text file and return its content as a list of lines.
        @param Parameter str file_path: Path to the plain text file.
        @return list: List of stripped lines from the file.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"Error loading plain text file: {e}")
            return []

