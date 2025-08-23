#Python Write Files

import os

# txt_data = "I like BMW!"

# employees = ["Sherry", "Patrick", "Saleh", "Ronaldo"]

# file_path = "C:/Users/computer lab/Desktop/sherry.txt"

# try:

#     with open(file_path, "a") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         # file.write("\n" + employees)
#         print(f"txt file '{file_path} created!")
        
# except FileExistsError:
#     print("Already Exist!")


import json
# employees = {
#              "Sherry" : "Cashier",
#              "Patrick" :  "Manager",
#              "Saleh" : "Worker",
#              "Ronaldo": "Teacher"
#              }

# file_path = "C:/Users/computer lab/Desktop/sherry.json"

# try:

#     with open(file_path, "a") as file:
#         json.dump(employees, file, indent=4)
#         # file.write("\n" + employees)
#         print(f"json file '{file_path} created!")
        
# except FileExistsError:
#     print("Already Exist!")

import csv
employees = [["Name", "Age", "Job"],
             ["Sherry", 25, "Developer"],
             ["Jerry", 20, "Designer"],
             ["Tom", 23, "Manager"]
             ]

file_path = "C:/Users/computer lab/Desktop/sherry.csv"

try:

    with open(file_path, "w", newline= "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        # file.write("\n" + employees)
        print(f"csv file '{file_path} created!")
        
except FileExistsError:
    print("Already Exist!")