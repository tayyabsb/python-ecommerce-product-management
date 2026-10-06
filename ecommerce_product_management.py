print("===== E-COMMERCE PRODUCT MANAGEMENT SYSTEM =====")

products = []


def add_product():
    print("\n===== ADD PRODUCT =====")

    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    products.append(product)

    print("Product added successfully!")


def view_products():
    print("\n===== ALL PRODUCTS =====")

    if len(products) == 0:
        print("No products found.")
        return

    for product in products:
        print("----------------------------")
        print("Product ID:", product["id"])
        print("Name:", product["name"])
        print("Category:", product["category"])
        print("Price: $", product["price"])
        print("Stock:", product["stock"])


def search_product():
    print("\n===== SEARCH PRODUCT =====")

    product_id = input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:
            print("\nProduct Found!")
            print("Product ID:", product["id"])
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Price: $", product["price"])
            print("Stock:", product["stock"])
            return

    print("Product not found.")


def update_product():
    print("\n===== UPDATE PRODUCT =====")

    product_id = input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:

            print("Leave a field empty if you don't want to change it.")

            name = input("Enter new product name: ")
            category = input("Enter new category: ")
            price = input("Enter new price: ")
            stock = input("Enter new stock quantity: ")

            if name:
                product["name"] = name

            if category:
                product["category"] = category

            if price:
                product["price"] = float(price)

            if stock:
                product["stock"] = int(stock)

            print("Product updated successfully!")
            return

    print("Product not found.")


def delete_product():
    print("\n===== DELETE PRODUCT =====")

    product_id = input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Product deleted successfully!")
            return

    print("Product not found.")


def update_stock():
    print("\n===== UPDATE STOCK =====")

    product_id = input("Enter product ID: ")

    for product in products:
        if product["id"] == product_id:

            quantity = int(input("Enter new stock quantity: "))

            if quantity >= 0:
                product["stock"] = quantity
                print("Stock updated successfully!")
            else:
                print("Stock quantity cannot be negative.")

            return

    print("Product not found.")


def calculate_inventory_value():
    print("\n===== INVENTORY VALUE =====")

    if len(products) == 0:
        print("No products available.")
        return

    total_value = 0

    for product in products:
        total_value += product["price"] * product["stock"]

    print("Total Inventory Value: $", total_value)


while True:
    print("\n===== MAIN MENU =====")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Update Stock")
    print("7. Calculate Inventory Value")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_product()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        update_stock()

    elif choice == "7":
        calculate_inventory_value()

    elif choice == "8":
        print("Thank you for using E-Commerce Product Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
