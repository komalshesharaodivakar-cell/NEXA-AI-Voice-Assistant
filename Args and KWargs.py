#args allows a function to accept any number of positional arguments. The arguments are stored/takes  as a tuple.
#kwargs allows a function to accept any number of keyword arguments (key=value). The arguments are stored as a dictionary.

# *args Example

def products(*items):
    print("Products:", items) #gives laptop as output accompanied by a comma as default-single element

products("Laptop")
products("Laptop", "Mobile", "Watch","Bag")#can give more products as it takes n number of positional value
products("Late","ontime")


 # **kwargs Example

def customer(**details):
    print(details)

customer(name="Ravi", city="Chennai", age=25,DOB="06-08-2003")


#combined together -*args and *kwargs


def shopping(*products, **customer):
    print("Products:", products)
    print("Customer:", customer)

shopping(
   "Laptop",
    "Mouse",
    "Keyboard",
    name="Ravi",
    city="Chennai")


shopping(
    "rice",
    "oil",
    "soap",
    komal=25
)



'''

#here while we need to add the products first, then only customer(gets error)

shopping(
    komal=25,
    "rice",
    "oil",
    "soap"
)


'''



'''
#Here we get error becaz **kwargs needs to be follwed by *args

def shopping(**customer,*products):
    print("Products:", products)
    print("Customer:", customer)

shopping(
    "rice",
    "oil",
    "soap",
    komal=25
)
'''
