#for loop
for i in range(2,10):     # it will print from 2 to 9
    print(i)

for i in range (5):        #it will print 5 times welcome to python
    print("welcome to python")

#while loop
count=0
while count<=5:     #0=0+1, 1+1=2, 2+1=3, 3+1=4, 4+1=5
    print(count)    #if we use <in the ans we count from 0 to 4 and if we use <= then it will count from 0 to 5 like above example
    count=count+1
num=1
while num<=5:      #1+1=2, 2+1=3, 3+1=4, 4+1=5 
    print(num)
    num=num+1

#for loop with if
word=input("Enter a word:")
count=0
for character in word:
    if character in "aeiouAEIOU":    #like if we take elephant in this how much vowels r there it will by vowels=1, vowels=2
        count=count+1
        print("vowels=",count)


# Nested for loop[for table generation]
for i in range(2,11):     # in this the table it will show from 2 to 10
    print("\n table of",i)
    for j in range(1,11):
        print(i,"X",j,"=",i*j)     # in this it will take by multiplying i*j like 2*1=2

# Nested while loop
i=2
while i<=10:
    print("\n table of",i)   #2*1=2, 3*2=6, 4*3=12
    j=1
    while j<=10:
        print(i,"X",j,"=",i*j)   #2*1=2, 2*2=4, 2*3=6
        j=j+1                    #2=1+1
        i=i+1                    #3=2+1

# example we not use (i in range) condition here
print("\n table of 2")
for j in range(1,11):
    print(2,"X",j,"=",2*j)   #2*1=2, 2*2=4 till 2*10=20 it will come . But till will not count 11
