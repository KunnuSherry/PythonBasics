# Write a program to filter a list of numbers which are divisible by 5.

listx = [5,19,23,45,55,12,34]
def div5(x):
    return x%5==0

listAns = list(filter(div5, listx))
print(listAns)