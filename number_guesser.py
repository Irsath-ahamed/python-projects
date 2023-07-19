import random

top_of_range = input('enter the number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
       print('pls enter above the 0')
       quit() 
else:
    print('pls type olny a number!!')
    quit()

random_number = random.randint(0, top_of_range)
print(random_number)
guesses= 0

while True:
    guesses += 1
    user_guesse= input('make a guess: ')
    if user_guesse.isdigit():
        user_guesse=int(user_guesse)
    else:
        print('type only a number')

    if user_guesse == random_number:
        print('you got it')
        break
    elif user_guesse > random_number:
        print('you were above the range')
    else:
        print('you were the below range')

print('you got it in' , guesses , 'guess')