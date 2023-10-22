# import built in severless sql database system that come with python
import sqlite3

####### Remind: Split this class into multiple smaller classes base on entity #######
class SalesService:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.create_tables()
        self.seed_data()

    ### Create 5 Tables/Entities ###

    def create_tables(self):
        # Creating a cursor object to perform operations like update, delete, insert data into a table
        cursor = self.conn.cursor()

        # Create Products table with no duplication
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                products_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                manufacturer TEXT,
                style TEXT,
                purchase_price REAL,
                sale_price REAL,
                qty_on_hand INTEGER,
                commission_percentage REAL,
                UNIQUE(products_id, name)
            )
        ''')
        # Create salesperson table with no duplication
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS salesperson (
                salePerson_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                address TEXT,
                phone TEXT,
                start_date TEXT,
                termination_date TEXT,
                manager TEXT,
                UNIQUE(salePerson_id, first_name, last_name)
            )
        ''')
        # Create Customer table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer (
                customer_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                address TEXT,
                start_date TEXT
            )
        ''')
        # Create Sales table 
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY,
                product_id INTEGER,
                salePerson_id INTEGER,
                customer_id INTEGER,
                sale_date TEXT,
                price REAL,
                salesperson_commission REAL,
                FOREIGN KEY (product_id) REFERENCES products (products_id),
                FOREIGN KEY (salePerson_id) REFERENCES salesperson (salePerson_id),
                FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
                FOREIGN KEY (price) REFERENCES products (purchase_price)   
            )
        ''')
        # Create Discount table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS discount (
                discount_id INTEGER PRIMARY KEY,
                product_id INTEGER,
                begin_date TEXT,
                end_date TEXT,
                discount_percent REAL,
                FOREIGN KEY (product_id) REFERENCES products (products_id)
            )
        ''')
        self.conn.commit()

    ### add items into a table function (this is mainly to seed the sample data) ###

    def seed_data(self):
        cursor = self.conn.cursor()
        #cursor.execute('SELECT * FROM products WHERE name = ?', (self.products.name))
        #count = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM products')
        count = cursor.fetchone()[0]
        #print(count)

        # check to see if the products table is empty or not (checking the number of row)
        # if it is empty then it will seed sample data for testing, else it will not
        # this is to prevent duplicating multiple record everytime we run the code
        if count == 0:
            # Seed products table with sample data
            cursor.execute('''
                INSERT INTO products (name, manufacturer, style, purchase_price, sale_price, qty_on_hand, commission_percentage)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', ("Mountain Bike", "Trek", "Mountain", 800, 1200, 10, 10))

            cursor.execute('''
                INSERT INTO products (name, manufacturer, style, purchase_price, sale_price, qty_on_hand, commission_percentage)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', ("Road Bike", "Specialized", "Road", 1000, 1500, 15, 8))

            # Seed salesperson table with sample data
            cursor.execute('''
                INSERT INTO salesperson (first_name, last_name, address, phone, start_date, termination_date, manager)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', ("John", "Doe", "123 Main St", "555-123-4567", "2023-01-01", None, "Manager1"))

            cursor.execute('''
                INSERT INTO salesperson (first_name, last_name, address, phone, start_date, termination_date, manager)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', ("Jane", "Doe", "456 Elm St", "555-987-6543", "2023-03-15", "2024-01-01", "Manager1"))

            # Seed customer table with sample data
            cursor.execute('''
                INSERT INTO customer (first_name, last_name, address, start_date)
                VALUES (?, ?, ?, ?)
            ''', ("James", "Doe", "321 Main St", "2023-01-04"))

            cursor.execute('''
                INSERT INTO customer (first_name, last_name, address, start_date)
                VALUES (?, ?, ?, ?)
            ''', ("Joe", "Doe", "111 Main St", "2023-05-04"))

            self.conn.commit()

    
    ### Getter methods ###

    # getter method for products table
    def get_products(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products')
        return cursor.fetchall()
    
    # getter method for a product data using product_id
    def get_product_by_id(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products WHERE products_id = ?', (product_id,))
        product = cursor.fetchone()
        if product:
            dict = {
                'products_id' : product[0],
                'name' : product[1],
                'manufacturer' : product[2],
                'style' : product[3],
                'purchase_price' : product[4],
                'sale_price' : product[5],
                'qty_on_hand' : product[6],
                'commission_percentage' : product[7]
            }
            return dict
        else:
            return None
    
    #getter method for salesperson table
    def get_salesperson(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM salesperson')
        return cursor.fetchall()

    # getter method for a saleperson data using salePerson_id
    def get_saleperson_by_id(self, salePerson_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM salesperson WHERE salePerson_id = ?', (salePerson_id,))
        saleperson = cursor.fetchone()
        if saleperson:
            dict = {
                'salePerson_id' : saleperson[0],
                'first_name' : saleperson[1],
                'last_name' : saleperson[2],
                'address' : saleperson[3],
                'phone' : saleperson[4],
                'start_date' : saleperson[5],
                'termination_date' : saleperson[6],
                'manager' : saleperson[7]
            }
            return dict
        else:
            return None

    #getter method for customer table
    def get_customer(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM customer')
        return cursor.fetchall()
    
    # getter method for a customer data using customer_id
    def get_customer_by_id(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM customer WHERE customer_id = ?', (customer_id,))
        customer = cursor.fetchone()
        if customer:
            dict = {
                'customer_id' : customer[0],
                'first_name' : customer[1],
                'last_name' : customer[2],
                'address' : customer[3],
                'start_date' : customer[4]
            }
            return dict
        else:
            return None

    ### Update Table Methods ###

    # update method for salesperson
    def update_salesperson(self, salePerson_id, update):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE salesperson
            SET first_name=?, last_name=?, address=?, phone=?, start_date=?, termination_date=?, manager=?
            WHERE salePerson_id=?
        ''', (update['first_name'], update['last_name'], update['address'], update['phone'],
              update['start_date'], update['termination_date'], update['manager'], salePerson_id))
        self.conn.commit()

    # update method for products
    def update_products(self, products_id, update):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE products
            SET name=?, manufacturer=?, style=?, purchase_price=?, sale_price=?, qty_on_hand=?, commission_percentage=?
            WHERE products_id=?
        ''', (update['name'], update['manufacturer'], update['style'], update['purchase_price'],
              update['sale_price'], update['qty_on_hand'], update['commission_percentage'], products_id))
        self.conn.commit()


    ### Sales Helper Methods ###

    # Method to create sale entry (can be use to seed Sales entity)
    def create_sale(self, product_id, salePerson_id, customer_id, sale_date, price, salesperson_commission):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO sales (product_id, salePerson_id, customer_id, sale_date, price, salesperson_commission)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (product_id, salePerson_id, customer_id, sale_date, price, salesperson_commission))
        self.conn.commit()
    
    # getter method for a sale data using sale_id
    def get_sale_by_id(self, sale_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM sales WHERE sale_id = ?', (sale_id,))
        sale = cursor.fetchone()
        if sale:
            dict = {
                'sale_id' : sale[0],
                'product_id' : sale[1],
                'salePerson_id' : sale[2],
                'customer_id' : sale[3],
                'sale_date' : sale[4],
                'price' : sale[5],
                'salesperson_commission' : sale[6]
            }
            return dict
        else:
            return None
        
    # Method to find how many entry is in the Sale entity
    def sales_entity_num(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM sales')
        return cursor.fetchall()
