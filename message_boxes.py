import tkinter as tk
from tkinter import *


def announce(title, text, buttons="Ok"):
    root = Tk()
    root.title(title)
    label = Label(root, text=text)
    label.grid()
    button = Button(root, text=buttons, command=root.destroy)
    button.grid(row=2, columnspan=len(text))
    root.update_idletasks()
    width, height = (root.winfo_width(), root.winfo_height())
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2) - 50 # 50 is for the awkwardness of the taskbar
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.mainloop()


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
        if type(self.button_options) == list or type(self.button_options) == tuple:
            for index, text in enumerate(self.button_options):
                tk.Button(self.root, text = f"{index + 1}: {text}", command = lambda index = index: self.finish(self.button_options[index])).grid(row=3, column=index, padx=25, pady=10)
                tk.Button(self.root, text = "Cancel", command = self.root.destroy).grid(row=4, columnspan=len(self.button_options), padx=25, pady=10)
                # bind number button to the corresponding button please
                if index < 10: # prevent from assigning to nonexisting keys
                    self.root.bind(str(index + 1), lambda event, index = index: self.finish(self.button_options[index]))
        if type(self.button_options) == str:
            tk.Button(self.root, text = self.button_options, command = self.finish(self.button_options)).grid(row=3, columnspan=len(self.button_options), padx=25, pady=10)
            tk.Button(self.root, text = "Cancel", command = self.root.destroy).grid(row=4, columnspan=len(self.button_options), padx=25, pady=10)
        self.center()
        self.root.mainloop()
        return self.value

    def finish(self, value):
        self.value = value
        self.root.destroy()


r = ButtonBox("Do you want to continue?", "Continue?", "Sure").options()
print(r)

