
def replace_word():
    str = ' hi.. irsath, how are you irsath, bye irsath'
    print(str)
    existing_word= input('enter what you want to change above the word from: ')
    replace_word= input('enter a word ' + existing_word + ' to: ' )
    
    print(str.replace(existing_word,replace_word))
    print('replaced successfully!!!')

replace_word()

