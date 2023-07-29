from PyDictionary import PyDictionary

dictionary= PyDictionary

word=input('enter your word: ')

print( dictionary.meaning(word))
while True:
  if word== '':
    break
  print(dictionary.meaning(word))