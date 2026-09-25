# ==========================================
# PRODUCT MANAGEMENT SYSTEM
# ABSTRACT CLASS + POLYMORPHISM
# ==========================================

# Import Abstract Base Class and Abstract Method
from abc import ABC, abstractmethod


# ==========================================
# ABSTRACT PARENT CLASS
# ==========================================

class Product(ABC):

    # Class Variable (Common for all products)
    company = "Flipkart"

    # Constructor (Automatically called when object is created)
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # Normal Method (Inherited by all child classes)
    def display_product(self):
        print("\n========== PRODUCT DETAILS ==========")
        print("Company      :", Product.company)
        print("Product Name :", self.name)
        print("Price        :", self.price)
        print("Stock        :", self.stock)

    # Abstract Method
    # Every child class MUST implement this method
    @abstractmethod
    def warranty(self):
        pass

    # Abstract Method
    # Every child class MUST implement this method
    @abstractmethod
    def final_price(self):
        pass


# ==========================================
# CHILD CLASS 1 - ELECTRONICS
# ==========================================

class Electronics(Product):

    # Constructor
    def __init__(self, name, price, stock, warranty_years):
        # Call Parent Constructor
        super().__init__(name, price, stock)
        self.warranty_years = warranty_years

    # Overriding Abstract Method
    def warranty(self):
        print("Warranty     :", self.warranty_years, "Years")

    # Overriding Abstract Method
    def final_price(self):
        discount = self.price * 0.10
        final = self.price - discount

        print("10% Discount :", discount)
        print("Final Price  :", final)


# ==========================================
# CHILD CLASS 2 - FURNITURE
# ==========================================

class Furniture(Product):

    # Constructor
    def __init__(self, name, price, stock, service_years):
        # Call Parent Constructor
        super().__init__(name, price, stock)
        self.service_years = service_years

    # Overriding Abstract Method
    def warranty(self):
        print("Free Service :", self.service_years, "Years")

    # Overriding Abstract Method
    def final_price(self):
        delivery = 500
        final = self.price + delivery

        print("Delivery Fee :", delivery)
        print("Final Price  :", final)


# ==========================================
# CHILD CLASS 3 - CLOTHING
# ==========================================

class Clothing(Product):

    # Constructor
    def __init__(self, name, price, stock, return_days):
        # Call Parent Constructor
        super().__init__(name, price, stock)
        self.return_days = return_days

    # Overriding Abstract Method
    def warranty(self):
        print("Warranty     : No Warranty")
        print("Return Policy:", self.return_days, "Days")

    # Overriding Abstract Method
    def final_price(self):
        discount = self.price * 0.20
        final = self.price - discount

        print("20% Discount :", discount)
        print("Final Price  :", final)


# ==========================================
# POLYMORPHISM FUNCTION
# Same Function - Different Behaviour
# ==========================================

def show_product(product):

    print("\n====================================")
    print("Displaying Product Information")
    print("Product Type :", type(product).__name__)
    print("====================================")

    # Parent Class Method
    product.display_product()

    # Child Class Method
    product.warranty()

    # Child Class Method
    product.final_price()

    print("====================================")


# ==========================================
# OBJECT CREATION
# ==========================================

product1 = Electronics("Laptop", 55000, 15, 2)
product2 = Furniture("Office Chair", 8000, 20, 3)
product3 = Clothing("T-Shirt", 999, 40, 7)


# ==========================================
# POLYMORPHISM
# Same Function Calls Different Methods
# Based On Object Type
# ==========================================

show_product(product1)
show_product(product2)
show_product(product3)