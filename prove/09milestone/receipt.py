# Name: Izzie Vazquez
# Assignment Name: 09 Prove Milestone: Text Files
# Problem Statement:
# A local grocery store subscribes to an online service that enables its customers to order groceries
# online. After a customer completes an order, the online service sends a CSV file that contains the 
# customer’s requests to the grocery store. The store needs you to write a program that reads the CSV 
# file and prints a receipt in the terminal window that lists the purchased items and shows the subtotal, 
# the sales tax amount, and the total.
# Assignment:
# During this milestone, you will write half of a Python program named receipt.py that prints a receipt 
# in the terminal window for a customer’s grocery order. Specifically, by the end of this milestone, your 
# program must read and process these two CSV files:
# - The products.csv file is a catalog of all the products that the grocery store sells.
# - The request.csv file contains the items ordered by a customer.

import csv

def read_products(filename):
    products_dict = {}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            product_id = row[0]
            product_name = row[1]
            product_price = float(row[2])
            products_dict[product_id] = [product_id, product_name, product_price]
    return products_dict

def read_request(filename, products_dict):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            product_num = row[0]
            quantity = int(row[1])

            product = products_dict[product_num]

            name = product[1]
            price = product[2]

            print(f"{name}: {quantity} @ {price:.2f}")

def main():
    products_dict = read_products("prove/09milestone/products.csv")
    print("All Products")
    print(products_dict)

    print("\nRequested Items")
    read_request("prove/09milestone/request.csv", products_dict)

if __name__ == "__main__":
    main()