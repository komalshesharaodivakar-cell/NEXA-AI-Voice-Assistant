# ==========================
# CITIZEN DOCUMENTS - TUPLE CONCEPTS
# ==========================

# Nested Tuple (Two Citizens)

citizens = (
    (
        "Ravi Kumar",
        "Ravi Kumar",
        "Ravi Kumar",
        "1234-5678-9012",
        "ABCDE1234F",
        "M1234567",
        True
    ),
    (
        "Priya Devi",
        "Priya Devi",
        "9876-5432-1098",
        "PQRSX5678Y",
        "P9876543",
        True
    )
)

print("Citizens:", citizens)

# ==========================
# Nested Tuple Unpacking
# ==========================

ravi, priya = citizens

print("\nRavi Record:", ravi)
print("Priya Record:", priya)

# ==========================
# Ravi Tuple Unpacking
# ==========================

ravi_name1, ravi_name2, ravi_name3, ravi_aadhaar, ravi_pan, ravi_passport, ravi_active = ravi

print("\nRavi Details")
print("Name 1:", ravi_name1)
print("Name 2:", ravi_name2)
print("Name 3:", ravi_name3)
print("Aadhaar:", ravi_aadhaar)
print("PAN:", ravi_pan)
print("Passport:", ravi_passport)
print("Active:", ravi_active)

# ==========================
# Priya Tuple Unpacking
# ==========================

priya_name1, priya_name2, priya_aadhaar, priya_pan, priya_passport, priya_active = priya

print("\nPriya Details")
print("Name 1:", priya_name1)
print("Name 2:", priya_name2)
print("Aadhaar:", priya_aadhaar)
print("PAN:", priya_pan)
print("Passport:", priya_passport)
print("Active:", priya_active)

#Concatenation
Extra_does=("Voter id","Ration Card")
print("\n After Concatenation:")
print(ravi+Extra_does)

#Loop
for i in citizens:
    print(i)

#Enumerate
print("\n citizen position:")
for pos,citizen in enumerate(citizens,start=4):
    print(pos,citizen)

#membership
print("\n PAN  FCY15U:", "ABCDE1234F" in citizens[0])    #give true if pan is present in tuple
print("\n PAN FCY15U:","PQRSX5678Y" in citizens[1])      #give true if pan no. is correct

#count
print(ravi.count("Ravi Kumar"))        #
print(priya.count("Priya Devi"))

#length
print("\n Total citizens:",len(citizens))    #total

#length based count
ravi_documents=citizens[0].count("Ravi Kumar")
priya_documents=citizens[1].count("Priya Devi")

documents_counts=(ravi_documents,priya_documents)

print("\n Ravi document count:",ravi_documents)
print("\n Priya document count:",priya_documents)
print("Maximum documents:",max(documents_counts))
print("Minimum documents:",sum(documents_counts))
print("Total documents:",sum(documents_counts))
print("Sorted documents:",sorted(documents_counts))

#Index
print("\n First Citizen:",citizens[0])  #it will show all the details of ravi kumar
print("\n Last Citizen:",citizens[1])    #it will show all the details of priya devi

document_counts=(ravi_documents,priya_documents)


print("\n Ravi document Count:",ravi_documents)
print("\n priya document Count:",priya_documents)
print("\n Maximum document",max(document_counts))
print("\n Minimum document",min(document_counts))
print("\n Total document",sum(document_counts))
print("Sorted documents:",sorted(document_counts))

#count
print("\nravi count:",citizens[0].count("Ravi Kumar"))
print("\npriya count:",citizens[1].count("Priya Devi"))

document_counts=(ravi_documents,priya_documents)
print(document_counts)
document_counts=(3,2)
document_counts2=(3,2)
print("\n Equal:",document_counts==document_counts2)
print("\n Less than:",document_counts<document_counts2)
print("\n Greater than:",document_counts>document_counts2)

#Repeated
print("\n Repeat:")
print((" verified\n"*3))
print((" verified"*3))
print((" verified,"*3))
#Immute
'''ravi[0]="Arun"
print("\n Tuple Immutable")
print('ravi[0]="Arun"')'''

#Slicing
print("\n Ravi First 4 fields:",ravi[:4])
print("\n priya  fields reverse:",priya[::-1]) #same as below here semicolon is mandoratory

#Negative Index
print("\n Ravi Last Item:",ravi[-1])  #it will come in negative bcz it is starting from right to left means -1,-2,-3

#Normal Index
print("Ravi Name:",ravi[1])
print("Priya Aadhaar:",priya[2])
print("First Citizen:",citizens[0])
print("Second Citizen:",citizens[1])


