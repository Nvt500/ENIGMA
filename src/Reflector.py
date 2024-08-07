class Reflector:
    
    reflectorMap = {
        'A' : 'X',
        'B' : 'R',
        'C' : 'U',
        'D' : 'H',
        'E' : 'Q',
        'F' : 'S',
        'G' : 'L',
        'H' : 'D',
        'I' : 'P',
        'J' : 'Y',
        'K' : 'N',
        'L' : 'G',
        'M' : 'O',
        'N' : 'K',
        'O' : 'M',
        'P' : 'I',
        'Q' : 'E',
        'R' : 'B',
        'S' : 'F',
        'T' : 'Z',
        'U' : 'C',
        'V' : 'W',
        'W' : 'V',
        'Y' : 'J',
        'X' : 'A',
        'Z' : 'T'
    }
    
    
    def switch(self, char):
        
        return list(self.reflectorMap.keys()).index(list(self.reflectorMap.values())[char])