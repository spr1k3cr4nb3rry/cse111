# Name: Izzie Vazquez
# Assignment Name: 02 Prove Assignment: Calling Functions
# Assignment Description:
# The previous lesson’s prove milestone required you to write a program named tire_volume.py that computes the approximate volume of air inside a tire. Add code near the end of that program that does the following:
# 1. Gets the current date from the computer’s operating system.
# 2. Opens a text file named volumes.txt for appending.
# 3. Appends to the end of the volumes.txt file one line of text that contains the following five values: 
#   a. current date
#   b. width of the tire
#   c. aspect ratio of the tire
#   d. diameter of the wheel
#   e. volume of the tire

import math
from datetime import datetime

def tire_volume():
    width = int(input("Enter the width of the tire in mm (ex. 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex. 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex. 15): "))

    volume = (math.pi * (width ** 2) * (aspect_ratio * ((width * aspect_ratio) + (2540 * diameter)))) / 10000000000
    print(f"\nThe approximate volume is {volume:.2f} liters.")
    
    choice = input(f"\nWould you like to place an order for new tires with a volume of {volume:.2f}? (y/n) ")
    if choice == 'y':
        phone_number = input("Please enter a phone number for order: ")

    date = datetime.now()

    with open("prove/02assignment/volumes.txt", "at") as volfile:
        print(f"{date:%Y-%m-%d}, {phone_number}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volfile)   

def main():
    tire_volume()

if __name__ == "__main__":
    main()