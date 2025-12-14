import pytest
from product_det import get_product_info

def test_employee_details():
    # Sample data
    name = "smart watch"
    emp_id = "123"
    department = "4"
    salary = "550"

    expected_output = (
        "product Name:smart watch,"
        "product ID:123,"
        "Quantity:4,"
        "Price:550.00"
    )

    # Assertion
    assert get_product_info(product_name, product_id, quantity, price) == expected_output
