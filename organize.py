import os
import shutil
from_dir = "C:/Users/acer/Downloads"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    root,extension = os.path.splitext(i)
    print(root)
    print(extension)