# ============================================
# NUMPY + PANDAS + MATPLOTLIB PROJECT
# Employee Dataset Analysis
# Part 1
# ============================================
import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------
# Read Excel File
# --------------------------------------------

df = pd.read_excel("C:\\Users\\komal\\Downloads\\Employee_Dataset.xlsx")

print("="*60)
print("EMPLOYEE DATASET")
print("="*60)

print(df) #  it will show the o/p but the gap will fill as nan

# --------------------------------------------
# Shape
# --------------------------------------------

print("\nShape")           #in this rows from 0 to 9 and columns are 6
print(df.shape)

# --------------------------------------------
# Columns
# --------------------------------------------

print("\nColumns")
print(df.columns)

# --------------------------------------------
# Data Types
# --------------------------------------------

print("\nData Types")
print(df.dtypes)

# --------------------------------------------
# Information
# --------------------------------------------

print("\nInfo")
print(df.info())

# --------------------------------------------
# Statistics
# --------------------------------------------

print("\nStatistics")
print(df.describe())

# --------------------------------------------
# First Rows
# --------------------------------------------

print("\nFirst Five Rows")
print(df.head())

# --------------------------------------------
# Last Rows
# --------------------------------------------

print("\nLast Five Rows")
print(df.tail())

# --------------------------------------------
# Random Rows
# --------------------------------------------

print("\nRandom Three Rows")
print(df.sample(3))

# --------------------------------------------
# Column Selection
# --------------------------------------------

print("\nEmployee Names")
print(df["Name"])

print("\nSalary Column")
print(df["Salary"])

print("\nMultiple Columns")
print(df[["Name","Department","Salary"]])

# --------------------------------------------
# Row Selection using loc
# --------------------------------------------

print("\nFirst Row")
print(df.loc[0])   #location

print("\nRows 2 to 5")
print(df.loc[2:5])

# --------------------------------------------
# Row Selection using iloc
# --------------------------------------------

print("\nUsing iloc")
print(df.iloc[0:4])

# --------------------------------------------
# Missing Values
# --------------------------------------------

print("\nMissing Values")
print(df.isnull())

print("\nMissing Value Count")
print(df.isnull().sum())

# --------------------------------------------
# Fill Missing Values
# --------------------------------------------

average_salary = df["Salary"].mean()

df["Salary"] = df["Salary"].fillna(average_salary)

df["Name"] = df["Name"].fillna("Unknown")

print("\nAfter Filling Missing Values")
print(df)

# --------------------------------------------
# Duplicate Rows
# --------------------------------------------

print("\nDuplicate Rows")

print(df.duplicated())

print("\nDuplicate Count")

print(df.duplicated().sum())

# --------------------------------------------
# Remove Duplicate
# --------------------------------------------

df = df.drop_duplicates()

print("\nAfter Removing Duplicates")
print(df)

# --------------------------------------------
# Sorting
# --------------------------------------------

print("\nSort Salary Ascending")

print(df.sort_values("Salary"))

print("\nSort Salary Descending")

print(df.sort_values("Salary",ascending=False))

# --------------------------------------------
# Filtering
# --------------------------------------------

print("\nSalary Greater than 40000")

print(df[df["Salary"]>40000])

print("\nIT Department")

print(df[df["Department"]=="IT"])

print("\nHR Department")

print(df[df["Department"]=="HR"])

print("\nExperience Greater than 4")

print(df[df["Experience"]>4])

print("\nIT Department with Salary > 40000")

print(df[(df["Department"]=="IT") &
         (df["Salary"]>40000)])

# --------------------------------------------
# isin()
# --------------------------------------------

print("\nIT and HR Employees")

print(df[df["Department"].isin(["IT","HR"])])

# --------------------------------------------
# Between
# --------------------------------------------

print("\nSalary Between 35000 and 50000")

print(df[df["Salary"].between(35000,50000)])

# --------------------------------------------
# New Columns
# --------------------------------------------

df["Bonus"] = df["Salary"]*0.10

df["Total Salary"] = df["Salary"]+df["Bonus"]

print("\nAfter Adding Bonus")

print(df)

# --------------------------------------------
# Rename Columns
# --------------------------------------------

df = df.rename(columns={
    "Salary":"Monthly Salary"
})

print("\nRenamed Columns")

print(df.columns)

