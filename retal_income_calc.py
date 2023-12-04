# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. Our client's name is Brandon from a company called "Bigger Pockets". 
# Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.
# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.
# the equation for the ROI is annual_Cashflow / total_investment

class Rental_Income_Calc:
    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.total_investment = 0
        self.annual_cashflow = 0

    # Income function    
    def income(self):
        user_income = float(input("Please enter the monthly income you generate from the from the property"))
        self.monthly_income = user_income
        return self.monthly_income
        
    # Expense function
    def expenses(self):
        print("Please give me some information about your monthly expenses")
        property_tax = float(input("how much do you pay in property tax"))
        insurance = float(input("how much do you pay for insurance"))
        mortage = float(input("how much do you pay for your mortage"))
        ultilies = float(input("how much do you pay in utilites"))
        
        self.monthly_expenses = property_tax + insurance + mortage + ultilies
        return self.monthly_expenses
        
    # Cashflow function
    def cashflow_calc(self):
        self.expenses()
        cashflow = self.monthly_income - self.monthly_expenses
        self.annual_cashflow = cashflow * 12
        return self.annual_cashflow      
    
    # CashonCash Function
    def cashoncash(self):
        downPayment = float(input("how much did you put down on your loan"))
        closingCost = float(input("how much were the closing cost"))
        refirb = float(input("how much did you spend on refirishing the property"))
        self.total_investment = downPayment + closingCost + refirb
        return self.total_investment
    
    # ROI calculations
    def roi_calculations(self):
        cash_ROI = self.annual_cashflow / self.total_investment
        return cash_ROI

# Create an instance of the class and call the methods
rental_calc = Rental_Income_Calc()
rental_calc.income()
rental_calc.cashflow_calc()
rental_calc.cashoncash()
print(rental_calc.roi_calculations())
         