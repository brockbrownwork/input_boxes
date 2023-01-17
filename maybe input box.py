import tkinter as tk
from tkinter import *    

class InputBox(object):
    def __init__(self, text, title):
        self.value = None
        self.root = None
        self.text = text
        self.title = title

    def center(self):
        self.root.update_idletasks()
        width, height = (self.root.winfo_width(), self.root.winfo_height())
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 50 # 50 is for the awkwardness of the taskbar
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def return_entry(self):
        Entry.get(self)
        self.root.destroy()

    def input(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.focus_force() # just in case
        self.root.title(self.title)
        Label(self.root, text=self.text).grid()
        Entry(self.root).grid()
        Button(self.root, text = "OK", command = self.return_entry).grid(row=3, column=0, padx=25, pady=10)
        Button(self.root, text = "Cancel", command = self.root.destroy).grid(row=3, column=1, padx=25, pady=10)
        self.center()
        self.root.mainloop()

r = InputBox("Enter your name", "Name").input()
print(r)