class Stecker:
    
    stecker = {
        'A' : 'B',
        'B' : 'A',
        'C' : 'C',
        'D' : 'D',
        'E' : 'O',
        'F' : 'T',
        'G' : 'R',
        'H' : 'H',
        'I' : 'I',
        'J' : 'J',
        'K' : 'K',
        'L' : 'P',
        'M' : 'M',
        'N' : 'N',
        'O' : 'E',
        'P' : 'L',
        'Q' : 'Q',
        'R' : 'G',
        'S' : 'S',
        'T' : 'F',
        'U' : 'U',
        'V' : 'V',
        'W' : 'W',
        'Y' : 'X',
        'X' : 'Y',
        'Z' : 'Z'
    }
    
    def switch(self, char):
        
        return list(self.stecker.values()).index(char)
    
    
    def showStecker(self):
        
        for i in range(len(self.stecker.values())):
            print(list(self.stecker.keys())[i] + '\t' + list(self.stecker.values())[i] + '\n')