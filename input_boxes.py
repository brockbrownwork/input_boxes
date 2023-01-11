import tkinter as tk

class InputBox(object):
    def __init__(self, button_options):
        self.value = None
        self.root = None
        self.button_options = button_options

    def show(self):
        '''Show the window, and wait for the user to click a button'''
        self.root = tk.Tk()
        self.root.attributes("-topmost", True) # keeps the window on top of other windows
        buttons = []
        for index, text in enumerate(self.button_options):
            print(index, text)
            buttons.append(tk.Button(self.root, text = text, 
                               command = lambda index = index: self.finish(self.button_options[index])))
            buttons[index].pack()

        # start the loop, and wait for the dialog to be
        # destroyed. Then, return the value:
        self.root.mainloop()
        return self.value

    def finish(self, value):
        '''Set the value and close the window

        This will cause the show() function to return.
        '''
        self.value = value
        print("finishing with value:", value)
        self.root.destroy()


print("getting ready to show dialog...")
print("value:", InputBox(("Yes", "No", "Maybe")).show())