import tkinter as tk
from tkinter import *


def announce(title, text, buttons="Ok", width = 200, height = 100, x = 800, y = 400):
    root = Tk()
    argument = f"{width}x{height}+{x}+{y}"
    root.geometry(argument)
    root.title(title)
    label = Label(root, text=text)
    label.pack()
    button = Button(root, text=buttons, command=root.destroy)
    button.pack()
    root.mainloop()


class ButtonBox(object):
    def __init__(self, text, title, button_options, width = 400, height = 200, x = 800, y = 400):
        self.value = None
        self.root = None
        self.button_options = button_options
        self.text = text
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        for index, text in enumerate(self.button_options):
            tk.Button(self.root, text = f"{index + 1}: {text}", command = lambda index = index: self.finish(self.button_options[index])).grid(row=3, column=index)
            # bind number button to the corresponding button
            self.root.bind(str(index + 1), lambda event, index = index: self.finish(self.button_options[index]))
        self.center()
        self.root.mainloop()
        return self.value

    def finish(self, value):
        self.value = value
        self.root.destroy()

r = ButtonBox("Do you want to continue?", "Continue?", ("Yes", "No", "Maybe", "You tell me")).options()
print(r)