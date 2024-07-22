# A file contains a word “Donkey” multiple times. You need to write a programn which replace this word with by updating the same file. 

with open('donkey.txt', 'r') as f:
    text = f.read()

num = text.count('donkey')
print(f'The Word Donkey is Written {num} times')

upd_txt = text.replace('donkey', '####')

with open('donkey.txt', 'w') as f:
    f.write(upd_txt)