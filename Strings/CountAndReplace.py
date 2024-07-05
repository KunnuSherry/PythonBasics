# This is a program to count the double spaces in a string

Str = input("Enter the string: ")
print("The Number of double spaces are: ",Str.count("  "))

# This is a program to replace the double spaces with underscore

str1 = Str.replace("  ", "_")
print(str1)