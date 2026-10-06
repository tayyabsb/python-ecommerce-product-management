🛒 E-Commerce Product Management System

A Python-based E-Commerce Product Management System designed to manage product records, pricing, stock quantities, and inventory value through an interactive command-line interface.

This project was developed as part of my Python learning journey to strengthen my understanding of functions, lists, dictionaries, loops, conditional statements, CRUD operations, searching, updating records, stock management, and menu-driven programming.

---

📌 Project Overview

Managing products and inventory is an essential part of an e-commerce system.

This project simulates a basic product management module where users can create and manage product records through a simple terminal-based interface.

The application allows users to:

- ➕ Add products
- 👀 View all products
- 🔍 Search products
- ✏️ Update product information
- 🗑️ Delete products
- 📦 Update stock quantities
- 💰 Calculate total inventory value
- 🚪 Exit the application

The current version stores product information temporarily in Python memory.

«Note: Product data is not permanently stored. All records are lost when the program is closed.»

---

✨ Features

➕ Add Product

Users can add a new product by providing:

- Product ID
- Product Name
- Category
- Price
- Stock Quantity

Each product is stored as a dictionary inside the product records list.

---

👀 View All Products

The system displays all available products and their information.

Each product includes:

- Product ID
- Product Name
- Category
- Price
- Stock Quantity

If no products exist, the application displays an appropriate message.

---

🔍 Search Product

Users can search for a specific product using its Product ID.

If a matching product is found, its complete information is displayed.

If the product does not exist, the system informs the user.

---

✏️ Update Product

Existing product information can be modified.

Users can update:

- Product Name
- Category
- Price
- Stock Quantity

The Product ID is used to locate the correct product.

Users can leave a field empty if they do not want to modify that particular value.

---

🗑️ Delete Product

Users can remove a product from the system by entering its Product ID.

If the product exists, it is permanently removed from the current program session.

---

📦 Update Stock

The stock management feature allows users to update the available quantity of a product.

For example:

Old Stock: 10
New Stock: 25

The system also prevents negative stock quantities.

---

💰 Calculate Inventory Value

The application can calculate the total value of all products currently in inventory.

The calculation is:

Inventory Value = Product Price × Stock Quantity

For multiple products:

Total Inventory Value =
(Product 1 Price × Stock 1)
+
(Product 2 Price × Stock 2)
+
...

This provides a simple overview of the monetary value of the current inventory.

---

🖥️ Application Menu

The main menu provides access to all available features:

===== MAIN MENU =====
1. Add Product
2. View All Products
3. Search Product
4. Update Product
5. Delete Product
6. Update Stock
7. Calculate Inventory Value
8. Exit

Enter your choice:

---

🛠️ Technologies Used

Technology| Purpose
Python| Application development
Lists| Storing multiple product records
Dictionaries| Representing individual products
Functions| Organizing application operations
Loops| Repeating menu operations
Conditional Statements| Controlling program logic
Command Line| User interface

---

🧠 Python Concepts Practiced

1. Variables

Variables are used to store product information, user input, calculations, and program state.

---

2. User Input

The "input()" function allows users to interact with the application.

product_id = input("Enter product ID: ")

---

3. Lists

A list is used to store multiple product dictionaries.

products = []

---

4. Dictionaries

Each product is represented using a dictionary:

product = {
    "id": product_id,
    "name": name,
    "category": category,
    "price": price,
    "stock": stock
}

This makes it possible to organize multiple properties of a product in one structure.

---

5. Functions

The program is divided into separate functions for better organization:

add_product()
view_products()
search_product()
update_product()
delete_product()
update_stock()
calculate_inventory_value()

This makes the application easier to understand, maintain, and expand.

---

6. Loops

A "while" loop keeps the main menu running until the user selects the exit option.

"for" loops are also used to search and process product records.

---

7. Conditional Statements

"if", "elif", and "else" statements control menu choices and application decisions.

---

8. CRUD Operations

The project demonstrates the basic CRUD pattern:

Operation| Project Feature
Create| Add Product
Read| View/Search Product
Update| Update Product/Stock
Delete| Delete Product

CRUD operations are fundamental to many real-world management systems.

---

📂 Project Structure

python-ecommerce-product-management/
│
├── ecommerce_product_management.py
│
└── README.md

"ecommerce_product_management.py"

Contains the complete Python implementation of the application.

"README.md"

Contains project documentation, features, setup instructions, concepts, examples, and future development plans.

---

⚙️ Requirements

The project has no external Python dependencies.

You only need:

- Python 3.x
- A terminal or command prompt
- A code editor or IDE

No external libraries are required.

---

🚀 How to Run

Step 1: Install Python

Make sure Python 3.x is installed on your system.

Check the installed version:

python --version

or:

python3 --version

---

Step 2: Clone the Repository

git clone https://github.com/tayyabsb/python-ecommerce-product-management.git

---

Step 3: Open the Project Directory

cd python-ecommerce-product-management

---

Step 4: Run the Application

python ecommerce_product_management.py

---

▶️ Example Usage

Adding a Product

===== ADD PRODUCT =====

Enter product ID: P101
Enter product name: Wireless Mouse
Enter product category: Electronics
Enter product price: 1500
Enter stock quantity: 10

Product added successfully!

---

Viewing Products

===== ALL PRODUCTS =====

----------------------------
Product ID: P101
Name: Wireless Mouse
Category: Electronics
Price: $ 1500.0
Stock: 10

---

Searching for a Product

===== SEARCH PRODUCT =====

Enter product ID: P101

