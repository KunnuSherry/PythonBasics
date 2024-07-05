# A program to accept marks of 6 students and display them in a sorted manner.

marks=[]
marks1=int(input("Enter marks for student 1: "))
marks2=int(input("Enter marks for student 2: "))
marks3=int(input("Enter marks for student 3: "))
marks4=int(input("Enter marks for student 4: "))
marks5=int(input("Enter marks for student 5: "))
marks6=int(input("Enter marks for student 6: "))
marks.append(marks1)
marks.append(marks2)
marks.append(marks3)
marks.append(marks4)
marks.append(marks5)
marks.append(marks6)
marks.sort()
print(marks)