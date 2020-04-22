
import os
import time

fName = "6.txt"

fPath = "C:\\Python_Drill\\"

abPath = os.path.join(fPath, fName)
print(abPath)


path = "C:\\Users\\burro\\Desktop\\Python Projects\\Python_Basic_projects\\Python_Drill"


list_dir = os.listdir(path)
for file in list_dir:
    print(file)


modification_time = os.path.getmtime(path)
print(modification_time)

local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)
