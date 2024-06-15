# Create a python program capable ofgreeting you with Good Morning, Good Afternoon 
#  and Good Evening. Your program should use time module to get the current hour.


import time

def greet():
    current_hour = time.localtime().tm_hour
    
    if 5 <= current_hour < 12:
        return "Good Morning!"
    elif 12 <= current_hour < 17:
        return "Good Afternoon!"
    elif 17 <= current_hour < 24:
        return "Good Evening!"
    else:
        return "Hello"

current_hour = time.localtime().tm_hour

print(greet())
