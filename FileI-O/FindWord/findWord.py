# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

f = open('twinkle.txt' , 'r')
text = f.read()
if("twinkle" in text):
    print("yes!")
else:
    print('no!')