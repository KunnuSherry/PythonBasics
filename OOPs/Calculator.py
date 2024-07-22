# Write a class “Calculator” capable of finding square, cube and square root of a
# number
import math
class Calculator:
    def __init__(self, number, operation):
        self.number = number
        self.operation = operation
        print(f'performing {operation} on {number}')
    def square(self):
        return (self.number)**2
    def cube(self):
        return (self.number)**3
    def sqrt(self):
        return math.sqrt((self.number))
    def getAns(self):
        if(self.operation == 'square'):
            return self.square()
        elif(self.operation == 'cube'):
            return self.cube()
        elif(self.operation == 'square root'):
            return self.sqrt()
        else:
            return 'Error in user input'
        
    
num = int(input('Enter the Number: '))
operation = input('Enter the Operation(square, cube, square root): ')

Calculator1 = Calculator(num, operation)
print(f"The answer is : {Calculator1.getAns()}")
