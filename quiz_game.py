print('Welcome to the quiz!')

playing= input('do you want to play?(yes/no): ')
if playing.lower()!= 'yes':
    quit()
print('ok..lets we start!!')
score = 0

answer = input('what does CPU stands for? ')
if answer.lower() == 'central processing unit':
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input('what does RAM stands for? ')
if answer.lower() == 'random access memory':
    print('correct')
    score += 1
else:
    print('incorrect')


answer = input('what does GPU stands for? ')
if answer.lower() == 'graphics processing unit':
    print('correct')
    score += 1
else:
    print('incorrect')


answer = input('what does LAN stands for? ')
if answer.lower() == 'local area network':
    print('correct')
    score += 1
else:
    print('incorrect')


print('you got '+ str((score/4)*100) + '%')
print('you got ' + str(score) + ' marks' )
