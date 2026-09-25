#Logical Operates #Concept of Using words # AND,OR,XOR,NOT #True\False
#Bitwise operates #Concept of using =,&,|,^,~,>>,<<

#Decimal To Binary
a=5
b=3
print(bin(a)) #ob101
print(bin(b)) #ob11

#Ignoring ob in output
print(format(a,'b')) #101
print(format(b,'b')) #11

#Binary To Decimal
a="101"
print(int(a,2)) #5
b="11"
print(int(b,2)) #3

#Now Do
X=5
Y=3
print("X&Y=",X&Y) #1
print("X|Y=",X|Y) #7
print("X^Y=",X^Y) #6
print("~X=",~X) #-6
print("X>>1=",X>>1) #2
print("X<<1=",X<<1) #10

salary = int(input("Input My salary"))
print("salary=",salary)
print("After Level 1 promotion(<<1):",salary<<1)
print("After Level 2 promotion(<<2);",salary<<2)
print("penalty|deducation(>>1):",salary>>1)