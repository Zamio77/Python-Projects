"""
A program to generate a class folder, mod and assignment folders
within directories.
"""

import os

class Homework:

    # create the Create function
    def create(class_name, number_of_modules = 1, number_of_tests = 2):
        for num in range(1, number_of_modules + 1):
            os.makedirs(f"C:/Users/HPi7/Dropbox/IvyTech/{class_name}/MOD{num}")
            os.makedirs(f"C:/Users/HPi7/Dropbox/IvyTech/{class_name}/MOD{num}/assignment")

        for num in range(1, number_of_tests + 1):
            os.makedirs(f"C:/Users/HPi7/Dropbox/IvyTech/{class_name}/Test{num}")
            


homework1 = Homework()
            
homework1.create("SDEV253", 5)
