##############################################################################################################################################################################
# Name: Aryan Patel, Will Padgett, Heitor Previatti                                                                                                                          #
# email: patel7aj@mail.uc.edu, padgetwg@mail.uc.edu, previahc@mail.uc.edu                                                                                                    #
# Assignment Number: Final Project                                                                                                                                           #
# Due Date: 12/10/2024                                                                                                                                                       #
# Course #/Section: IS4010/001                                                                                                                                               #
# Semester/Year: Fall/2024                                                                                                                                                   #
# Brief Description of the assignment: Collaborate with team members to develop a python application to go on a scavenger hunt.                                              #  
# Brief Description of what this module does:This module calls all the functions in the other modules                                                                        #
# Citations: https://stackoverflow.com/questions/48729915/how-to-read-images-into-a-script-without-using-using-imageio-or-scikit-image                                       #
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/                                                                                                 #
# Anything else that's relevant:                                                                                                                                             #
##############################################################################################################################################################################



from file_handlerPackage.file_handler import FileHandler
from decryptionPackage.movie_decryptor import MovieDecryptor
from decryptionPackage.location_decryptor import Location_Decryptor
from picturePackage.picture import Picture
import os

if __name__ == "__main__":
    # Define the base directory dynamically
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Define absolute paths for input files
    group_hints_file = os.path.join(base_dir, 'Data', 'EncryptedGroupHints Fall 2024 Section 001.json')
    messages_file = os.path.join(base_dir, 'Data', 'TeamsAndEncryptedMessagesForDistribution.json')
    dictionary_file = os.path.join(base_dir, 'Data', 'UCEnglish.txt')

    # Load data using FileHandler class
    group_hints_data = FileHandler.load_json(group_hints_file)
    messages_data = FileHandler.load_json(messages_file)
    dictionary = list(FileHandler.load_plain_text(dictionary_file))
    
   

    # Hardcoded group name and decryption key
    group_name = "EloquentGiraffe"
    key = b'J6ixusQyNGGFBPd7K1WWkUZDTaUMfOVO7zQ9UrUvicY='  # Replace with the actual key

    # Create instances of MovieDecryptor and LocationDecryptor
    movie_decryptor = MovieDecryptor(key)
    location_decryptor = Location_Decryptor(dictionary)

    # Get and validate group hints for location decryption
    group_hints = group_hints_data.get(group_name, [])
    print(f"Group Hints: {group_hints}")
    location = location_decryptor.decrypt_location(group_hints, dictionary)
    print(f"Decrypted Location: {location}")
        

    # Decrypt movie names using MovieDecryptor
    group_messages = messages_data.get(group_name, [])
    results = []

    for encrypted_message in group_messages:
       
        decrypted_message = movie_decryptor.decrypt_message(encrypted_message)
        print(f"Decrypted message: {decrypted_message}")
            
    chickfilaPicture = Picture('./Data/Chickfila.jpg')

    chickfilaPicture.show_image()
   