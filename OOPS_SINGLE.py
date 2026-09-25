# =========================================================
# PRODUCT MANAGEMENT SYSTEM
# OOP CONCEPTS IN ONE PROGRAM
# Concepts:
# 1. Class
# 2. Object
# 3. Constructor
# 4. Inheritance
# 5. Single Inheritance
# 6. Multiple Inheritance
# 7. Multilevel Inheritance
# 8. Method Overriding
# =========================================================


# =========================================================
# PARENT CLASS (Base Class)
# Inheritance starts from this class
# =========================================================

class Product:

    # Constructor - Automatically executes when object is created
    def __init__(self, name, description, price):

        # Store product name
        self.name = name

        # Store product description
        self.description = description

        # Store product price
        self.price = price

    # Method to display product details
    def display_info(self):

        # Return product information
        return (
            f"Product Name : {self.name}\n"
            f"Description  : {self.description}\n"
            f"Price        : ₹{self.price}"
        )


# =========================================================
# CHILD CLASS
# SINGLE INHERITANCE STARTS HERE
# PhysicalProduct inherits Product
# =========================================================

class PhysicalProduct(Product):

    # Constructor
    def __init__(self, name, description, price, weight):

        # Call Parent(Product) constructor
        super().__init__(name, description, price)

        # Store product weight
        self.weight = weight

    # Method Overriding
    def display_info(self):

        # Get parent information
        parent_info = super().display_info()

        # Add weight information
        return (
            f"{parent_info}\n"
            f"Weight       : {self.weight} kg"
        )


# =========================================================
# ANOTHER PARENT CLASS
# Used for Multiple Inheritance
# =========================================================

class Warranty:

    # Constructor
    def __init__(self, warranty_years):

        # Store warranty period
        self.warranty_years = warranty_years

    # Display warranty details
    def warranty_info(self):

        # Return warranty
        return f"Warranty     : {self.warranty_years} Years"


# =========================================================
# GRANDCHILD CLASS
# MULTIPLE INHERITANCE:
# Shipping inherits PhysicalProduct and Warranty
#
# MULTILEVEL INHERITANCE:
# Product → PhysicalProduct → Shipping
# =========================================================

class Shipping(PhysicalProduct, Warranty):

    # Constructor
    def __init__(self, name, description, price, weight, warranty_years):

        # Initialize Product and PhysicalProduct
        PhysicalProduct.__init__(self, name, description, price, weight)

        # Initialize Warranty
        Warranty.__init__(self, warranty_years)

    # Calculate shipping cost
    def shipping_cost(self):

        # Shipping Cost = Weight × 50
        return self.weight * 50


# =========================================================
# OBJECT CREATION
# =========================================================

# First Product Object
product1 = Shipping(
    "Laptop",
    "16GB RAM, 512GB SSD",
    65000,
    2.5,
    2
)

# Second Product Object
product2 = Shipping(
    "Mobile",
    "8GB RAM, 256GB Storage",
    25000,
    0.5,
    1
)

# Third Product Object
product3 = Shipping(
    "Printer",
    "Wireless Color Printer",
    12000,
    5,
    3
)


# =========================================================
# DISPLAY PRODUCT 1
# =========================================================

print("========== PRODUCT 1 ==========")
print(product1.display_info())
print(product1.warranty_info())
print("Shipping Cost : ₹", product1.shipping_cost())

print()

# =========================================================
# DISPLAY PRODUCT 2
# =========================================================

print("========== PRODUCT 2 ==========")
print(product2.display_info())
print(product2.warranty_info())
print("Shipping Cost : ₹", product2.shipping_cost())

print()

# =========================================================
# DISPLAY PRODUCT 3
# =========================================================

print("========== PRODUCT 3 ==========")
print(product3.display_info())
print(product3.warranty_info())
print("Shipping Cost : ₹", product3.shipping_cost())