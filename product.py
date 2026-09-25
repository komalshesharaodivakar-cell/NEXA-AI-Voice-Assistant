# ==========================================
# PARENT CLASS (Base Class)
# No inheritance starts here.
# ==========================================

# Parent Class
class Product:

    # Constructor - Automatically runs when object is created
    def __init__(self, name, description, price):   #underscore is mandatory then it will not show error

        # Store product name
        self.name = name     #attribute

        # Store product description
        self.description = description

        # Store product price
        self.price = price

    # Method to display product details
    def display_info(self):

        # Return formatted product information
        return (
            f"Product Name : {self.name}\n"
            f"Description  : {self.description}\n"
            f"Price        : ₹{self.price}"
        )

p1=Product("laptop","15GB Ram",50000)
print(p1.display_info())


