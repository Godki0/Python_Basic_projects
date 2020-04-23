
import sqlite3

import os

conn = sqlite3.connect('Drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_cars( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Col_txt TEXT, \
        )")
    conn.commit()
conn.close()

path = "C:\Users\burro\Desktop\Python Projects\Python_Basic_projects\Python_Drill2"

list_dir = os.listdir(path)
for filename in list_dir:
    if filename.endswith(".txt"):
        print(filename)
