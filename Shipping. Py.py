# ==========================================
# GRANDCHILD CLASS
# Multiple + Multilevel Inheritance
# ==========================================

# Import PhysicalProduct class
from PhysicalProduct import PhysicalProduct

# Import Warranty class
from warranty import Warranty

# Shipping inherits from PhysicalProduct and Warranty
class Shipping(PhysicalProduct, Warranty):

    # Constructor
    def __init__(self, name, description, price, weight, warranty_years):

        # Initialize Product and PhysicalProduct
        PhysicalProduct.__init__(self, name, description, price, weight)

        # Initialize Warranty class
        Warranty.__init__(self, warranty_years)

    # Calculate shipping cost
    def shipping_cost(self):

        # Shipping = Weight × 50
        return self.weight * 50