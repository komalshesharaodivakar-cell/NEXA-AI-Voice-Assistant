# ==========================================
# CHILD CLASS
# Single Inheritance
# ==========================================

# Import Product class from Product.py
from product import Product

# PhysicalProduct inherits Product
class PhysicalProduct(Product): #always create a constructor when creating a class

    # Constructor
    def __init__(self, name, description, price, weight):

        # Call Parent(Product) constructor
        super().__init__(name, description, price)

        # Store product weight
        self.weight = weight

    # Method Overriding
    def display_info(self):

        # Call Parent display_info()
        parent_info = super().display_info()

        # Return parent details + weight
        return (
            f"{parent_info}\n"
            f"Weight       : {self.weight} kg"
        )

p2=PhysicalProduct("laptop","15GB Ram",50000,50)
print(p2.display_info())