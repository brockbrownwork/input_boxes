import tkinter as tk
from tkinter import *


class ButtonBox(object):
    def __init__(self, text, title, button_options):
        self.value = None
        self.root = None
        self.button_options = button_options
        self.text = text
        self.title = title
    def center(self):
        self.root.update_idletasks()
        width, height = (self.root.winfo_width(), self.root.winfo_height())
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 50 # 50 is for the awkwardness of the taskbar
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    def options(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.focus_force() # just in case
        self.root.title(self.title)
        Label(self.root, text=self.text).grid(columnspan=len(self.button_options))
        if type(self.button_options) == str:
            self.button_options = [self.button_options]
        if type(self.button_options) == list or tuple:
            for index, text in enumerate(self.button_options):
                tk.Button(self.root, text = f"{index + 1}: {text}", command = lambda index = index: self.finish(self.button_options[index])).grid(row=3, column=index, padx=25, pady=10)
                tk.Button(self.root, text = "Cancel", command = self.root.destroy).grid(row=4, columnspan=len(self.text), padx=25, pady=10)
                # bind number button to the corresponding button please
                if index < 10: # prevent from assigning to nonexisting keys
                    self.root.bind(str(index + 1), lambda event, index = index: self.finish(self.button_options[index]))
        self.center()
        self.root.mainloop()
        return self.value

    def finish(self, value):
        self.value = value
        self.root.destroy()

def inputbox(text=None, title=None):
    root = Tk()
    root.attributes("-topmost", True)
    root.focus_force() # just in case
    root.title(title)

    # Create this method before you create the entry
    def return_entry():
        """Gets and prints the content of the entry"""
        content = entry.get()
        root.destroy()
        return(content)  

    Label(root, text=text).grid(row=0, sticky=W)

    entry = Entry(root)
    entry.grid(row=1, column=1)

    # Connect the entry with the return button
    entry.bind('<Return>', return_entry) 

    mainloop()
        

r = inputbox("what is 2 + 2?", None)
print(r)

