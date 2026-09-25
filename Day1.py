print("welcome to python code")

#import  keyword #retrieve import variables
#print(keyword.kwlist)

print("Hello World")

Name="Gayathri" # Variable names cannot start with a number
Age1=25
Student_name=150

# Hyphen (-) is treated as a subtraction operator
x=Name+str(Age1)
#class=10 #'class' is a reserved keyword and cannot be used as a variable name
print(Name)
print(Age1)
print(x)

#split command normal()
text="python is easy"
result=text.split() #default cone as splitted as , # split() uses whitespace as the default separator
print(result)


data="Apple,Banana,JackFruit"
result=data.split(",")
print(result)

data="2026-05-27"
result= data.split("-")
print(result)

email="rjgayathri25@gmail.com"
result=email.split("@")
print(result)

print(email.split("@"))

word="tiger"
print(list(word))

#input
name=input("Enter employee name:") # Takes input from the user
print("Enter Employee name:") # Only displays the message


a,b=int(input("Enter 2 numbers") )# Accepts two characters and assigns them to a and b
print(a)
print(b)



#Salary and age calculations
Name=input("Enter Employee Name:")
Age1="25"
Salary=input("enter basic salary:")
status=input("Permanent:True/False")
#print(Age1)
print(type(Age1))
Age1=int(Age1)
print(Age1)
print(type(Age1))
Salary=float(Salary)
print(type(Salary))
#status_strip().lower()

#Expression
Next_year_age=Age1+1
Retirement_year=60-Age1
Bonus=Salary*0.10
TotalSalary=Salary+Bonus
print(Next_year_age)
print(Bonus)
print(Retirement_year)
print(TotalSalary)
