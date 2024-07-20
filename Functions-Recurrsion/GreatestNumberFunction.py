# Write a program using functions to find greatest of three numbers.

def GNF(num1, num2, num3):
    if(num1>num2 and num1>num3):
        print(f'{num1} is the greatest number')
    if(num2>num1 and num2>num3):
        print(f'{num2} is the greatest number')
    else:
        print(f'{num3} is the greates number')
