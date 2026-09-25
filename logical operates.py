#real life program for smart door security system
print("SMART DOOR SECURITY SYSTEM\n")
A=int(input("motion sensor(1=person, 0=no person):"))
B=int(input("face recognition(1=know face,0=unknown face):"))
print("in===SIMPLE Explanation====\n")

#AND Operator
print("AND(&)-both must be true")
print('meaning:"door opens only if person is there and face is known"')
print('case;)A,B')
print("result:",A&B)

#OR Operator
print("\n or (|)- Anyone can be true")
print('meaning:"door  just reacts if person there or known face detected"')
print("CASE:",(A,B))
print("Result:",A|B)

#XOR operator
print("|n Xor (^)- Only one must be true")
print('meaning:"Alert it only one condition true (suspecous)"')
print("CASE:",(A,B))
print("Result:",A^B)

#Not Operator (formula ~n=-(n+1)
print("|n NOT(~)-opposite value")
print('meaning:"change 0 to 1-change 1 to 0"')
print("CASE:",A,"NOT A:",~A)
print("CASE:",B,"NOT B:",~B)

print("\n=== final decision ===")

#Case 1 : A= and B =1(Both true)
if A==1 and B==1:
    print("Door open-person detected and face recognition")
