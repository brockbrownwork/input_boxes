import tkinter as tk
from tkinter import *    

class DoubleInputBox(object):
    def __init__(self, text1, text2, title = ''):
        self.value = None
        self.root = None
        self.text1 = text1
        self.text2 = text2
        self.title = title
        self.result = None

    def center(self):
        self.root.update_idletasks()
        width, height = (self.root.winfo_width(), self.root.winfo_height())
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 50 # 50 is for the awkwardness of the taskbar
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def return_entry(self):
        self.result = self.entry1.get()
        self.result2 = self.entry2.get()
        self.root.destroy()

    def input(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.focus_force() # just in case
        self.root.title(self.title)
        Label(self.root, text=self.text1).grid(columnspan = 2)
        self.entry1 = Entry(self.root)
        self.entry1.focus_set()
        self.entry1.grid(columnspan = 2)
        Label(self.root, text=self.text2).grid(columnspan = 2)
        self.entry2 = Entry(self.root)
        self.entry2.grid(columnspan = 2)
        self.ok_button = Button(self.root, text = "OK", command = self.return_entry)
        self.ok_button.grid(row=4, column=0, padx=25, pady=10)
        Button(self.root, text = "Cancel", command = lambda: self.root.destroy()).grid(row=4, column=1, padx=25, pady=10)
        self.center()
        self.root.bind("<Return>", lambda e = None: self.return_entry())
        self.root.bind("<Escape>", lambda e = None: self.root.destroy())
        self.root.mainloop()

box = DoubleInputBox("Enter your name", "Name")
box.input()
result = box.result
result2 = box.result2
print("result:", result, result2)
