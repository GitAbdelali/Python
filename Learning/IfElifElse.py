# Is used to check IF something is the case
# Mostly always is used with some sort of assignment operator (<,>,=,)
# <= - Less than or equal to
# >= - Greater than or equal to
# == - is equal to
# != - does not equal
# it's necessary to add a colon when using if,else & elif else statements

# Example

x = 5
y = 8

if x > y:
    print('x is greater than y')
# The above will not print because the statement provided is not true
if x < y: 
    print('x is less than y')
# The above will print because it is true
if x > y:
    print('x is greater than y')
else: 
    print('x is not greater than y')
# this will output the else statement because the if statement is false.
# else statements will only respond to the if statement that is above it

x = 5
y = 10
z = 22

if x > y:
    print('x is greater than y')
elif x < z:
    print('x is less than z')
else:
    print('if and elif(s) never ran')
# The elif statement, once true, will stop all other code in the block from running
    
