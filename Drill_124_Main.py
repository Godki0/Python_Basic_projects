#
# Python ver: 3.8.2
#
# Author: Braydon L Burrows
#
#
#
# Tested OS: Windows 10

from tkinter import *
import tkinter as tk


# Other module import
import Drill_124_Gui
import Drill_124_Func


# Frame that will be used in our own class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Defining our master frame configuration
        self.master = master
        self.master.minsize(400,240) #(height, width)
        self.master.maxsize(400,240)
        self.master.title("Check files")
        

        Drill_124_Gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
