code = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
  cryptograph = []
  normalsentence = []
  a = '>> '
  mode = ''
  mode = input('1. encryptor, 2. decryptor : ')
  if mode == '2':
    key = int(input(' Please enter the key for caesar cipher : '))
    print(' ')
    print('-'*10, ' mode : decryptor/ key : ', key, '-'*10)
    cryptograph = input(' Please enter your caesar cipher here : ')
    for i in cryptograph:
      if i == ' ':
        normalsentence.append(' ')
      else:
        if code.index(i) - key > -1:
          normalsentence.append(code[code.index(i) - key])
        else:
          normalsentence.append(code[25-(key-code.index(i))])
    for i in normalsentence:
      a = a + i
    print(a)
  elif mode == '1':
    key = int(input(' Please enter the key for caesar cipher : '))
    print(' ')
    print('-'*10, ' mode : encryptor/ key : ', key, '-'*10)
    #print(" I'm working on it. You can use decryptor only:(")
    normalsentence = input(' Please enter your sentence here : ')
    for i in normalsentence:
      if i == ' ':
        cryptograph.append(' ')
      else:
        if code.index(i) + key < 26:
          cryptograph.append(code[code.index(i) + key])
        else:
          cryptograph.append(code[(key+code.index(i)-25)])
    for i in cryptograph:
      a = a + i
    print(a)
  else:
    print(' Please enter 1 or 2')
