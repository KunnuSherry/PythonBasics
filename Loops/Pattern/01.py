#   *
#  ***
# *****  for n=3

n=3

for i in range(1,n+1):
    for j in range (1,4-i):
        print(" ", end='')
    for k in range (1, 2*i):
        print('*', end='')
    print('\n')
        