# --------------------------------------------
# Unique Values
# --------------------------------------------

print("\nDepartments")

print(df["Department"].unique())

print("\nNumber of Departments")

print(df["Department"].nunique())

# --------------------------------------------
# Value Counts
# --------------------------------------------

print("\nDepartment Count")

print(df["Department"].value_counts())
# ===========================================
# PART 2 : GROUPBY + NUMPY
# ===========================================

# -------------------------------------------
# GroupBy Operations
# -------------------------------------------

print("\n" + "="*60)
print("GROUPBY OPERATIONS")
print("="*60)

print("\nAverage Salary by Department")
print(df.groupby("Department")["Monthly Salary"].mean())

print("\nMaximum Salary by Department")
print(df.groupby("Department")["Monthly Salary"].max())

print("\nMinimum Salary by Department")
print(df.groupby("Department")["Monthly Salary"].min())

print("\nTotal Salary by Department")
print(df.groupby("Department")["Monthly Salary"].sum())

print("\nEmployee Count by Department")
print(df.groupby("Department")["Emp_ID"].count())

# -------------------------------------------
# Multiple Aggregations
# -------------------------------------------

print("\nMultiple Aggregation")

result = df.groupby("Department").agg({
    "Monthly Salary":["mean","max","min","sum"],
    "Experience":["mean","max"],
    "Attendance":["mean","max"]
})

print(result)

# -------------------------------------------
# Sorting GroupBy Result
# -------------------------------------------

print("\nDepartment Average Salary Descending")

print(
    df.groupby("Department")["Monthly Salary"]
      .mean()
      .sort_values(ascending=False)
)

# -------------------------------------------
# NumPy Section
# -------------------------------------------

print("\n" + "="*60)
print("NUMPY")
print("="*60)

salary = df["Monthly Salary"].to_numpy()

print("\nSalary Array")
print(salary)

print(type(salary))

# -------------------------------------------
# Array Information
# -------------------------------------------

print("\nDimension")
print(salary.ndim)

print("\nShape")
print(salary.shape)

print("\nSize")
print(salary.size)

print("\nData Type")
print(salary.dtype)

# -------------------------------------------
# Mathematical Functions
# -------------------------------------------

print("\nMean")
print(np.mean(salary))

print("\nMedian")
print(np.median(salary))

print("\nMaximum")
print(np.max(salary))

print("\nMinimum")
print(np.min(salary))

print("\nSum")
print(np.sum(salary))

print("\nStandard Deviation")
print(np.std(salary))

print("\nVariance")
print(np.var(salary))

# -------------------------------------------
# Indexing
# -------------------------------------------

print("\nFirst Salary")
print(salary[0])

print("\nLast Salary")
print(salary[-1])

# -------------------------------------------
# Slicing
# -------------------------------------------

print("\nFirst Four Salaries")
print(salary[:4])

print("\nMiddle Salaries")
print(salary[2:6])

# -------------------------------------------
# Arithmetic Operations
# -------------------------------------------

print("\nSalary + 5000")
print(salary + 5000)

print("\nSalary * 2")
print(salary * 2)

print("\nSalary - 1000")
print(salary - 1000)

# -------------------------------------------
# Comparison
# -------------------------------------------

print("\nSalary Greater Than 40000")
print(salary > 40000)

# -------------------------------------------
# NumPy Arrays
# -------------------------------------------

arr = np.array([10,20,30,40,50])

print("\nSimple Array")
print(arr)

# -------------------------------------------
# Zeros
# -------------------------------------------

print("\nZeros Matrix")

print(np.zeros((3,3)))

# -------------------------------------------
# Ones
# -------------------------------------------

print("\nOnes Matrix")

print(np.ones((2,4)))

# -------------------------------------------
# Identity Matrix
# -------------------------------------------

print("\nIdentity Matrix")

print(np.eye(4))

# -------------------------------------------
# Arange
# -------------------------------------------

print("\nArange")

print(np.arange(1,21))

print(np.arange(10,101,10))

# -------------------------------------------
# Linspace
# -------------------------------------------

print("\nLinspace")

print(np.linspace(0,100,5))

# -------------------------------------------
# Random Numbers
# -------------------------------------------

print("\nRandom Integers")

print(np.random.randint(1,100,10))

print("\nRandom Float Values")

print(np.random.rand(5))