Product Found!
Product ID: P101
Name: Wireless Mouse
Category: Electronics
Price: $ 1500.0
Stock: 10

---

Updating Product Information

===== UPDATE PRODUCT =====

Enter product ID: P101

Leave a field empty if you don't want to change it.

Enter new product name: Gaming Wireless Mouse
Enter new category: Gaming
Enter new price: 2000
Enter new stock quantity: 15

Product updated successfully!

---

Updating Stock

===== UPDATE STOCK =====

Enter product ID: P101
Enter new stock quantity: 25

Stock updated successfully!

---

Calculating Inventory Value

Suppose the inventory contains:

Product Price = 2000
Stock Quantity = 25

Then:

Inventory Value = 2000 × 25
                = 50000

The application displays:

===== INVENTORY VALUE =====

Total Inventory Value: $ 50000.0

---

🔄 Application Workflow

                    START
                      │
                      ▼
                Display Menu
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
     Add Product    View       Search
                    Products    Product
          │           │           │
          └───────────┼───────────┘
                      │
                      ▼
                Update Product
                      │
                      ▼
                Delete Product
                      │
                      ▼
                 Update Stock
                      │
                      ▼
             Inventory Value
                      │
                      ▼
                Return to Menu
                      │
                      ▼
                    Exit
                      │
                      ▼
                     END

---

🎯 Learning Objectives

The main objective of this project was to transform basic Python programming concepts into a practical application.

Through this project, I practiced:

- Designing a menu-driven application
- Creating reusable functions
- Managing collections of data
- Working with lists and dictionaries
- Implementing CRUD operations
- Searching records
- Updating records
- Deleting records
- Managing inventory quantities
- Performing calculations
- Handling user input
- Organizing application logic

---

📚 What I Learned

This project helped me understand how different Python concepts work together in a real-world style application.

Instead of working with isolated programming exercises, I used:

Functions + Lists + Dictionaries + Loops + Conditions + CRUD Logic

to create a complete product management system.

It also introduced me to an important concept used in larger applications: managing structured records and performing operations on them.

---

⚠️ Current Limitations

This project is intentionally designed as a beginner-to-intermediate Python application.

Current limitations include:

- Data is stored only in memory.
- Data is lost when the application closes.
- No database is connected.
- No user authentication system.
- No shopping cart.
- No payment processing.
- No customer management.
- No graphical user interface.
- Basic input validation.
- Terminal-based interface.

These limitations provide opportunities for future development.

---

🚀 Future Improvements

Version 2 — File Storage

Product records could be permanently stored using:

- JSON
- CSV
- Text files

---

Version 3 — SQLite Database

The application can be upgraded to use an SQLite database.

Possible database tables:

Products
Customers
Orders
Categories

This would allow product information to remain available after restarting the application.

---

Version 4 — Shopping Cart

A shopping cart system could be added with features such as:

- Add product to cart
- Remove product from cart
- Update quantity
- Calculate subtotal
- Calculate total
- Generate order summary

---

Version 5 — Customer Management

Customer features could include:

- Customer registration
- Customer profiles
- Customer orders
- Order history

---

Version 6 — Authentication

User authentication could be introduced for:

- Admin
- Customer

Admins could manage products while customers could browse and purchase products.

---

Version 7 — GUI Application

A graphical interface could be developed using Python GUI frameworks such as:

- Tkinter
- PyQt

This would make the application more user-friendly.

---

Version 8 — Web-Based E-Commerce System

The project could eventually be transformed into a web application using technologies such as:

- Python
- Flask or Django
- HTML
- CSS
- JavaScript
- SQLite or another database

This would turn the current command-line project into a complete web-based e-commerce application.

---

🗺️ Development Roadmap

Basic Python Projects
        │
        ▼
Product Management System
        │
        ▼
File-Based Product Storage
        │
        ▼
SQLite Database
        │
        ▼
Shopping Cart
        │
        ▼
Customer Management
        │
        ▼
Authentication
        │
        ▼
Web-Based E-Commerce Application

---

🔐 Disclaimer

This project is developed for educational and portfolio purposes.

It is not a production-ready e-commerce platform and does not implement real payment processing, authentication security, database security, encryption, or other requirements necessary for a production e-commerce system.

No real customer or payment information should be entered into this application.

---

🌟 Why I Built This Project

I built this project to move beyond basic Python exercises and create something that represents a real-world business use case.

E-commerce platforms depend heavily on product and inventory management, making this project a useful way to practice programming concepts in a practical context.

This project is another step in my journey of learning through building practical applications rather than only studying programming concepts theoretically.

---

📈 Project Progression

This project follows my progression from basic Python applications toward more structured and practical software:

Python Calculator
        ↓
Password Generator
        ↓
Student Grade Calculator
        ↓
Banking Management System
        ↓
Student Management System
        ↓
E-Commerce Product Management System
        ↓
Database-Based Applications
        ↓
Advanced Software Projects

Each project builds upon concepts learned in previous projects.

---

👨‍💻 Author

Muhammad Tayyab

Computer Science Student & Developer

Interested in:

- Python
- Web Development
- Software Development
- SEO
- Artificial Intelligence
- Programming & Technology

Connect With Me

- GitHub: "@tayyabsb" (https://github.com/tayyabsb)
- LinkedIn: "Muhammad Tayyab" (https://www.linkedin.com/in/muhammad-tayyab-3918a63a6)

---

⭐ Support

If you find this project useful for learning Python or understanding basic product management systems, consider giving the repository a ⭐.

More projects and improvements will be added as I continue my programming and development journey.

---

Built with Python 🐍 | Developed for Learning & Growth 🚀
