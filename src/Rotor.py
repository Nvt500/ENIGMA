class Rotor:
    
    rotor1Map = {
        'A' : 'F',
        'B' : 'Z',
        'C' : 'X',
        'D' : 'U',
        'E' : 'I',
        'F' : 'K',
        'G' : 'M',
        'H' : 'Q',
        'I' : 'N',
        'J' : 'A',
        'K' : 'L',
        'L' : 'D',
        'M' : 'P',
        'N' : 'Y',
        'O' : 'B',
        'P' : 'R',
        'Q' : 'W',
        'R' : 'H',
        'S' : 'C',
        'T' : 'E',
        'U' : 'V',
        'V' : 'G',
        'W' : 'O',
        'Y' : 'J',
        'X' : 'T',
        'Z' : 'S'
    }
    rotor2Map = {
        'A' : 'K',
        'B' : 'X',
        'C' : 'Y',
        'D' : 'A',
        'E' : 'O',
        'F' : 'S',
        'G' : 'U',
        'H' : 'D',
        'I' : 'M',
        'J' : 'R',
        'K' : 'W',
        'L' : 'Z',
        'M' : 'I',
        'N' : 'C',
        'O' : 'T',
        'P' : 'J',
        'Q' : 'F',
        'R' : 'V',
        'S' : 'E',
        'T' : 'L',
        'U' : 'N',
        'V' : 'Q',
        'W' : 'H',
        'Y' : 'P',
        'X' : 'G',
        'Z' : 'B'
    }
    rotor3Map = {
        'A' : 'W',
        'B' : 'N',
        'C' : 'A',
        'D' : 'H',
        'E' : 'T',
        'F' : 'M',
        'G' : 'L',
        'H' : 'S',
        'I' : 'B',
        'J' : 'O',
        'K' : 'Z',
        'L' : 'F',
        'M' : 'R',
        'N' : 'U',
        'O' : 'D',
        'P' : 'E',
        'Q' : 'C',
        'R' : 'X',
        'S' : 'V',
        'T' : 'G',
        'U' : 'K',
        'V' : 'I',
        'W' : 'P',
        'Y' : 'J',
        'X' : 'Q',
        'Z' : 'Y'
    }
    
    
    def __init__(self, ALPHABET):
        
        self.rotor1 = list(ALPHABET)
        self.rotor2 = list(ALPHABET)
        self.rotor3 = list(ALPHABET)
    
    
    def rotate(self):
        
        if self.rotor2[0] == 'Z':
            rotor = self.rotor3
            tmp = rotor[0]
            
            for i in range(len(rotor)):
                if i == len(rotor)-1:
                    rotor[i] = tmp
                    break
                rotor[i] = rotor[i+1]
            self.rotor3 = rotor
        if self.rotor1[0] == 'Z':
            for e in range(1):
                rotor = self.rotor2
                tmp = rotor[0]
                
                for i in range(len(rotor)):
                    if i == len(rotor)-1:
                        rotor[i] = tmp
                        break
                    rotor[i] = rotor[i+1]
                self.rotor2 = rotor
        
        for e in range(2):
            rotor = self.rotor1
            tmp = rotor[0]
            
            for i in range(len(rotor)):
                if i == len(rotor)-1:
                    rotor[i] = tmp
                    break
                rotor[i] = rotor[i+1]
            self.rotor1 = rotor
    
    
    def switch(self, num, decode=None):
        
        if decode:
            num = list(decode.keys())[num]
            num = list(self.rotor1Map.values()).index(num)
            num = self.rotor2[num]
            num = list(self.rotor2Map.values()).index(num)
            num = self.rotor3[num]
            num = list(self.rotor3Map.values()).index(num)
            return num
        
        num = self.rotor1[num]
        num = list(self.rotor1Map.values()).index(num)
        num = self.rotor2[num]
        num = list(self.rotor2Map.values()).index(num)
        num = self.rotor3[num]
        num = list(self.rotor3Map.values()).index(num)
        return num
    
    
    def backwardsSwitch(self, num):
        
        num = list(self.rotor3Map.values())[num]
        num = self.rotor3.index(num)
        num = list(self.rotor2Map.values())[num]
        num = self.rotor2.index(num)
        num = list(self.rotor1Map.values())[num]
        num = self.rotor1.index(num)
        num = self.rotor1[num]
        return num
    
    
    def showRotors(self):
        
        for i in range(len(self.rotor1)):
            print(self.rotor1[i] + '    ' + list(self.rotor1Map.values())[i] + '\t\t' + self.rotor2[i] + '    ' + list(self.rotor2Map.values())[i] + '\t\t' + self.rotor3[i] + '    ' + list(self.rotor3Map.values())[i] + '\n')