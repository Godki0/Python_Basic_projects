

import sqlite3

conn = sqlite3.connect('Drill.db')

fileList = ('information.docx', 'Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Col_txt TEXT \
        )")
    for filename in fileList:
        if filename.endswith(".txt"):
            print(filename)
            cur.execute("INSERT INTO tbl_file(Col_txt) VALUES (?)", \
            (filename,))
    conn.commit()
conn.close() 

