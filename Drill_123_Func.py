from tkinter import *
import tkinter as tk
import tkinter.filedialog

import Drill_123_Main
import Drill_123_Gui


def openDir(self):
    self.Dir = tkinter.filedialog.askdirectory()
    self.txt_bar.delete(0,END)
    self.txt_bar.insert(0,self.Dir)
    print(self.Dir)
    
