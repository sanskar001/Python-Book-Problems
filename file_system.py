# This  is python program to understand the concept of recursion.
# This is program to compute the disk usage for all files and folders(directories) nested 
# within a particular folder(directory).

import os  # importing the os library.

# This is recursive function for computing the disk usage for nested files and folder.

def disk_usage(path):
    
    total = os.path.getsize(path)      # for taking size of files.

    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total = total + disk_usage(childpath)       # for taking size of folders.
    
    print("{} KB".format(total//1024 + 1),path)
    return total

path = "D:\projects\Book_problem"        # given path.
disk_usage(path)