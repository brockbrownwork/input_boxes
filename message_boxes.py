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
    def options(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        argument = f"{self.width}x{self.height}+{self.x}+{self.y}"
        self.root.geometry(argument)
        self.root.title(self.title)
        Label(self.root, text=self.text).grid()
        for index, text in enumerate(self.button_options):
            tk.Button(self.root, text = text, command = lambda index = index: self.finish(self.button_options[index])).grid(row=3, column=index)
        self.root.mainloop()
        return self.value

    def finish(self, value):
        self.value = value
        self.root.destroy()

r = ButtonBox("Do you want to continue?", "Continue?", ("Yes", "No", "Maybe", "You tell me")).options()
if r == "Yes":
    print("Yes")
if r == "No":
    print("No")
if r == "Maybe":
    print("Maybe")
if r == "You tell me":
    print("You tell me")