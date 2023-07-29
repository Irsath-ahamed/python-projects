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
        print('pls enter valid answer, you lost')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
