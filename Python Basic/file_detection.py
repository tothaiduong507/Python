import os

path="F:\\TT HCM\\week1.txt"

if os.path.exists(path):
    print("Path exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("Path do not exist")