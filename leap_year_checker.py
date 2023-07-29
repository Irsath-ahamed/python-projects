
while True:
    year =eval(input('0 to quit/enter year: '))
    
    if year == (0):
        break
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap Year' )
            else:
                print('Not leap year')
        else:
            print('Leap year' )
    else:
        print('Not Leap Year')


