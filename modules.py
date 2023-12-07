# Importing the datetime module
import datetime

# Getting the current date and time
current_datetime = datetime.datetime.now()

# Displaying the current date and time
print("Current Date and Time:", current_datetime)

# Accessing specific components of the datetime object
print("Current Year:", current_datetime.year)
print("Current Month:", current_datetime.month)
print("Current Day:", current_datetime.day)
print("Current Hour:", current_datetime.hour)
print("Current Minute:", current_datetime.minute)
print("Current Second:", current_datetime.second)




def greet(name):
    return f"Hello, {name}!"

def add_numbers(i, b):
    return i + b


import main as mm

print(mm.greet("Begimai"))
print(mm.add_numbers(9, 6))