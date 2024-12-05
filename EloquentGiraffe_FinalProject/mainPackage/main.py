# main.py

from file_handlerPackage.file_handler import FileHandler
from decryptionPackage.movie_decryptor import MovieDecryptor
from decryptionPackage.location_decryptor import Location_Decryptor
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
    
    print(f"Loaded dictionary sample: {dictionary[:10]}")
    print(f"Total lines in dictionary: {len(dictionary)}")

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
        print(f"Attempting to decrypt message: {encrypted_message}")
        decrypted_message = movie_decryptor.decrypt_message(encrypted_message)

        if decrypted_message:
            print(f"Decrypted message: {decrypted_message}")
            results.append(decrypted_message)
        

   