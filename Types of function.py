#Types of functions
#USES:
#Reducing the length of code
#To call function anytime
#To update straight away
# NO ARGUMENTS, NO RETURNS
def say_hello(): #shop person telling hello
    print("hello")

say_hello()


# Arguments with No Return
def greet(name): #Asking to make juice
    print("hello", name)
    greet("riya")

def greet(marks):
    print("your marks is",marks)
    greet("100")

#no Arguments only return    #given fruits return back as juice
def get_number():
    return 10        #return-return a results
x=get_number()
print(x)

def get_balance():
    return 100
x=get_balance()
print(x)

#Arguments, Return
def add(a,b):
    return a+b
result = add(10,20)
print(result)
def multiply(a,b,c):
    return a*b*c
result = multiply(10,20,30)
print(result)

# Nested Function
def outer():
    def inner():
        print("How are you")

    inner()

outer()

#LIST
#[ ]open box can be closed [] - using tuple() - we can't modify
#[]closed box can be open [ ] - using list[]  - we can modify

