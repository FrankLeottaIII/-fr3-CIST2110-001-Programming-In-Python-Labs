#Lab3
#Author: Frank R. Leotta III

"""_summary_
This lab is designed to get you familiar with Python input(), converting data types, and using the round() function.
"""

# 1. Ask the user for their name and assign it to a variable called "name".
name = input("What is your name? ")
# 2. Ask the user for their age and assign it to a variable called "age".
age = int(input("What is your age? "))
# 3. Ask the user for a balance and assign it to a variable called "balance".
balance = float(input("What is your balance for this account? "))
# 4. Ask the user for a number of years to calculate interest and assign it to a variable called "years".
years = float(input("How many years do you plan on keeping this balance? "))
# 5. Ask the user for an interest rate and assign it to a variable called "interest_rate".
interest_rate = float(input("What is the interest rate for this account? "))
# 6. Convert the balance, years, and interest_rate to float data types.
# Note: This is only necessary if you did not specify the data type in the input() function...
## doing it anyway because why not
years = float(years)
# 7. Calculate the future balance using the formula: balance * (1 + interest_rate/100) ** years
future_balance = balance * (1 + interest_rate/100) ** years
# 8. Round the future balance to 2 decimal places using the round() function.
future_balance = round(future_balance, 2)
# 9. Print the following sentence using string concatenation: "Hello <name>, your balance after <years> years will be $<future_balance>."
print("Hello " + name + ", your balance after " + str(years) + " years will be $" + str(future_balance) + ".")

## this is basic interest calculator typically not used for monthly payments or savings accounts... still good for APR calculations... Not APY  
## APY = (1 + r/n)^n - 1
## r = interest rate
## n = number of times interest is compounded per year
## APY = Annual Percentage Yield
## APR = Annual Percentage Rate
# APR is the simple interest rate you pay over one year.
## APY is the actual interest earned or paid in one year, taking into account the effect of compounding.
#

