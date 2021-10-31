import os
import shutil

path = "C:/Users/Raghav/Desktop/all/Institute"
files = os.listdir(path)
print(files)

for i in files:
    name,ext = os.path.splitext(i)
    ext = ext[1:]
    if ext == " ":
        continue
    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + i, path + "/" + ext + "/" + i)
    else:
        os.mkdir(path + "/" + ext)
        shutil.move(path + "/" + i, path + "/" + ext + "/" + i)
