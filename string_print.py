def product():
    product_name = input("Enter the Product Name: ")
    product_code = input("Enter the Product Code: ")
    price = int(input("Enter the product price: "))
    print("The " + product_name + " with " + product_code + " is sold as Rs." + str(price))
product()
