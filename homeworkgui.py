"""
A program to use the Homework class to create
class folders using a GUI.
"""

import os
import tkinter
import tkinter.messagebox


class HomeworkGUI:

    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        # Create the frames to group widgets
        self.class_frame = tkinter.Frame(self.main_window)
        self.mod_frame = tkinter.Frame(self.main_window)
        self.test_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for the class name
        self.prompt_name = tkinter.Label(self.class_frame,
                                          text = 'Enter the name of the class:')
        self.class_entry = tkinter.Entry(self.class_frame,
                                         width=10)
        self.prompt_name.pack(side='left')
        self.class_entry.pack(side='left')

        # Create and pack the widgets for the mod frame
        self.prompt_mods = tkinter.Label(self.mod_frame,
                                         text='Enter the number of MODS:')
        self.mod_entry = tkinter.Entry(self.mod_frame,
                                       width=10)
        self.prompt_mods.pack(side='left')
        self.mod_entry.pack(side='left')

        # Create and pack the widgets for the test frame
        self.prompt_test = tkinter.Label(self.test_frame,
                                         text='Enter the number of tests:')
        self.test_entry = tkinter.Entry(self.test_frame,
                                        width=10)
        self.prompt_test.pack(side='left')
        self.test_entry.pack(side='left')

        # Create and pack the button widgets
        self.create_button = tkinter.Button(self.button_frame,
                                            text='Create',
                                            command=self.create)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.create_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.class_frame.pack()
        self.mod_frame.pack()
        self.test_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    # The create method is the callback function for
    # the create_button widget

    def create(self):
        # Get the three entries and store them
        # in variables.
        self.name = self.class_entry.get()
        self.mod = int(self.mod_entry.get())
        self.test = int(self.test_entry.get())

        for num in range(1, self.mod + 1):
            os.makedirs(f"C:/Users/HPi7/Dropbox/IvyTech/{self.name}/MOD{num}")
            os.makedirs(f"C:/Users/HPi7/Dropbox/IvyTech/{self.name}/MOD{num}/assignment")

        for num in range(1, self.test + 1):
            os.makedirs(f"C:/Users/HPi7/Dropbox/IvyTech/{self.name}/Test{num}")

        tkinter.messagebox.showinfo('Results','The folders have been created.')

# Create an instance of the HomeworkGUI class.
homework1 = HomeworkGUI()
            
            
        
