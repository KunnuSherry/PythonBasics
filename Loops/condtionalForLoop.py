# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]
for items in l:
    if(items[0] == 's' or items[0] == 'S'):
        print(items)
