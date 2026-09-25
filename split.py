# string . split(seperater)# split always returns as list seperator should match after split seperator removed extra spaces ignorer when using plain split()
#a)
text="Real 100 Champions"
print(text.split(" "))


#b) by comma
student="Ram,Sita,Ravi"
print(student.split(","))

#c) by hyphen(-)
date="01-06-2026"
print(date.split("-"))

#by /
date="01/06/2026"

#e)
name,age="Ashok 25".split()
print(name)
print(age)

print(bool(0))
print(bool(1))
print(bool(-5))
print(bool("Hello"))
print(bool(""))


#Input # python is asking you to type what you want in "out put"
name= input("Enter name: ")
age= int(input("Enter age: "))
print(age+age)

# id gives unique no(address) to every variable started in a database
x=4
y=6
print(id(x))
print(id(y))


#coversion int to float
#int to float
a=10
print(type(a))
b=float(a)
print(type(a))
print(b)

#float to int
x=90.95
print(type(x))
y=int(x)
print(type(y))
print(y)

#str to int
a="1000"
print(type(a))
c=int(a)
print(type(c))
print(c)

#int to str
x=10432
print(type(x))
y=str(x)
print(type(y))
print(y)

#
x=10
print(int(x))