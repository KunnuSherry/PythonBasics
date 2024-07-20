num = int(input('Enter The Number: '))
if num == 2 :
    print('It is a PRIME number')
else:
    for i in range (2,num):
        if (num % i == 0 ):
            break
        else:
            print('It is a PRIME number')
      