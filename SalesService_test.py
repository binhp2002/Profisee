from service import SalesService
import sqlite3

sales_service = SalesService('sales.db')

def test_get_product_by_id_first_entry_before_update():
    expected_result = {'products_id': 1, 'name': 'Mountain Bike', 'manufacturer': 'Trek', 'style': 'Mountain', 'purchase_price': 800.0, 'sale_price': 1200.0, 'qty_on_hand': 10, 'commission_percentage': 10.0}
    test_result = sales_service.get_product_by_id(1)

    assert test_result == expected_result

def test_get_saleperson_by_id_first_entry_before_update():
    expected_result = {'salePerson_id': 1, 'first_name': 'John', 'last_name': 'Doe', 'address': '123 Main St', 'phone': '555-123-4567', 'start_date': '2023-01-01', 'termination_date': 'None', 'manager': 'Manager1'}
    test_result = sales_service.get_saleperson_by_id(1)

    assert test_result == expected_result

def test_get_customer_by_id_first_entry_before_update():
    expected_result = {'customer_id': 1, 'first_name': 'James', 'last_name': 'Doe', 'address': '321 Main St', 'start_date': '2023-01-04'}
    test_result = sales_service.get_customer_by_id(1)

    assert test_result == expected_result

def test_get_products_correct_number_of_entry():
    # because we seed 2 entry in the products entity, this doesn't change
    expected_result = 2
    test_result = len(sales_service.get_products())

    assert test_result == expected_result

def test_get_salesperson_correct_number_of_entry():
    # because we seed 2 entry in the salesperson entity, this doesn't change
    expected_result = 2
    test_result = len(sales_service.get_salesperson())

    assert test_result == expected_result

def test_get_customer_correct_number_of_entry():
    # because we seed 2 entry in the customer entity, this doesn't change
    expected_result = 2
    test_result = len(sales_service.get_customer())

    assert test_result == expected_result


if __name__ == "__main__":
    test_get_product_by_id_first_entry_before_update()
    test_get_saleperson_by_id_first_entry_before_update()
    test_get_customer_by_id_first_entry_before_update()
    test_get_products_correct_number_of_entry()
    test_get_salesperson_correct_number_of_entry()
    test_get_customer_correct_number_of_entry()
    print("Everything passed")