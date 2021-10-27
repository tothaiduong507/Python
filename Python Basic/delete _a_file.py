import os
import shutil
try:
    #delete a file
    os.remove('F:\\TT HCM\\copy.txt')
    #delete an empty directory
    #os.rmdir(path)
    #delete directory containing files
    #shutil.rmtree(path);
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("U do not have the permission")
except OSError:
    print("You cannot delete that using that function")
else:
    print("File is removed")