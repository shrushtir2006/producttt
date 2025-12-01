def product_details(name, p_id, quantity, price):
    result = (
        f"Product Name: {name}\n"
        f"Product ID: {p_id}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result

if __name__ == "__main__":
   
        name = "Shampoo\n"
        p_id = "E1001\n"
        quantity = "3\n"
        price = 1000

        print(product_details(name, p_id, quantity, price))