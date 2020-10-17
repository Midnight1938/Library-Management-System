from random import choice
sentence = 'Hello World'
print(''.join(choice((str.upper, str.lower))(c) for c in sentence))
