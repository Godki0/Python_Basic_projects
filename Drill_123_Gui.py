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
import Drill_123_Main
import Drill_123_Func


def load_gui(self):


    self.btn_locate = tk.Button(self.master,width=16, height=2,text='Locate directory...',command=lambda: Drill_123_Func.openDir(self))
    self.btn_locate.grid(row=1,column=1,columnspan=2,padx=(115,0),pady=(60,0),sticky=N)
                                 

    self.txt_bar = tk.Entry(self.master,text='')
    self.txt_bar.grid(row=0,column=1,columnspan=3,padx=(100,0),pady=(55,0),sticky=S)
    

if __name__ == "__main__":
    pass
