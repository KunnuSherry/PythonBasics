# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

def game():
    with open('Hi-Score.txt', 'r') as f:
        text = f.read()
    prevHiScore = int(text)
    userNumber = int(input('Enter The Number Greater Than the previous one, if you remember it, it will be the new hi-score: '))
    if(userNumber>prevHiScore):
        print(f'Yeah! You Created a new Hi-Score {userNumber}')
        with open('Hi-Score.txt', 'w') as f:
            f.write(str(userNumber))
        
    else:{
        print('Sorry Better Luck Next time.')
    }
        
game()