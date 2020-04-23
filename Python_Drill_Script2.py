
import sqlite3

import os

conn = sqlite3.connect('Drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Col_txt TEXT \
        )")
    conn.commit()
conn.close()

fileList = ('information.docx', 'Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('Drill.db')

for filename in fileList:
    if filename.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_file(Col_txt) VALUES (?)", \
                        ('Hello'))
            cur.execute("INSERT INTO tbl_file(Col_txt) VALUES (?)", \
                        ('World'))
            conn.commit()
        conn.close()
        print(filename)


with conn:
    cur = conn.cursor()
    cur.execute("SELECT Col_txt FROM tbl_file WHERE Col_txt = 'Hello'")
    cur.execute("SELECT Col_txt FROM tbl_file WHERE Col_txt = 'World'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {}".format(item[0])
    print(msg)
