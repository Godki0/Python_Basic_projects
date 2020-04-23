
import os
import time


path = "C:\\Users\\burro\\Desktop\\Python Projects\\Python_Basic_projects\\Python_Drill"


list_dir = os.listdir(path)
for filename in list_dir:
    if filename.endswith(".txt"):
        abPath = os.path.join(path, filename)
        modification_time = os.path.getmtime(abPath)
        local_time = time.ctime(modification_time)
        print(filename, modification_time,"Last modification time(Local time):", local_time)


