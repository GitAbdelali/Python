# Write a Python program that does the following:
#     Reads in a principal amount (A floating point number)
#     Reads in the annual percentage interest rate for the investment
#     Displays the number of years it will take for the investment to double
#             DO NOT USE RULE OF 72


prinAmount = float(input("Enter principal amount:"))
annualIR = float(input("Enter percentage annual interest rate:"))
ROI = 2 * prinAmount 
year = 0
balance = prinAmount

while balance < ROI:
    year += 1
    interest = balance * annualIR / 100
    balance += interest


print("It will take", year, "years for the investment to double.")








