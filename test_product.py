from employee import employee_details
def test_employee_details():
    expected_output = (
        "product name: Alice\n"
        "product ID: E1001\n"
        "quantity: 3\n"
        "price: 1000"
    )
    
    assert employee_details("Alice", "E1001", "3", "1000") == expected_output