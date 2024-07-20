# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    Sum = 0
    if(n==0):
        return 0
    else:
        return n+sum(n-1)

print(sum(5))
