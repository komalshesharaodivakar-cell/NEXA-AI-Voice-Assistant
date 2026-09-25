#0 1 2 3 4 5 6 7 8 9 10 11 12 13
#RULES FOR THE INDEX
#E V E R Y W H E R E     G  O  D
#1.Includes start index
#Accessing Elements by Index
#2.left to right
X="EVERYWHERE GOD"
#3.end-before index
print(X[1])
#4.jump - 2,3,4,5 - 2 4 6 8 10- 3 6 9 11 13
print(X[13])
print(X[12])
print(X[7])
print(X[9])
print(X[5])

#Slicing #left to right - includes start index
X="EVERYWHERE GOD"
print(X[0:5])# 0 is mandate upto 4 it takes for 5
print(X[5:10])
print(X[11:14]) #else [11: ]
print(X[6:10])
print(X[0:4])
print(X[1:5])

X="EVERYWHERE GOD"
print(X[0:14:2])
print(X[0:14:3])
print(X[0:14:4])
print(X[:])
print(X[::])
print(X[::1])
print(X[0:14:11])
print(X[0:12:11])
print(X[-1] + X[-10]) #negative
print(X[13] + X[4])
print(X[::-1])
print(X[-1])
print(X[-4])
print(X[-5])
print(X[-10])
print(X[-13])
print(X[-14])

print(X[-4:-3]) #wrong                                   #rule always starts with -1
print(X[-3:-4])                                           #ends exactly
print(X[-13:-1])                                          #right to left
print(X[-9:-2])                                           #start should be greater than end
print(X[-14:-8])
print(X[-8:-5])
print(X[-14:-8:-1])
print(X[-8:-14:-1]) #explaining of the 51 line how it can be work.