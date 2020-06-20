s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
  d = {'upper': 0, 'lower': 0}
  for letter in s:
    #if letter.upper()
    if letter.isalpha() and letter.isupper():
      d['upper'] += 1
    #elif letter.lower()
    elif letter.isalpha() and letter.islower():
      d['lower'] += 1
    else:
      pass
  print('Orginal str:', s)
  print('uppercase #:', d['upper'])
  print('lowercase #:', d['lower'])
  #print(d)
up_low(s)