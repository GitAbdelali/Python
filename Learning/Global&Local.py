# Global Variable - Accessed anywhere
# Local Variable - Within it's function

# EXAMPLES OF GLOBAL VARIABLE

x = 6 

def example():
    global x 
    print(x)
    x+=5
    print(x)

example()

# or

# def example():
  
#   globx = x
#   print(globx)
#   globx+=5
#   print(globx)

# example()

# or

# def example():
  
#   globx = x
#   print(globx)
#   globx+=5
#   print(globx)

#   return globx

# x = example()
# print(x)
