#Airport Management system
'''print("Airport Bag Check\n")
Bags=int(input("number of bags"))
if Bags>2:
  print("Extra Baggage Detected")
print("Checked Completed")

#if-else
print("Ticket Verification")
Ticket=input("Ticket Status(valid/invalid):")
if Ticket == "valid":
   print("valid Ticket")
else:
    print("invalid Ticket")

#if elif else
weight=float(input("Enter luggage weight:"))
if weight>60:
    print("Heavy luggage")
elif weight>40:
    print("Medium luggage")
elif weight>30:
    print("small luggage")
elif weight>20:
    print("normal luggage")
else:
    print("light luggage")


#Nested if
print("Document Verification\n")
ticket = input("ticket status (valid/invalid):")
visa = input("visa status(yes/no):")
if ticket == "valid":
    print("ticket verified")
if visa == "yes":
    print("visa approved")

#Nested if else
Age = int(input("Age:"))
danger = input("Danger item found?(Yes/no):")
if Age >= 18:
    print("Adult passenger")
    if danger == "no":
        print("Security clearance passed")
    else:
        print("Danger item detected")
else:
    print("Minor passenger")'''

# Nested if
Ticket = input("Ticket status (Valid/Invalid): ")
Visa = input("Visa status (Yes/No): ")
Danger = input("Danger item found (Yes/No): ")

if Ticket == "Valid":
    print("Ticket validated")

    if Visa == "Yes":
        print("Visa available")

        if Danger == "Yes":
            print("Dangerous item detected")
        elif Danger == "No":
            print("No dangerous item detected")
            print("Boarding Allowed")

    else:
        print("Visa missing")

else:
    print("Invalid Ticket")

#Nested if+elif+else
'''Country=input("Country:")
Age=int(input("Age:"))
if Country == "USA":
    if Age >= 60:
        print("Senior citizen assistance")

    elif Age >= 18:
         print("Regular passenger")
    else:
         print("child passenger")
else:
    print("International passenger")'''
