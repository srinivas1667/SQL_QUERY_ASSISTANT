import sqlite3
import os

def create_database():

    DATABASE_PATH = os.path.join(os.getcwd(), "database.db")  # Adjust as needed
    conn = sqlite3.connect(DATABASE_PATH)

    #conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    # Create Products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Category TEXT,
        Price REAL,
        StockQuantity INTEGER
    )
    ''')

    # Create Customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        Email TEXT UNIQUE,
        RegistrationDate DATE
    )
    ''')

    # Create Orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY,
        CustomerID INTEGER,
        OrderDate DATE,
        TotalAmount REAL,
        Status TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    )
    ''')

    # Create OrderDetails table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS OrderDetails (
        OrderDetailID INTEGER PRIMARY KEY,
        OrderID INTEGER,
        ProductID INTEGER,
        Quantity INTEGER,
        Price REAL,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    )
    ''')

    # Insert expanded data into Products
    products = [
        ('Laptop', 'Electronics', 999.99, 50),
        ('Smartphone', 'Electronics', 699.99, 100),
        ('Headphones', 'Accessories', 149.99, 200),
        ('T-shirt', 'Clothing', 19.99, 500),
        ('Running Shoes', 'Footwear', 89.99, 150),
        ('Tablet', 'Electronics', 299.99, 80),
        ('Smartwatch', 'Electronics', 199.99, 100),
        ('Jacket', 'Clothing', 49.99, 300),
        ('Backpack', 'Accessories', 59.99, 250),
        ('Sunglasses', 'Accessories', 24.99, 400),
        ('Jeans', 'Clothing', 39.99, 350),
        ('Sneakers', 'Footwear', 129.99, 180),
        ('Bluetooth Speaker', 'Accessories', 99.99, 120),
        ('Camera', 'Electronics', 449.99, 70),
        ('Gaming Console', 'Electronics', 399.99, 90),
        ('Coffee Machine', 'Appliances', 79.99, 40),
        ('Blender', 'Appliances', 49.99, 60),
        ('Smart TV', 'Electronics', 899.99, 30),
        ('Desk Lamp', 'Furniture', 29.99, 200),
        ('Office Chair', 'Furniture', 149.99, 100)
    ]
    cursor.executemany('INSERT INTO Products (Name, Category, Price, StockQuantity) VALUES (?, ?, ?, ?)', products)

    # Insert expanded data into Customers
    customers = [
        ('John', 'Doe', 'john.doe@email.com', '2023-01-15'),
        ('Jane', 'Smith', 'jane.smith@email.com', '2023-02-20'),
        ('Bob', 'Johnson', 'bob.johnson@email.com', '2023-03-10'),
        ('Alice', 'Brown', 'alice.brown@email.com', '2023-04-05'),
        ('Tom', 'Wilson', 'tom.wilson@email.com', '2023-05-25'),
        ('Emily', 'Davis', 'emily.davis@email.com', '2023-06-30'),
        ('David', 'Martinez', 'david.martinez@email.com', '2023-07-15'),
        ('Jessica', 'Miller', 'jessica.miller@email.com', '2023-08-10'),
        ('Chris', 'Taylor', 'chris.taylor@email.com', '2023-09-01'),
        ('Sara', 'Lee', 'sara.lee@email.com', '2023-09-15'),
        ('Michael', 'White', 'michael.white@email.com', '2023-10-02'),
        ('Natalie', 'Green', 'natalie.green@email.com', '2023-10-10'),
        ('Lucas', 'King', 'lucas.king@email.com', '2023-10-15'),
        ('Olivia', 'Moore', 'olivia.moore@email.com', '2023-10-20')
    ]
    cursor.executemany('INSERT INTO Customers (FirstName, LastName, Email, RegistrationDate) VALUES (?, ?, ?, ?)', customers)

    # Insert expanded data into Orders
    orders = [
        (1, '2023-04-01', 1149.98, 'Completed'),
        (2, '2023-04-15', 699.99, 'Shipped'),
        (3, '2023-05-01', 169.98, 'Processing'),
        (4, '2023-06-10', 89.99, 'Completed'),
        (5, '2023-07-05', 249.98, 'Shipped'),
        (6, '2023-08-20', 549.97, 'Completed'),
        (7, '2023-09-10', 199.98, 'Processing'),
        (8, '2023-09-25', 129.99, 'Shipped'),
        (9, '2023-10-05', 999.99, 'Completed'),
        (10, '2023-10-12', 179.98, 'Shipped'),
        (11, '2023-10-18', 399.99, 'Processing'),
        (12, '2023-10-19', 899.99, 'Completed')
    ]
    cursor.executemany('INSERT INTO Orders (CustomerID, OrderDate, TotalAmount, Status) VALUES (?, ?, ?, ?)', orders)

    # Insert expanded data into OrderDetails
    order_details = [
        (1, 1, 1, 999.99),
        (1, 3, 1, 149.99),
        (2, 2, 1, 699.99),
        (3, 4, 2, 19.99),
        (3, 3, 1, 149.99),
        (4, 5, 1, 89.99),
        (5, 6, 1, 299.99),
        (5, 3, 1, 149.99),
        (6, 7, 1, 199.99),
        (6, 8, 1, 49.99),
        (7, 9, 2, 24.99),
        (8, 10, 1, 129.99),
        (9, 1, 1, 999.99),
        (10, 4, 2, 19.99),
        (11, 15, 1, 399.99),
        (12, 18, 1, 899.99)
    ]
    cursor.executemany('INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Price) VALUES (?, ?, ?, ?)', order_details)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
