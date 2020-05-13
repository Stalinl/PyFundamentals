# https://www.simplifiedpython.net/python-get-files-in-directory/
import os

# specify your path of directory
path = r"C:\Users\Documents"

# call listdir() method
# path is a directory of which you want to list
directories = os.listdir(path)

# This would print all the files and directories
for file in directories:
    print(file)

with os.scandir(path) as dirs:
    for entry in dirs:
        print(entry.name)
