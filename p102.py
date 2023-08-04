import os
import shutil

from_dir = "C:/Users/Anike/Downloads"
to_dir = "C:/Users/Anike/Downloads/Downloads_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)



for i in list_of_files:
    root, ext = os.path.splitext(i)

    ext = ext[1:]
    
    if ext != "" :
        if os.path.exists(to_dir):
            shutil.move(from_dir +  '/' + i , to_dir + '/' + i)
            print("Moving " + i)

        else:
            os.makedirs(to_dir)
            shutil.move(from_dir +  '/' + i , to_dir + '/' + i)
            print("Moving " + i)