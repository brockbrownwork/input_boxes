import tkinter as tk
from tkinter import *


def announce(title, text, buttons="Ok", size = "200x100"):
    root = Tk()
    root.geometry(size)
    root.title(title)
    label = Label(root, text=text)
    label.pack()
    button = Button(root, text=buttons, command=root.destroy)
    button.pack()
    root.mainloop()


class ButtonBox(object):
    def __init__(self, text, title, button_options, size = "400x200"):
        self.value = None
        self.root = None
        self.button_options = button_options
        self.text = text
        self.title = title
        self.size = size

    def options(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.geometry(self.size)
        self.root.title(self.title)
        Label(self.root, text=self.text).pack()
        buttons = []
        for index, text in enumerate(self.button_options):
            buttons.append(tk.Button(self.root, text = text, 
                               command = lambda index = index: self.finish(self.button_options[index])))
            buttons[index].pack()
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