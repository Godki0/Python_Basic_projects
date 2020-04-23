
import sqlite3

conn = sqlite3.connect('Drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Col_txt TEXT \
        )")
    conn.commit()
conn.close()


      
