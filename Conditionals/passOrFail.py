marks1 = int(input("Enter the marks of the 1st subject: "))
marks2 = int(input("Enter the marks of the 2nd subject: "))
marks3 = int(input("Enter the marks of the 3rd subject: "))

if((marks1+marks2+marks3)>=120 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Passed!")
else:
    print("Sorry You're Failed.")
    