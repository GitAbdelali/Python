x = float(input("Enter x: "))
while x < -10 or x > 10:
        x = float(input("Invalid Value. Enter x: "))

y = float(input("Enter y: "))
while y < -10 or y > 10:
        y = float(input("Invalid Value. Enter y: "))

distance = (x**2 + y**2)**0.5

if distance < 8:
        print("It is in!")
else:
        print("Try again.")