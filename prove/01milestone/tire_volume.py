# Name: Izzie Vazquez
# Assignment Name: 01 Prove Milestone: Review Python
# Assignment Description:
# Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.

import math

def tire_volume():
    width = int(input("Enter the width of the tire in mm (ex. 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = (math.pi * (width ** 2) * (aspect_ratio * ((width * aspect_ratio) + (2540 * diameter)))) / 10000000000
    print(f"\nThe approximate volume is {volume:.2f} liters.")

def main():
    tire_volume()

if __name__ == "__main__":
    main()