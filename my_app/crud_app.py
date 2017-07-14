import csv

products = []
products_csv_file_path = "data/products.csv"
headers = ["id", "name", "aisle", "department", "price"] # for "Further Exploration" use: ["product_id", "product_name", "aisle_id", "aisle_name", "department_id", "department_name", "price"]
user_input_headers = [header for header in headers if header != "id"] # don't prompt the user for the product_id

def read_products_from_file(products_csv = products_csv_file_path):
    with open(products_csv, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ordered_dict in reader:
            products.append(dict(ordered_dict))

def write_products_to_file(products_csv = products_csv_file_path):
    with open(products_csv, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def get_product_id(product): return int(product["id"])

def auto_incremented_id():
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1

def list_products():
    print("LISTING PRODUCTS HERE")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("READING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product)

def create_product():
    print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
    product = {"id": auto_incremented_id() }
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT HERE", product)

def update_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

def destroy_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT HERE", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

menu = """
-----------------------------------
PRODUCTS APPLICATION
-----------------------------------

Welcome @s2t2!

operation | description
--------- | ------------------
'List'    | Display a list of product identifiers and names.
'Show'    | Show information about a product.
'Create'  | Add a new product.
'Update'  | Edit an existing product.
'Destroy' | Delete an existing product.

Please select an operation: """ # end of multi- line string

def run():
    read_products_from_file()
    crud_operation = input(menu)
    if crud_operation.title() == "List":
        list_products()
    elif crud_operation.title() == "Show":
        show_product()
    elif crud_operation.title() == "Create":
        create_product()
    elif crud_operation.title() == "Update":
        update_product()
    elif crud_operation.title() == "Destroy":
        destroy_product()
    else:
        print("OOPS SORRY. PLEASE TRY AGAIN.")
    write_products_to_file()


# don't run this app unless this script is executed from the command line.
# this strategy allows us to test the app's component functions without asking for user input
if __name__ == "__main__": # "if this script is run from the command-line"
    run()
