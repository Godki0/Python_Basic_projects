# Python Ver:   3.8.2
#
# Author:       Braydon L Burrows
#
#
#
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk

#other modules
import Drill_124_Main
import Drill_124_Func


def load_gui(self):


    self.btn_browse = tk.Button(self.master,width=12, height=1,text='Browse...',command=lambda: Drill_124_Func.openDir(self))
    self.btn_browse.grid(row=0,column=0,padx=(30,0),pady=(30,0),sticky=S)
    self.btn_browse2 = tk.Button(self.master,width=12, height=1,text='Browse...',command=lambda: Drill_124_Func.openDirDes(self))
    self.btn_browse2.grid(row=1,column=0,padx=(30,0),pady=(30,0),sticky=S)
    self.btn_pushdir = tk.Button(self.master,width=12, height=2,text='Push file',command=lambda: Drill_124_Func.pushDir(self))
    self.btn_pushdir.grid(row=2,column=0,padx=(30,0),pady=(30,0),sticky=S)


    self.txt_bar = tk.Entry(self.master,text='')
    self.txt_bar.grid(row=0,column=1,columnspan=3,padx=(40,0),pady=(0,0),sticky=S)
    self.txt_bar2 = tk.Entry(self.master,text='')
    self.txt_bar2.grid(row=1,column=1,columnspan=3,padx=(40,0),pady=(0,0),sticky=S)                              


if __name__ == "__main__":
    pass
