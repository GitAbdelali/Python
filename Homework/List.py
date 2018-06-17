# Write a Python program that reads in a list of integers and displays the following:
# A) The average of the numbers in the list
# B) The median value of the numbers
# C) The number of even numbers in the list


import math

# Part A
print("Please enter a list of integers:")
arr = [int(x) for x in input().split()]
numArr = len(arr)
average = sum(arr) / float(len(arr))

print("The average of the numbers is:",average)

#Part B
if numArr % 2 == 0:
    median = ((arr[math.ceil(numArr/2)-1]) + (arr[math.ceil(numArr/2)]))/2
else:
    median = arr[math.ceil(numArr/2)-1]

print("The median value of the numbers is:",median)
# Part C
evenCount = 0
for number in arr:
    if number % 2 == 0:
        evenCount += 1

print("The number of even numbers in the list is:",evenCount)



