import tkinter as tk
from tkinter import *


class ButtonBox(object):
    '''
    A message box that returns the text of the button pressed. Can have as many buttons as you want, as long as there is at least one. 
    
    '''
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
        Label(self.root, text=self.text).grid(columnspan=len(self.button_options), padx=25, pady=10)
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

class InputBox(object):
    '''
    A message box that returns the text of the entry.
    
    '''
    def __init__(self, text, title = '', show = None):
        self.value = None
        self.root = None
        self.text = text
        self.title = title
        self.show = show
        self.result = None

    def center(self):
        self.root.update_idletasks()
        width, height = (self.root.winfo_width(), self.root.winfo_height())
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 50 # 50 is for the awkwardness of the taskbar
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def return_entry(self):
        self.result = self.entry.get()
        self.root.destroy()

    def input(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.focus_force() # just in case
        self.root.title(self.title)
        Label(self.root, text=self.text).grid(columnspan = 2)
        self.entry = Entry(self.root, show=self.show)
        self.entry.focus_set()
        self.entry.grid(columnspan = 2)
        self.ok_button = Button(self.root, text = "OK", command = self.return_entry)
        self.ok_button.grid(row=3, column=0, padx=25, pady=10)
        Button(self.root, text = "Cancel", command = lambda: self.root.destroy()).grid(row=3, column=1, padx=25, pady=10)
        self.center()
        self.root.bind("<Return>", lambda e = None: self.return_entry())
        self.root.bind("<Escape>", lambda e = None: self.root.destroy())
        self.root.mainloop()

class DoubleInputBox(object):
    '''
    A message box that allows for two seperate text entries, with two different labels. Wil return ("text_input1", "text_input2").
    
    '''
    def __init__(self, text1, text2, title = '', show1 = None, show2 = None):
        self.value = None
        self.root = None
        self.text1 = text1
        self.text2 = text2
        self.title = title
        self.show1 = show1
        self.show2 = show2
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
        self.entry1 = Entry(self.root, show=self.show1)
        self.entry1.focus_set()
        self.entry1.grid(columnspan = 2)
        Label(self.root, text=self.text2).grid(columnspan = 2)
        self.entry2 = Entry(self.root, show=self.show2)
        self.entry2.grid(columnspan = 2)
        self.ok_button = Button(self.root, text = "OK", command = self.return_entry)
        self.ok_button.grid(row=4, column=0, padx=25, pady=10)
        Button(self.root, text = "Cancel", command = lambda: self.root.destroy()).grid(row=4, column=1, padx=25, pady=10)
        self.center()
        self.root.bind("<Return>", lambda e = None: self.return_entry())
        self.root.bind("<Escape>", lambda e = None: self.root.destroy())
        self.root.mainloop()


def button_box(text=None, title=None, button_options=["Ok"]):
    bttn = ButtonBox(text=text, title=title, button_options=button_options).options()
    return bttn

def input_box(text=None, title=None, show=None):
    box = InputBox(text=text, title=title, show=show)
    box.input()
    return box.result

def double_input_box(text1=None, text2=None, title=None, show1=None, show2=None):
    box = DoubleInputBox(text1=text1, text2=text2, title=title, show1=show1, show2=show2)
    box.input()
    result = box.result
    result2 = box.result2
    final_result = result, result2
    return final_result

def login():
    r = double_input_box("Username:", "Password:", "Login", show2="*")
    if r == ("Joe", "123"):
        button_box("Login successful!", "Login")
    else:
        button_box("Login failed!", "Login")
        login()

login()