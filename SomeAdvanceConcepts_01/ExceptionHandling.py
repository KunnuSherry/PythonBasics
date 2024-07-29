# Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

a = int(input("Enter Number1: "))
b = int(input("Enter Number2: "))

if(b!=0):
    print(f'Division is {a/b}')
    
else:
    raise ZeroDivisionError('Infinite')
    

