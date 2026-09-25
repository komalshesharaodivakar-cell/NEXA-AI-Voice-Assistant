# ==========================================================
# AMAZON CUSTOMER MANAGEMENT SYSTEM
# COMPLETE NESTED DICTIONARY (WITH SIMPLE COMMENTS)
# ==========================================================

# A dictionary stores data in the form of:
# Key : Value
# Example:
# "Name" : "Ravi Kumar"

# Here we are creating one main dictionary called "amazon".
# Inside it, there are other dictionaries like Customer,
# Orders, Payment, and Seller.
# This is called a Nested Dictionary.

amazon = {

    # ---------------- CUSTOMER DETAILS ----------------
    "Customer": {

        # Customer basic information
        "Customer ID": 101,
        "Name": "Ravi Kumar",
        "Age": 25,
        "Prime Member": True,      # True means Prime member
        "Mobile": "9876543210",

        # Customer Address
        # Address itself is another dictionary
        "Address": {
            "Door No": "12A",
            "Street": "Anna Nagar",
            "City": "Chennai",
            "State": "Tamil Nadu",
            "Pincode": 600040
        }
    },

    # ---------------- ORDER DETAILS ----------------
    "Orders": {
        "Order ID": "OD1001",
        "Product": "Laptop",
        "Price": 55000,
        "Quantity": 1,
        "Status": "Delivered"
    },

    # ---------------- PAYMENT DETAILS ----------------
    "Payment": {
        "Method": "UPI",
        "Amount": 55000,
        "Paid": True
    },

    # ---------------- SELLER DETAILS ----------------
    "Seller": {
        "Seller ID": 500,
        "Name": "ABC Electronics",
        "Rating": 4.8
    }
}

# ==========================================================
# PRINT COMPLETE DICTIONARY
# ==========================================================

# Prints the entire dictionary at once.
print("=========== AMAZON DATA ===========")
print(amazon)

# ==========================================================
# ACCESS SPECIFIC VALUES
# ==========================================================

# To access nested dictionary values,
# keep using square brackets [].

# Main Dictionary -> Customer -> Name
print("\nCustomer Name :", amazon["Customer"]["Name"])

# Main Dictionary -> Customer -> Address -> City
print("Customer City :", amazon["Customer"]["Address"]["City"])

# Main Dictionary -> Orders -> Product
print("Product :", amazon["Orders"]["Product"])

# Main Dictionary -> Payment -> Method
print("Payment Method :", amazon["Payment"]["Method"])

# Main Dictionary -> Seller -> Name
print("Seller Name :", amazon["Seller"]["Name"])

# ==========================================================
# UPDATE EXISTING VALUES
# ==========================================================

# Change customer's age from 25 to 26. #changing
amazon["Customer"]["Age"] = 26  #straight away assign
amazon["Customer"]["Mobile"] = 9876543210 #straight away assign

# Change order status.
amazon["Orders"]["Status"] = "Returned"

print("\nAfter Update")
print(amazon)

# ==========================================================
# ADD NEW KEY AND VALUE
# ==========================================================

# Add Email because it does not exist.
amazon["Customer"]["Email"] = "ravi@gmail.com"

print("\nAfter Adding Email")
print(amazon["Customer"])

# ==========================================================
# LOOP THROUGH CUSTOMER DETAILS
# ==========================================================

# .items() gives both key and value.
# Example:
# Name : Ravi Kumar
# Age : 26

print("\nCustomer Details")

for key, value in amazon["Customer"].items():
    print(key, ":", value)   #giving : in order to separate key and value

# ==========================================================
# LOOP THROUGH ADDRESS
# ==========================================================

# Loop only inside Address dictionary.

print("\nCustomer Address")

for key, value in amazon["Customer"]["Address"].items():
    print(key, ":", value)

# ==========================================================
# CHECK WHETHER A KEY EXISTS
# ==========================================================

# Checks if Email key is available.

if "Email" in amazon["Customer"]:
    print("\nEmail Available")

# ==========================================================
# POP METHOD
# ==========================================================

# pop() removes a key and returns its value.

removed = amazon["Payment"].pop("Paid")

print("\nRemoved :", removed)

removed = amazon["Payment"].pop("Method")

print("\nRemoved :", removed)

# ==========================================================
# SETDEFAULT METHOD
# ==========================================================

# setdefault() adds a key only if it is missing.
# If Country already exists, nothing changes.

amazon["Seller"].setdefault("Country", "India")

print("\nSeller Details")
print(amazon["Seller"])

amazon["Seller"].setdefault("Seller1.abc")

print("\nSeller Details")
print(amazon["Seller"])

amazon["Seller"].setdefault("Country", "India")

print("\nSeller Details")
print(amazon["Seller"])


# ==========================================================
# COPY METHOD
# ==========================================================

# copy() creates another dictionary with the same data.
# Original dictionary remains unchanged.

amazon_copy = amazon.copy()

print("\nCopied Dictionary")
print(amazon_copy)

# ==========================================================
# FROMKEYS METHOD
# ==========================================================

# Creates a new dictionary.
# Every key gets the same default value.

warehouse = dict.fromkeys(
    ["Chennai", "Bangalore", "Hyderabad"],
    "Available"
)

print("\nWarehouse")
print(warehouse)

warehouse = dict.fromkeys(
    ["Chennai", "Bangalore", "Hyderabad","Up"],
    "Available"
)

print("\nWarehouse")
print(warehouse)

# ==========================================================
# DICTIONARY COMPREHENSION
# ==========================================================

# Automatically creates a dictionary using a loop.
# Every product gets 10 as discount.

discount = {
    product: 10
    for product in ["Laptop", "Mobile", "Watch"]
}

print("\nDiscount")
print(discount)

# ==========================================================
# CLEAR METHOD
# ==========================================================

# Make a copy of the dictionary.
temp = amazon.copy()

# clear() removes all key-value pairs.
temp.clear()

print("\nAfter Clear")
print(temp)

# ==========================================================
# END OF PROGRAM
# ==========================================================

print("\n===== PROGRAM COMPLETED =====")