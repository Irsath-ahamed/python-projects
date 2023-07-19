name = input('type your name: ')
print('welcome', name ,'to this adventures..!!')

answer=input(
    'you are in dirty road. and it has come to end. now make (right/left): ')

if answer == 'left':
    answer= input(
        'you came to river, now you can walk around it or swim (walk/swim): ')
    if answer == 'swim':
        print('you are eaten by alligator. you lost the game')
    elif answer == 'walk':
        print('you are walked many miles and died. you lost..!')
    else:
        print('pls enter valid answer')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
