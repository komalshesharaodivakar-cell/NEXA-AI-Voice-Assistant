print("EMPLOYEE HR & SALARY MANAGEMENT SYSTEM\n")

salary = float(input("Enter Basic Salary: "))
attendance = int(input("Attendance (0-30): "))
performance = int(input("Performance (0-10): "))

# =====================================
# ARITHMETIC OPERATORS
# =====================================

monthly_salary = salary / 12

print("\n===== ARITHMETIC =====")
print("Bonus Salary   :", salary + salary * 0.10)
print("Tax Salary     :", salary - salary * 0.05)
print("Reward Salary  :", salary * 2)
print("Monthly Salary :", monthly_salary)
print("Floor Salary   :", salary // 12)
print("Remainder      :", salary % 12)
print("Power Example  :", 2 ** 3)

# =====================================
# ASSIGNMENT OPERATORS
# =====================================

print("\n===== ASSIGNMENT =====")

salary += 1000
print("After += :", salary)

salary -= 500
print("After -= :", salary)

salary *= 2
print("After *= :", salary)

salary /= 2
print("After /= :", salary)

salary //= 3
print("After //= :", salary)

salary %= 1000
print("After %= :", salary)

salary **= 2
print("After **= :", salary)

# =====================================
# RELATIONAL OPERATORS
# =====================================

print("\n===== RELATIONAL =====")

print("salary > 20000  :", salary > 20000)
print("salary < 50000  :", salary < 50000)
print("salary >= 10000 :", salary >= 10000)
print("salary <= 80000 :", salary <= 80000)
print("salary == 0     :", salary == 0)
print("salary != 1000  :", salary != 1000)

# =====================================
# LOGICAL OPERATORS
# =====================================

eligible_bonus = (salary > 20000) and (monthly_salary > 1000)
loan_approved = (salary > 30000) or (monthly_salary > 2000)
risk_flag = not (salary > 100000)

print("\n===== LOGICAL =====")
print("Bonus (AND) :", eligible_bonus)
print("Loan (OR)   :", loan_approved)
print("Risk (NOT)  :", risk_flag)

# =====================================
# BITWISE OPERATORS
# =====================================

good_attendance = attendance >= 25
good_performance = performance >= 7

print("\n===== BITWISE HR =====")
print("Bonus (&)     :", good_attendance & good_performance)
print("Promotion (|) :", good_attendance | good_performance)
print("Warning (^)   :", good_attendance ^ good_performance)

# =====================================
# FINAL REPORT
# =====================================

print("\n===== FINAL REPORT =====")
print("Final Salary   :", salary)
print("Monthly Salary :", monthly_salary)
print("Attendance     :", attendance)
print("Performance    :", performance)
print("renmainder:",salary%12)