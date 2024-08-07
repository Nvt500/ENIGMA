import Stecker as s
import Rotor as ro
import Reflector as re

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def procedure(letter, decode=None):
    
    letter = Stecker.switch(letter)
    letter = Rotor.switch(letter, decode)
    letter = Reflector.switch(letter)
    letter = Rotor.backwardsSwitch(letter)
    letter = Stecker.switch(letter)
    return ALPHABET[letter]

def every5Letters(list_):
    
    tmp = ''
    for l in list_:
        tmp += l
        if len(tmp.replace(' ', '')) % 5 == 0:
            tmp += ' '
    return tmp

with open('in.txt', 'r') as f:
    fileIn = f.read()
fileIn = ''.join(i for i in fileIn if i.isalpha())
fileIn = fileIn.upper()
if len(fileIn) > 10000:
    print("Message is too large.")
else:
    while True:
        inp = input('Do you want to [encode] or [decode]? ')
        if inp.lower() == 'encode':
            encode = True
        elif inp.lower() == 'decode':
            encode = False
        else:
            continue
        break
    
    Stecker = s.Stecker()
    
    Rotor = ro.Rotor(ALPHABET)

    Reflector = re.Reflector()
    
    if encode:
        newFile = ''
        steckerMap = Stecker.stecker
        for l in fileIn:
            newFile += procedure(l, steckerMap)
            Rotor.rotate()
    else:
        tmp = fileIn
        for i in range(1):
            newFile = ''
            steckerMap = Stecker.stecker
            for l in tmp:
                newFile += procedure(l, steckerMap)
                Rotor.rotate()
            tmp = newFile
            tmp = list(tmp)
            for e, char in enumerate(tmp):
                if char == 'Z':
                    tmp[e] = 'G'
                if char == 'G':
                    tmp[e] = 'Z'
                if char == 'X':
                    tmp[e] = 'Y'
                if char == 'Y':
                    tmp[e] = 'X'
            
            tmp = ''.join(tmp)
            
        newFile = tmp

    fileIn = every5Letters(fileIn)
    newFile = every5Letters(newFile)

    with open('out.txt', 'w') as f:
        f.write(newFile)