import csv
import datetime

PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
QUANTITY_INDEX = 1

SALES_TAX_RATE = .06

def main():
    try:
        ordered_products_list = []
        quantity_products_list = []

        products_dict = read_dict("products.csv", PRODUCT_NUMBER_INDEX)

        #print(products_dict)

        read_receipt("request.csv", ordered_products_list, quantity_products_list, products_dict)
        
        print_receipt(ordered_products_list, quantity_products_list)

    except FileNotFoundError as not_found_err:
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")

    except KeyError as key_err:
        print()
        print(type(key_err).__name__, key_err, sep=": ")
        print(f"The key does not exists in the dictionary.")
        print("Run the program again and enter a" \
                " valid key.")

    except PermissionError as per_err:
        print()
        print(type(per_err).__name__, per_err, sep=": ")
        print(f"You are not allowed to access this file.")
        print("Run the program again and enter the" \
                " name of an allowed file.")

    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")

def read_dict(filename, key_column_index):

    dict = {}

    with open(filename, "rt") as csv_file:
        read = csv.reader(csv_file)
        next(read)
    
        for row_list in read:
            key = row_list[key_column_index]
            
            dict[key] = row_list

    return dict

def read_receipt(filename, ordered_list, quantity_list, dict):

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            key = row_list[PRODUCT_NUMBER_INDEX] 

            ordered_list.append(dict[key])
            quantity_list.append(row_list[QUANTITY_INDEX])

def sum_items(list):

    items = 0

    for x in list:
       items += int(x)

    return items

def sum_subtotal(orders, quantity):

    subtotal_due = 0

    for x, product in enumerate(orders):
        subtotal_due += float(product[PRODUCT_PRICE_INDEX]) * int(quantity[x])


    return subtotal_due

def compute_sales_tax(subtotal):
    return subtotal * SALES_TAX_RATE

def print_receipt(orders_list, quantity_list):

    items = sum_items(quantity_list)
    subtotal_due = sum_subtotal(orders_list, quantity_list)
    total = compute_sales_tax(subtotal_due)

    current_date = datetime.datetime.now()

    store_name = input("Enter you store name: ")


    print("")
    print(f"-------------------------  {store_name} ---------------------------")

    for x, item in enumerate(orders_list):
        print(f"{x + 1}. {item[PRODUCT_NAME_INDEX]}")

    print(f"------------------  Number of ordered items  ------------------")
    print(items)
    print(f"------------------------  Subtotal Due  ------------------------")
    print(f"${round(subtotal_due, 2)}")
    print(f"--------------------------  Sales Tax  -------------------------")
    print(f"Sales tax: (6%): ${round(total, 2)}")
    print(f"----------------------------  Total  ---------------------------")
    print(f"Total: ${round(subtotal_due + total, 2)}")
    print(f"-----------------------------------------------------------------")
    print("")
    print(f"Thank you for shopping at the {store_name}.")
    print(f"Receipt issuance date and time: {current_date}")

if __name__ == "__main__":
    main()