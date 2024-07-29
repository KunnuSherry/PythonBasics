# Write a program to print third, fifth and seventh element from a list using enumerate
# function.

list = [1,2,3,4,5,6,7,8]
for index, item in enumerate(list):
    match index:
        case 2:
            print(f'{list[2]} is the third element.')
        case 4:
            print(f'{list[4]} is the fifth element.')
        case 6:
            print(f'{list[6]} is the seventh element.')
        case _:
            print(f'Not in question')

