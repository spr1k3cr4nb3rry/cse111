# Name: Izzie Vazquez
# Assignment Name: 10 Prove Assignment: Handling Exceptions
# Problem Statement:
# A local grocery store subscribes to an online service that enables its customers to order groceries 
# online. After a customer completes an order, the online service sends a CSV file that contains the 
# customer’s requests to the grocery store. The store needs you to write a program that reads the CSV 
# file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, 
# the sales tax amount, and the total.
# Assignment:
# During the prove milestone for the previous lesson, you wrote the part of this program that reads and 
# processes two CSV files, one named products.csv that contains a catalog of products and one named 
# request.csv that contains a customer’s order. During this prove assignment, you will add code to 
# finish printing a receipt and to handle any exceptions that might occur while your program is running. 
# Specifically, your program must do the following:
#      1. Print the store’s name at the top of the receipt.
#      2. Print the list of ordered items.
#      3. Sum and print the number of ordered items.
#      4. Sum and print the subtotal due.
#      5. Compute and print the sales tax amount. Use 6% as the sales tax rate.
#      6. Compute and print the total amount due.
#      7. Print a thank you message.
#      8. Get the current date and time from your computer’s operating system and print the current date and time.
#      9. Include a try block and except blocks to handle FileNotFoundError and KeyError.

import csv
from datetime import datetime
import random

def read_products(filename):
    products_dict = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                product_id = row[0]
                product_name = row[1]
                product_price = float(row[2])
                products_dict[product_id] = [product_id, product_name, product_price]
        return products_dict
    except FileNotFoundError as e:
        print(f"Error: Filename {e} was not found.")
        exit()

def read_request(filename, products_dict):
    total_items = 0
    subtotal = 0.0
    sales_tax_rate = 0.06
    total = 0.0
    purchased_items = []

    print("Inkom Emporium\n")
    
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                product_num = row[0]
                quantity = int(row[1])

                product = products_dict[product_num]

                name = product[1]
                price = product[2]

                total_items += quantity
                subtotal += price * quantity
                purchased_items.append(name)


                print(f"{name}: {quantity} @ ${price:.2f}")

            sales_tax = subtotal * sales_tax_rate
            total = subtotal + sales_tax

            print(f"\nNumber of Items: {total_items}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${sales_tax:.2f}")
            print(f"Total: ${total:.2f}")
            print("\nThank you for shopping at Inkom Emporium.")

            current_datetime = datetime.now()
            print(current_datetime.strftime("%a %b %d %H:%M:%S %Y"))

            if purchased_items:
                coupon_item = (random.choice(purchased_items))
                print(f"\nCOUPON: 10% off your next purchase of {coupon_item}!")

    except FileNotFoundError as e:
        print(f"Error: Filename {e} was not found.")
        exit()
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file:", e)
        exit()

def main():
    products_dict = read_products("prove/10assignment/products.csv")
    read_request("prove/10assignment/request.csv", products_dict)

if __name__ == "__main__":
    main()