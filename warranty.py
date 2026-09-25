# ==========================================
# ANOTHER PARENT CLASS
# Used for Multiple Inheritance
# ==========================================

# Warranty class
class Warranty:

    # Constructor
    def __init__(self, warranty_years):

        # Store warranty period
        self.warranty_years = warranty_years

    # Method to display warranty
    def warranty_info(self):

        # Return warranty information
        return f"Warranty     : {self.warranty_years} Years"