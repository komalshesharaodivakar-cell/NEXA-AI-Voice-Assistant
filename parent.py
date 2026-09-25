# ==========================================
# EMPLOYEE MANAGEMENT SYSTEM
# Covers:
# Class, Object, Method
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
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    # Method
    def display_info(self):
        return (
            f"Employee ID : {self.emp_id}\n"
            f"Name        : {self.name}"
        )


# ==========================================
# CHILD CLASS
# Single Inheritance
# ==========================================
class Developer(Employee):

    # Constructor
    def __init__(self, emp_id, name, language):
        super().__init__(emp_id, name)
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
    def __init__(self, emp_id, name, language, experience):
        super().__init__(emp_id, name, language)
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
class TeamLead(SeniorDeveloper, Attendance):         #senior developer from grandchild , attendance from another new parent

    # Constructor
    def __init__(self, emp_id, name, language,
                 experience, attendance, team):

        # Initialize SeniorDeveloper hierarchy
        SeniorDeveloper.__init__(                          #we using instead of super().init giving senior developer and attendance bcz it is from new parent not from the old employee or first parent.
            self, emp_id, name, language, experience
        )

        # Initialize Attendance class
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
    "Rahul"
)

developer = Developer(
    102,
    "Anita",
    "Python"
)

senior = SeniorDeveloper(
    103,
    "Kiran",
    "Java",
    6
)

lead = TeamLead(
    104,
    "Meena",
    "Python",
    8,
    96,
    "AI Team"
)


# ==========================================
# OUTPUT
# ==========================================

print("===== EMPLOYEE =====")
print(employee.display_info())

print("\n===== DEVELOPER =====")
print(developer.display_info())

print("\n===== SENIOR DEVELOPER =====")
print(senior.display_info())

print("\n===== TEAM LEAD =====")
print(lead.display_info())