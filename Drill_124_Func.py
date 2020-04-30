from tkinter import *
import tkinter as tk
import tkinter.filedialog
import os
import time
import shutil
import sqlite3

import Drill_124_Main
import Drill_124_Gui


def openDir(self):
    self.Dir = tkinter.filedialog.askdirectory()
    self.txt_bar.delete(0,END)
    self.txt_bar.insert(0,self.Dir)

def openDirDes(self):
    self.Dir = tkinter.filedialog.askdirectory()
    self.txt_bar2.delete(0,END)
    self.txt_bar2.insert(0,self.Dir)


def pushDir(self):
    src = self.txt_bar.get()
    dessrc = self.txt_bar2.get()
    list_dir = os.listdir(src)
    for filename in list_dir:
        if filename.endswith(".txt"):
            abPath = os.path.join(src, filename)
            modification_time = os.path.getmtime(abPath)
            local_time = time.ctime(modification_time)
            print(filename, modification_time,"Last modification time(Local time):", local_time)
            shutil.move(abPath, dessrc)
            with conn:
                cur.execute("INSERT INTO tbl_file(Col_txt) VALUES (?)", \
                (filename,))
                conn.commit()
            
conn = sqlite3.connect("Drill124.db")
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Col_txt TEXT \
        )")
    

if __name__ == "__main__":
    pass
