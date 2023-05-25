import os
import shutil

from_dir = "C:\Users\chala\Downloads"              
to_dir = "C:\Users\chala\OneDrive\Desktop\downloads"


list_of_files = os.listdir(from_dir)
print(list_of_files)

path = list_of_files
root,extension=os.path.splitext(path)
print(root)
print(extension)
