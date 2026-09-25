# ==========================================
# FLIPKART WAREHOUSE MANAGEMENT - SETS
# ==========================================
# A Set stores only UNIQUE products.
# Duplicate products are automatically removed.
# ==========================================

# ==========================================
# WAREHOUSE 1
# Duplicate products are automatically removed.
# ==========================================

w1 = {
    "Mobile",
    "Laptop",
    "Watch",
    "Earbuds",
    "Power Bank",
    "Laptop",      # Duplicate
    "Mobile",      # Duplicate
    "Watch"        # Duplicate
}

# ==========================================
# WAREHOUSE 2
# Duplicate products are automatically removed.
# ==========================================

w2 = {
    "Laptop",
    "Watch",
    "Camera",
    "Printer",
    "Power Bank",
    "Camera",      # Duplicate
    "Printer"      # Duplicate
}

print("Warehouse 1 Products:")
print(w1)

print("\nWarehouse 2 Products:")
print(w2)

# ==========================================
# len()
# Counts the total number of
# UNIQUE products available
# in Warehouse 1.
# ==========================================

print("\nTotal Products in Warehouse 1:")
print(len(w1))

# ==========================================
# add()
# Adds ONE new product.
# If the product already exists,
# nothing changes.
# ==========================================

w1.add("Keyboard")
w1.add("Keyboard")

print("\nAfter add():")
print(w1)

# ==========================================
# update()
# Adds MANY products at once.
# Duplicate products are ignored.
# ==========================================

w2.update(["Mouse", "Monitor", "Mouse", "Laptop"])

print("\nAfter update():")
print(w2)

# ==========================================
# remove()
# Removes the product.
# If the product does not exist,
# Python gives an error.
# ==========================================

w1.remove("Keyboard")

print("\nAfter remove():")
print(w1)

# ==========================================
# discard()
# Removes the product if it exists.
# If the product is missing,
# nothing happens.
# No error is given.
# ==========================================

w1.discard("Tablet")

print("\nAfter discard():")
print(w1)

# ==========================================
# Membership (in)
# Checks whether a product
# is available in Warehouse 1.
# Returns True or False.
# ==========================================

print("\nIs Laptop Available?")
print("Laptop" in w1)

# ==========================================
# copy()
# Creates a backup copy.
# Changes made to the backup
# do not affect the original.
# ==========================================

backup = w1.copy()

print("\nBackup Warehouse:")
print(backup)

# ==========================================
# union()
# Combines products from BOTH
# warehouses.
# Duplicate products appear
# only once.
# ==========================================

print("\nAll Products Available:")
print(w1.union(w2))

# ==========================================
# intersection()
# Shows ONLY the common
# products available in
# BOTH warehouses.
# ==========================================

print("\nProducts Available in Both Warehouses:")
print(w1.intersection(w2))

# ==========================================
# difference()
# Shows ONLY the products
# available in Warehouse 1.
# Common products are removed.
# ==========================================

print("\nProducts Only in Warehouse 1:")
print(w1.difference(w2))

# ==========================================
# difference()
# Shows ONLY the products
# available in Warehouse 2.
# Common products are removed.
# ==========================================

print("\nProducts Only in Warehouse 2:")
print(w2.difference(w1))

# ==========================================
# symmetric_difference()
# Removes common products.
# Keeps ONLY unique products
# from BOTH warehouses.
# ==========================================

print("\nUnique Products from Both Warehouses:")
print(w1.symmetric_difference(w2))

# ==========================================
# pop()
# Removes and returns ANY ONE product.
# Sets have NO fixed order,
# so Python chooses any product.
# ==========================================

temp = w1.copy()

print("\nPopped Product:")
print(temp.pop())

print("\nRemaining Products:")
print(temp)

# ==========================================
# issubset()
# Checks whether EVERY product in
# Warehouse 1 is also available
# in Warehouse 2.
# Returns True or False.
# ==========================================

print("\nIs Warehouse 1 a Subset of Warehouse 2?")
print(w1.issubset(w2))

# ==========================================
# issubset()
# Checks whether EVERY product in
# Warehouse 2 is also available
# in Warehouse 1.
# Returns True or False.
# ==========================================

print("\nIs Warehouse 2 a Subset of Warehouse 1?")
print(w2.issubset(w1))

# ==========================================
# issuperset()
# Checks whether Warehouse 1
# contains EVERY product
# from Warehouse 2.
# Returns True or False.
# ==========================================

print("\nIs Warehouse 1 a Superset of Warehouse 2?")
print(w1.issuperset(w2))

# ==========================================
# issuperset()
# Checks whether Warehouse 2
# contains EVERY product
# from Warehouse 1.
# Returns True or False.
# ==========================================

print("\nIs Warehouse 2 a Superset of Warehouse 1?")
print(w2.issuperset(w1))

# ==========================================
# isdisjoint()
# Checks whether both sets have
# NO common products.
# Returns True if there are
# no common products.
# ==========================================

food_items = {                   #check whether there is common product between them
    "Rice",
    "Oil"
}

print("\nDisjoint Check:")
print(w1.isdisjoint(food_items))
print("\nDisjoint Check:")
print(w2.isdisjoint(food_items))

# ==========================================
# difference_update()
# Make a copy of Warehouse 1.
# Permanently removes products
# that are also available
# in Warehouse 2.
# ==========================================

w1_copy = w1.copy()

w1_copy.difference_update(w2)

print("\nAfter difference_update():")
print(w1_copy)

# ==========================================
# intersection_update()
# Make a copy of Warehouse 1.
# Permanently keeps ONLY the
# common products available
# in both warehouses.
# ==========================================

w1_common = w1.copy()

w1_common.intersection_update(w2)

print("\nAfter intersection_update():")
print(w1_common)

# ==========================================
# symmetric_difference_update()
# Make a copy of Warehouse 1.
# Permanently removes common
# products and keeps ONLY
# unique products.
# ==========================================

w1_unique = w1.copy()

w1_unique.symmetric_difference_update(w2)

print("\nAfter symmetric_difference_update():")
print(w1_unique)

# ==========================================
# clear()
# Removes EVERY product
# from the set.
# The set becomes empty.
# ==========================================

temp_set = {
    "A",
    "B",
    "C",
    "A"      # Duplicate
}

temp_set.clear()

print("\nAfter clear():")
print(temp_set)