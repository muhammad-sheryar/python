#Python File Handling


import os

file_path = "C:/Users/computer lab/Desktop/text.txt"

if os.path.exists(file_path):
    print(f"The Location {file_path} Exist!")
    
    if os.path.isfile(file_path):
        print("This is a File!")
    
    elif os.path.isdir(file_path):
        print("This is Directory!")
    
else:
    print(f"The Location {file_path} Doesn't Exist!")
    
