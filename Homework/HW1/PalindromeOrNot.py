# Write a python program that reads in a string and determines 
# whether the string is a palindrome or not.


def check(string):
    reverse=string[::-1]
    print("String:",string)
    print("Reverse:",reverse)
    if(string==reverse):
        return True
    else:  
        return False

x = input("Enter a string: ")
if check(x):
    print(x,'is a palindrome!')
else:
    print(x,'is not a palidrome.')
