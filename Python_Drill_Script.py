
import os
import time


path = "C:\\Users\\burro\\Desktop\\Python Projects\\Python_Basic_projects\\Python_Drill"


list_dir = os.listdir(path)
for filename in list_dir:
    if filename.endswith(".txt"):
        fPath = "list_dir"
        fName = "filename"
        abPath = os.path.join(fPath, fName)
        print(filename)

modification_time = os.path.getmtime(path)
print(modification_time)

local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)
