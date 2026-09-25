# ==========================================
# EMPLOYEE MANAGEMENT SYSTEM
# Covers:
# Class, Object, Method
# Encapsulation (Getter & Setter)
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Method Overriding
# ==========================================


# ==========================================
# PARENT CLASS
# ==========================================
class Employee:

    # Constructor
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name

        # '.__salary' - means to lock the salary nobody cant access without  getter and setter
        self.__salary = salary      # Private Attribute   #money inside locker

    # Getter
    def get_salary(self):
        return self.__salary        #just to see data      #key to see money

    # Setter
    def set_salary(self, salary):   #gonna set new salary ,so used, salary        #authorized person
        self.__salary = salary

    # Method
    def display_info(self):
        return (
            f"Employee ID : {self.emp_id}\n"
            f"Name        : {self.name}\n"
            f"Salary      : ₹{self.__salary}"
        )

    # Method with Expression
    def calculate_bonus(self, percentage):
        bonus = self.__salary * percentage / 100
        return bonus



# ==========================================
# CHILD CLASS
# Single Inheritance
# ==========================================
class Developer(Employee):

    # Constructor
    def __init__(self, emp_id, name, salary, language):
        super().__init__(emp_id, name, salary)
        self.language = language

    # Method Overriding
    def display_info(self):
        parent = super().display_info()
        return (
            f"{parent}\n"
            f"Language    : {self.language}"
        )


# ==========================================
# GRANDCHILD CLASS
# Multilevel Inheritance
# ==========================================
class SeniorDeveloper(Developer):

    # Constructor
    def __init__(self, emp_id, name, salary, language, experience):
        super().__init__(emp_id, name, salary, language)
        self.experience = experience

    # Method Overriding
    def display_info(self):
        parent = super().display_info()
        return (
            f"{parent}\n"
            f"Experience  : {self.experience} Years"
        )


# ==========================================
# ANOTHER PARENT CLASS
# Used for Multiple Inheritance
# ==========================================
class Attendance:

    # Constructor
    def __init__(self, attendance):
        self.attendance = attendance

    # Method
    def attendance_info(self):
        return f"Attendance  : {self.attendance}%"


# ==========================================
# GREAT GRANDCHILD CLASS
# Multiple + Multilevel Inheritance
# ==========================================
class TeamLead(SeniorDeveloper, Attendance):

    # Constructor
    def __init__(self, emp_id, name, salary,
                 language, experience,
                 attendance, team):

        SeniorDeveloper.__init__(
            self,
            emp_id,
            name,
            salary,
            language,
            experience
        )

        Attendance.__init__(self, attendance)

        self.team = team

    # Method Overriding
    def display_info(self):
        parent = super().display_info()
        return (
            f"{parent}\n"
            f"Team        : {self.team}\n"
            f"{self.attendance_info()}"
        )


# ==========================================
# OBJECT CREATION
# ==========================================
employee = Employee(
    101,
    "Rahul",
    30000
)

developer = Developer(
    102,
    "Anita",
    50000,
    "Python"
)

senior = SeniorDeveloper(
    103,
    "Kiran",
    70000,
    "Java",
    6
)

lead = TeamLead(
    104,
    "Meena",
    90000,
    "Python",
    8,
    96,
    "AI Team"
)


# ==========================================
# UPDATE SALARY USING SETTER
# ==========================================

senior.set_salary(75000)
lead.set_salary(95000)

'''
senior.set_salary(75000)        #15%
lead.set_salary(95000)          #20%

senior.set_salary(75000)  #15%     #
lead.set_salary(100000) #50%
developer.set_salary(25000) #18%

senior.set_salary(100)        #15%
lead.set_salary(950)          #12%
'''
# ==========================================
# OUTPUT
# ==========================================
print("===== EMPLOYEE =====")
print(employee.display_info())
print(f"Bonus       : ₹{employee.calculate_bonus(10)}")

print("\n===== DEVELOPER =====")
print(developer.display_info())
print(f"Bonus       : ₹{developer.calculate_bonus(12)}")

print("\n===== SENIOR DEVELOPER =====")
print(senior.display_info())
print(f"Bonus       : ₹{senior.calculate_bonus(18)}")

print("\n===== TEAM LEAD =====")
print(lead.display_info())
print(f"Bonus       : ₹{lead.calculate_bonus(15)}")