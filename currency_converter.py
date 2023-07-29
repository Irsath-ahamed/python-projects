#methos:1

def main():
    
    print('this program will convert dollars to rupees:')

    dollars= eval(input('enter amount in dollar: '))
    rupees= dollars * 82.24
    print('this is', rupees, 'in rupees')
main()

#method:2 (using lambda)

def rupees():
    print()
    print('this program will convert dollars to rupees:')

    dollars= eval(input('enter amount in dollar: '))
    rupees= convert_to_rupees(dollars)
    print('this is', rupees, 'in rupeesss')
convert_to_rupees= lambda rupees : rupees * 82.24

rupees()
    


