import time
import os

# Function to print string as if typing so that people (mainly me) dont have to read a wall of text
def type_print(string, delay = 0.06):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

# Clear the terminal for easier reading
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_number(string_check):
    if string_check.isdigit() == True:
        return True
    else:
        return False