# -------------------------------------------
# Reshape
# -------------------------------------------

print("\nReshape")

numbers = np.arange(1,13)

print(numbers)

matrix = numbers.reshape(3,4)

print(matrix)

# -------------------------------------------
# Flatten
# -------------------------------------------

print("\nFlatten")

print(matrix.flatten())

# -------------------------------------------
# Transpose
# -------------------------------------------

print("\nTranspose")

print(matrix.T)

# -------------------------------------------
# Maximum and Minimum Position
# -------------------------------------------

print("\nIndex of Maximum Salary")

print(np.argmax(salary))

print("\nIndex of Minimum Salary")

print(np.argmin(salary))

# -------------------------------------------
# Square Root
# -------------------------------------------

print("\nSquare Root")

print(np.sqrt(salary))

# -------------------------------------------
# Power
# -------------------------------------------

print("\nSquare")

print(np.power(arr,2))

# -------------------------------------------
# Trigonometry
# -------------------------------------------

angles = np.array([0,30,45,60,90])

print("\nSin Values")

print(np.sin(np.radians(angles)))

# -------------------------------------------
# Save Updated Excel
# -------------------------------------------

df.to_excel("Updated_Employee.xlsx",index=False)

print("\nUpdated Excel Saved Successfully")
# ============================================
# PART 3 : MATPLOTLIB
# ============================================

print("\n" + "="*60)
print("MATPLOTLIB VISUALIZATION")
print("="*60)

# --------------------------------------------
# Line Chart
# --------------------------------------------

plt.figure(figsize=(6,4))

plt.plot(
    df["Emp_ID"],
    df["Monthly Salary"],
    marker="o",
    linewidth=2
)

plt.title("Employee Salary")
plt.xlabel("Employee ID")
plt.ylabel("Monthly Salary")
plt.grid(True)

plt.show()

# --------------------------------------------
# Bar Chart
# --------------------------------------------

dept_salary = df.groupby("Department")["Monthly Salary"].mean()

plt.figure(figsize=(6,4))

plt.bar(
    dept_salary.index,
    dept_salary.values
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

# --------------------------------------------
# Horizontal Bar Chart
# --------------------------------------------

plt.figure(figsize=(7,5))

plt.barh(
    df["Name"],
    df["Monthly Salary"]
)

plt.title("Employee Salary")
plt.xlabel("Salary")
plt.ylabel("Employee")

plt.show()

# --------------------------------------------
# Pie Chart
# --------------------------------------------

dept_count = df["Department"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    dept_count.values,
    labels=dept_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Department Distribution")

plt.show()

# --------------------------------------------
# Histogram
# --------------------------------------------

plt.figure(figsize=(6,4))

plt.hist(
    df["Monthly Salary"],
    bins=5
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

# --------------------------------------------
# Scatter Plot
# --------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    df["Experience"],
    df["Monthly Salary"]
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.grid(True)

plt.show()

# --------------------------------------------
# Box Plot
# --------------------------------------------

plt.figure(figsize=(5,5))

plt.boxplot(
    df["Monthly Salary"]
)

plt.title("Salary Box Plot")
plt.ylabel("Salary")

plt.show()

# --------------------------------------------
# Attendance Line Chart
# --------------------------------------------

plt.figure(figsize=(6,4))

plt.plot(
    df["Name"],
    df["Attendance"],
    marker="*"
)

plt.title("Attendance")
plt.xlabel("Employee")
plt.ylabel("Attendance")

plt.grid(True)

plt.show()

# --------------------------------------------
# Experience Bar Chart
# --------------------------------------------

plt.figure(figsize=(6,4))

plt.bar(
    df["Name"],
    df["Experience"]
)

plt.title("Experience of Employees")
plt.xlabel("Employee")
plt.ylabel("Years")

plt.show()

# --------------------------------------------
# Salary vs Attendance
# --------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    df["Attendance"],
    df["Monthly Salary"]
)

plt.title("Attendance vs Salary")
plt.xlabel("Attendance")
plt.ylabel("Salary")

plt.grid(True)

plt.show()

# --------------------------------------------
# Save Final Excel
# --------------------------------------------

df.to_excel(
    "Employee_Analysis_Output.xlsx",
    index=False
)

print("\nEmployee Analysis Completed Successfully.")
print("Updated Excel File Saved.")