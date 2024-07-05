# This is to replace name and date with input given by the user

letter = '''
        Dear Name,
        You are selected!
        Date
        '''
Name = input("Enter Your Name: ")
Date = input("Enter the Date: ")
print(letter.replace("Name", Name).replace("Date",Date))