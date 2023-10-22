from service import SalesService
#import pandas as pd

sales_service = SalesService('sales.db')

# Display a list of salesperson
def display_salesperson():
    salesperson = sales_service.get_salesperson()
    if salesperson:
        print("List of salesperson:\n")
        formatted_row = '{:<10} {:<10} {:<10} {:<20} {:<20} {:<20} {:<20} {:<20}'
        print(formatted_row.format("ID", "First Name", "Last Name", "Address", "Phone", "Start Date", "Termination Date", "Manager"))
        for person in salesperson:
            person = [str(x) for x in person]
            print(formatted_row.format(*person))
        # print("List of salesperson:")
        # for person in salesperson:
        #     print(f"ID: {person[0]}, First Name: {person[1]}, Last Name: {person[2]}, Address: {person[3]}, Phone: {person[4]}, Start Date: {person[5]}, Termination Date: {person[6]}, Manager: {person[7]}")
    else:
        print("No salesperson found.")

# Update a salesperson 
def update_salesperson_Input():
    salePerson_id = int(input("Enter the ID of the salesperson to update: "))
    update = {
        'first_name': input("First Name: "),
        'last_name': input("Last Name: "),
        'address': input("Address: "),
        'phone': input("Phone: "),
        'start_date': input("Start Date: "),
        'termination_date': input("Termination Date: "),
        'manager': input("Manager: ")
    }
    sales_service.update_salesperson(salePerson_id, update)
    print("Salesperson updated successfully")


# Display a list of products
def display_products():
    products = sales_service.get_products()
    if products:
        print("List of Products:\n")
        formatted_row = '{:<10} {:<15} {:20} {:<20} {:<20} {:<20} {:<20} {:<20}'
        print(formatted_row.format("ID", "Name", "Manufacturer", "Style", "Purchase Price", "Sale Price", "Quantity", "Commission Percentage"))
        for product in products:
            print(formatted_row.format(*product))
        # print("List of Products:")
        # for product in products:
        #     print(f"ID: {product[0]}, Name: {product[1]}, Manufacturer: {product[2]}, Style: {product[3]}, Purchase Price: ${product[4]}, Sale Price: ${product[5]}, Quantity: {product[6]}, Commission Percentage: {product[7]}")
    else:
        print("No products found")

# Update a product 
def update_products_Input():
    products_id = int(input("Enter the ID of the product to update: "))
    update = {
        'name': input("Name: "),
        'manufacturer': input("Manufacturer: "),
        'style': input("Style: "),
        'purchase_price': input("Purchase Price: "),
        'sale_price': input("Sale Price: "),
        'qty_on_hand': input("Quantity On Hand: "),
        'commission_percentage': input("Commission Percentage: ")
    }
    sales_service.update_products(products_id, update)
    print("Product updated successfully")


# Display a list of customers
def display_customers():
    customers = sales_service.get_customer()
    # print(customers)
    # print(pd.DataFrame(customers))
    if customers:
        print("List of customers:\n")
        formatted_row = '{:<10} {:<10} {:<10} {:<10} {:<10}'
        print(formatted_row.format("ID", "First Name", "Last Name", "Address", "Start Date"))
        for customer in customers:
            print(formatted_row.format(*customer))
        # print("List of customers:")
        # for customer in customers:
        #     print(f"ID: {customer[0]}, First Name: {customer[1]}, Last Name: {customer[2]}, Address: {customer[3]}, Start Date: {customer[4]}")
    else:
        print("No customer found.")


# Create a sale
def create_sale_Input():
    product_id = int(input("Enter the ID of the product being sold: "))
    salesperson_id = int(input("Enter the ID of the salesperson making the sale: "))
    customer_id = int(input("Enter the ID of the customer: "))
    sale_date = input("Enter the sale date (YYYY-MM-DD): ")
    price = float(input("Enter the sale price: "))
    
    # Calculate salesperson commission (based on product commission percentage and price)
    product = sales_service.get_product_by_id(product_id)
    if product:
        commission_percentage = product['commission_percentage']
        salesperson_commission = price * (commission_percentage / 100)
        
        # Create the sale
        sales_service.create_sale(product_id, salesperson_id, customer_id, sale_date, price, salesperson_commission)
        print("sale has been created")
    else:
        print("product does not exist in the database")


# Display a list of sales
def display_sales():
    entries_num = sales_service.sales_entity_num()[0][0]
    formatted_row = '{:<15} {:<20} {:<20} {:<15} {:<10} {:<20} {:<25} {:<25}'
    print("List of sales:\n")
    print(formatted_row.format("Product Name", "Customer First Name", "Customer Last Name", "Sale Date", "Price", "Salesperson First Name", "Salesperson Last Name", "Salesperson Commission"))
    for id in range(1, entries_num + 1):
        sales_data_product = sales_service.get_product_by_id(id)
        sales_data_salesperson = sales_service.get_saleperson_by_id(id)
        sales_data_customer = sales_service.get_customer_by_id(id)
        sales_data_sale = sales_service.get_sale_by_id(id)

        print(formatted_row.format(sales_data_product['name'], sales_data_customer['first_name'],  sales_data_customer['last_name'], sales_data_sale['sale_date'], sales_data_sale['price'], sales_data_salesperson['first_name'], sales_data_salesperson['last_name'], sales_data_sale['salesperson_commission']))


def main():
    while True:
        print("\nMenu:")
        print("1. Display List of salesperson")
        print("2. Display List of Products")
        print("3. Update a salesperson")
        print("4. Update a product")
        print("5. Display a list of customers")
        print("6. Create a sale")
        print("7. Display a list of sales")
        print("0. Exit")

        choice = input("Enter your choice: ")

        dictFunc = {
            '1': display_salesperson,
            '2': display_products,
            '3': update_salesperson_Input,
            '4': update_products_Input,
            '5': display_customers,
            '6': create_sale_Input,
            '7': display_sales
        }

        if choice == '0':
            print("Exiting")
            break
        else:
            dictFunc[choice]()


if __name__ == "__main__":
    main()
