
def view():
    with open ('password.txt' , 'r') as f:
        for line in f.readlines():
            data= line.rstrip()
            user, passw= data.split('|')
            print('user: ', user , '| passw: ', passw)

def add():
    name= input('account name: ')
    pwd= input('password: ')

    with open ('password.txt' , 'a') as f:
        f.write( name + '|' + pwd + '\n' )



while True:
    mode= input('type if you are add or view the password (add/view) or q to break? ').lower()

    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print ('invalid value')
        continue