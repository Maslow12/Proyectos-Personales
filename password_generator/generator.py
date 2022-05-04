import numpy as np

class generator(object):
    def __init__(self,arg,arg_2,arg_3,arg_4,length):
        self.charm = arg
        self.charM = arg_2
        self.charE = arg_3
        self.charN = arg_4
        self.length = length
        self.empty = []
        self.password = ''
        self.a = self.length/4
        
    def __str__(self):
        a = self.alf_charN()
        p = ''.join(a)
        return p
        
    def alf_charm(self):
        for i in range(self.length):
            a = np.random.randint(0, len(self.charm)) 
            g = self.charm[a]
            self.empty.append(g)
            
        return self.empty

    def alf_charM(self):
        a = np.random.randint(1, self.a) 
        char = self.alf_charm()
        for i in range(a):
            b = np.random.randint(0, self.length-1)
            c = np.random.randint(0, len(self.charM))
            char[b] = self.charM[c]
        return char
    
    def alf_charE(self):
        a = np.random.randint(1, self.a+2) 
        char = self.alf_charM()
        for i in range(a):
            b = np.random.randint(0, self.length)
            c = np.random.randint(0, len(self.charE))
            char[b] = self.charE[c]
        return char
    
    def alf_charN(self):
        a = np.random.randint(1, self.a) 
        char = self.alf_charE()
        for i in range(a):
            b = np.random.randint(1, self.length)
            c = np.random.randint(0, len(self.charN))
            char[b] = self.charM[c]
        return char
        
    
def PassGen(N):
    alf_char_m = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alf_char_M = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    esp_char = ['!','@','#','$','^','&','*','(',')',',','.','/',';','{',',','=']
    num_char = ['1','2','3','4','5','6','7','8','9','0']

    g = generator(alf_char_m, alf_char_M, esp_char, num_char, N)
    p = g.__str__()
    print('Contrasenia generada: ' + p)