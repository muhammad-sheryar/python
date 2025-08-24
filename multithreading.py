#Python MultiThreading -> Multitasking (I/O) File Reading 

import threading
import time

def walk_dog(first,last):
    time.sleep(8)
    print(f"You Finish Walking The {first} {last}!")
    
def take_out_trash():
    time.sleep(2)
    print("You take Out The Trash!")
    
def get_mail():
    time.sleep(4)
    print("You Get the Mail!")
    
# walk_dog()
# take_out_trash()
# get_mail()

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()


print("All Chores are Completed!")