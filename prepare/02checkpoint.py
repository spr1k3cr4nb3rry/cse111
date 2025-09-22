# Name: Izzie Vazquez
# Assignment Name: 02 Checkpoint: Calling Functions
# Assignment Description:
# A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
# Write a Python program named boxes.py that asks the user for two integers:
#   1. the number of manufactured items
#   2. the number of items that the user will pack per box
# Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may 
# be packed with fewer items than the other boxes.

import math

def boxes(manufactured_items, items_per_box):
    total_boxes = math.ceil(manufactured_items / items_per_box)
    print()
    print(f"For {manufactured_items} items, packing {items_per_box} items in each box, you will need {total_boxes} boxes.")

def main():
    mi = int(input("Enter the number of items: "))
    ipb = int(input("Enter the number of items per box: "))
    boxes(mi, ipb)

if __name__ == "__main__":
    main()