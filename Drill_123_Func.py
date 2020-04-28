from tkinter import *
import Tkinter as tk
import Tkinter.filedialog

import Drill_123_Main
import Drill_123_Gui


def openDir(self):
    self.Dir = tkFileDialog.askdirectory()
    print (self.dir)
