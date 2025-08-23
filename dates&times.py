#Python Dates & Times

import datetime

date = datetime.date(2025, 1, 2)

today = datetime.date.today()

time = datetime.time(12, 30, 0)

now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%y")

# print(today)
# print(date)
# print(time)
# print(now)


target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target Date Has Passed!")
   
else:   
    print("Target Date Has Passed!")