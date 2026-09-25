#list to tuple conversion
products=["Rice","oil","Soap","Rice",100]
prices=[50,120,30,50,100]

products_to_tuple = tuple(products)
prices_to_tuple = tuple(prices)
print("\n products_conv_tuple:",products_to_tuple)
print("\n prices_conv_tuple:",prices_to_tuple)

#I tried modify in normal way
products[1] ="Bag"
print("Alter Append:",products_to_tuple) #if we put products then it will show bag or else it will not show bcz it is in tuple

# I tried modifying using try and except method
try:
    products_to_tuple[1] = "Bag"         # if we  use try and except typeerror also it will not  show in the (list) bag bcz it is in tuple
except TypeError:                        # to handle unexcepted error so that program does not crash
    print("products tuple cannot be modified")

# list to tuple
products_to_list=list(products_to_tuple)
prices_to_list=list(prices_to_tuple)

print("\n modified product to list:",products_to_list)
   
try:
    qty=int(input("Enter quantity:"))
    price=50
    total=qty*price
    print("price per item:",price)
    print("Total bill:",total)

except:
    print("quantity must be a number")

try:
    numerator=int(input("Enter any number:"))
    denominator=int(input("Enter any number:"))
    result=numerator/denominator
    print(result)

except ZeroDivisionError:
    print("denominator cannot be zero")






