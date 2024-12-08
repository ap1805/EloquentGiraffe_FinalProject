##############################################################################################################################################################################
# Name: Aryan Patel, Will Padgett, Heitor Previatti                                                                                                                          #
# email: patel7aj@mail.uc.edu, padgetwg@mail.uc.edu, previahc@mail.uc.edu                                                                                                    #
# Assignment Number: Final Project                                                                                                                                           #
# Due Date: 12/10/2024                                                                                                                                                       #
# Course #/Section: IS4010/001                                                                                                                                               #
# Semester/Year: Fall/2024                                                                                                                                                   #
# Brief Description of the assignment: Collaborate with team members to develop a python application to go on a scavenger hunt.                                              #  
# Brief Description of what this module does: uses matplotlib and numpy libraries in a class with a file path attribute to show the image identified by the filepath         #
# Citations: https://stackoverflow.com/questions/48729915/how-to-read-images-into-a-script-without-using-using-imageio-or-scikit-image                                       #
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/                                                                                                 #
# Anything else that's relevant:                                                                                                                                             #
##############################################################################################################################################################################



import matplotlib.pyplot as plt
import numpy as np

class Picture:

    def __init__(self, image_path):
        '''
        constructor the the class picture
        @param self: the current object
        @param image path: the filepath of the picture that you want to display
        '''
        self.image_path = image_path

    def show_image(self):
        '''
        Loads, corrects orientation, and displays the image using matplotlib
        @param self: the current object
        '''
        image = plt.imread(self.image_path)
        # Flip the image vertically to correct orientation if necessary
        image = np.flipud(image)
        plt.imshow(image)
        plt.axis('off')  # Hide axes for a cleaner display
        plt.show()