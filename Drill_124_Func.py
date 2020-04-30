from tkinter import *
import tkinter as tk
import tkinter.filedialog
import os
import time

import Drill_124_Main
import Drill_124_Gui


def openDir(self):
    self.Dir = tkinter.filedialog.askdirectory()
    self.txt_bar.delete(0,END)
    self.txt_bar.insert(0,self.Dir)
    print(self.Dir)

def openDirDes(self):
    self.Dir = tkinter.filedialog.askdirectory()
    self.txt_bar2.delete(0,END)
    self.txt_bar2.insert(0,self.Dir)
    print(self.Dir)


def pushDir(self):
    list_dir = os.listdir(openDir)
    for filename in list_dir:
        if filename.endswith(".txt"):
            abPath = os.path.join(path, filename)
            modification_time = os.path.getmtime(abPath)
            local_time = time.ctime(modification_time)
            print(filename, modification_time,"Last modification time(Local time):", local_time)

if __name__ == "__main__":
    pass
