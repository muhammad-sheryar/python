#Python Reading Files

import json
import csv

file_path = "C:/Users/computer lab/Desktop/sherry.csv"

try:

    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
        # print(content['Sherry'])
        
except FileNotFoundError:
    print("File Not Found!")
    
except PermissionError:
    print("Do Not Have Permission!")
    