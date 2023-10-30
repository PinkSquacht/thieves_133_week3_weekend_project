# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. Our client's name is Brandon from a company called "Bigger Pockets". 
# Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.
# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property.
# the equation for the ROI is annual_Cashflow / total_investment

class Rental_Income_Calc:
    def __init__(self):
        pass
    
    # Income function    
    def income(self):
        self.user_income = float(input("Please enter the monthly income you generate from the from the property"))
        self.monthly_income = self.user_income
        return self.monthly_income
        
    # Expense function
    def expenses(self):
        print("Please give me some information about your monthly expenses")
        self.property_tax = float(input("how much do you pay in property tax"))
        self.insurance = float(input("how much do you pay for insurance"))
        self.mortage = float(input("how much do you pay for your mortage"))
        self.ultilies = float(input("how much do you pay in utilites"))
        
        self.monthly_Expenses = self.property_tax + self.insurance + self.mortage + self.ultilies
        return self.monthly_Expenses
        
    # Cashflow function
    def cashflow_calc(self):
        self.expenses()
        self.cashflow = self.monthly_income - self.monthly_Expenses
        self.annual_cashflow = self.cashflow * 12
        return self.annual_cashflow      
    # CashonCash Funtion
    def cashoncash(self):
        self.downPayment = float(input("how much did you put down on your loan"))
        self.closingCost = float(input("how much were the closing cost"))
        self.refirb = float(input("how much did you spend on refirishing the property"))
        self.total_investment = self.downPayment + self.closingCost + self.refirb
        return self.total_investment
    # ROI calculations
    def roi_calculations(self):
        self.cash_ROI = self.annual_cashflow / self.total_investment
        return self.cash_ROI
         