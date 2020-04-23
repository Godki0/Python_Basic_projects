
import os
import time


path = "C:\\Users\\burro\\Desktop\\Python Projects\\Python_Basic_projects\\Python_Drill"


list_dir = os.listdir(path)
for filename in list_dir:
    if filename.endswith(".txt"):
        print(filename)

f1Name = "1.txt"

f1Path = "C: \\Python_Drill\\"

abPath = os.path.join(f1Path, f1Name)
print(abPath)

f2Name = "2.txt"

f2Path = "C: \\Python_Drill\\"

cdPath = os.path.join(f2Path, f2Name)
print(cdPath)

modification_time = os.path.getmtime(path)
print(modification_time)

local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)
