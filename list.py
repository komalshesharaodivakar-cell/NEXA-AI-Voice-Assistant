#Mega Mart-list concepts
#list creation(ordered,duplicates,heterogeneous)
products=["Rice","oil","Soap","Rice",100]
prices=[50,120,30,50,100]
print("products:",products)
print("prices:",prices)

#+ve index
print("\n First product:",products[0])
print("\n First prices:",prices[4])
#-ve index
print("\n last product:",products[-1])
print("\n last prices:",prices[-1])
#string
print("First 3 products:",products[0:3])
#length
print("Total products:",len(products))
#membership
print("Rs oil available?","oil" in products)
print("Rs Soap available?", "Soap" not in products)

#copy
backup_products=products.copy()
print("copied list:",backup_products)
#append
products.append("Milk")            #we can only put one item
print("Alter Append:",products)
#extend
products.extend(["Bread","Sugar"])      #we can add multiple items in the list[]
print("Alter extend:",products)
#Insert
products.insert(1,"Tea")            # in middle
print("Alter insert:",products)
#Count
print("Rice Count:",products.count("Rice"))
#Index
print("oil index",products.index("oil"))             #it will see as which is in the position like 1,2,3
print("Soap index",products.index("Soap"))
#mutable(replace)
products[0]="Basmati Rice"
print("After Replace:",products)           #it will replace the item from the list like rice to basmati rice
#Remove
products.remove("Soap")
print("After Remove:",products)             #it will remove the item
#POP
removed_item=products.pop()           #if we have large set of data and i have to remove last and it will automatically remove the last item
print("popped_item:",removed_item)
print("after pop:",products)
#Reverse
products.reverse()
print("After reverse:",products)         # it will give in reverse like from last to first
#Sort
numbers_price=[50,10,80,20,40]
numbers_price.sort()
print("Sorted numbers:",numbers_price)        #it will give o/p in correct manner like 10,20,40,50,80 low to high
#sort()#high to low
numbers_price=[50,10,80,20,40]
numbers_price.sort()
numbers_price.sort(reverse= True)
print("Sorted numbers:",numbers_price)

#lambda-Add 18%GST
gst=lambda i:i+(i*18/100)           #online function it will give single item from the list
print("GST on 1250=",gst(1250))
print("GST on 3333=",gst(3333))

#Map-Apply to all GST products
gst_prices=list(map(lambda x:x+(x*18/100),prices))    #it will take all item from the list
print("gst for all items in list:",gst_prices)

#Filter-products above 1000 after GST
high_prices=list(filter(lambda x:x>100,gst_prices))           #it will get above greater 100
print("prices above 100:",high_prices)

#Reduce_calculate total bill
from functools import reduce
total_bill=reduce(lambda x,y:x+y,gst_prices)        #it will give the direct o/p like we will see amazon cart they will the direct calculations
print("total_bill after gst:",total_bill)

#clear
tempfile_product=["Rice","oil","Soap","Rice","Sugar"]
tempfile_product.clear()
print("\n after clear:",tempfile_product)

#Nested list
        # 0,0  0      1     2     0         1    2      0       1     2     0       1      2      0       1    2      0       1      2
Customers=[[["Ravi","Rice",50],["karthik","oil",120],["Meena","Soap",30],["Divya","Sugar",45],["Suresh","Tea",20],["Priya","coffee",40]]]
print(Customers[0][0])
print(Customers[0][1][2])
print(Customers[0][2][1])
print(Customers[0][3][0])
print(Customers[0][4][1])
print(Customers[0][5][0])