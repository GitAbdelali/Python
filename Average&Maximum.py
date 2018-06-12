# Write a Python program that reads in 3 numbers and displays the following:
# a) the average of the three numbers
# b) the maximum fo the three numbers


print("Please enter three numbers of your choosing.")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))

if (num1 > num2) and (num1 > num3):
      maximum = num1
elif (num2 > num1) and (num2 > num3):
      maximum = num2
else: maximum = num3

average = ((num1 + num2 + num3)/3)
print ("The average of the three numbers is:", average)
print ("The Maximum of the numbers is:", maximum)

