def product_details(product_id, name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"ProductName: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
if __name__ == "__main__":
    pid = "P101"
    pname = "Laptop"
    qty = 5
    pr = 50000
    
    print(Product_Details(pid,pname,qty,pr))
