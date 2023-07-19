val1= float(input('enter the num1: '))
val2= float(input('enter the num2: '))
operator= input ('enter the operator (+,-,*,/): ')

if operator == '+':
    answer= val1 + val2
    print(round(answer,3))
elif operator == '-':
    answer= val1 - val2
    print(round(answer,3))
elif operator == '*':
    answer= val1 * val2
    print(round(answer,3))
elif operator == '/':
    answer= val1 / val2
    print(round(answer,3))
else:
    print( operator , 'is not valid')