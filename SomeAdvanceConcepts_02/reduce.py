# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

list1 = [1,3,6,7,8,5,13,56,12]

maxnum = 0

def maximumFunc(x,y):
    return x if x>y else y

print(f' {reduce (maximumFunc, list1)} is the maximum number')
