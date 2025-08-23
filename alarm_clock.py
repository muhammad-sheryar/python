#Python Alarm Clock 


import time
import datetime
import pygame



def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "east_duo.mp3"
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("WAKE UP! 😆")
            
            is_running = False
        
        time.sleep(1)
       

if __name__ == "__main__":
    alarm_time = input("Enter the Alarm Time (HH:MM:SS): ")
    set_alarm(alarm_time)
    