import numpy as np

class email(object):
    def __init__(self, host, name, numChar, espChar, Num, Esp, last_name):
        self.host = host
        self.name = name
        self.numChar = numChar
        self.espChar = espChar
        self.NNum = Num
        self.NEsp = Esp
        self.last_name = last_name
        self.email = []
        self.all = len(self.name) + len(self.last_name)
        
    def generate_name(self):
        a = np.random.randint(1, len(self.name)) 
        char = self.name[a]
        aux = ''.join(char)
        aux2 = list(aux)
        for i in aux2:
            self.email.append(i)
        return self.email
    
    def generate_lastname(self):
        char = self.generate_name()
        a = np.random.randint(1, len(self.last_name)) 
        char = self.last_name[a]
        aux = ''.join(char)
        aux2 = list(aux)
        for i in aux2:
            self.email.append(i)
        return self.email
    
    def CharNum(self):
        char = self.generate_lastname()
        for i in range(self.NNum):
            a = np.random.randint(1, len(self.numChar))
            b = np.random.randint(1, len(char))
            self.email[b] = self.numChar[a]
        return self.email
                  
    def CharEsp(self):
        char = self.CharNum()
        for i in range(self.NEsp):
            a = np.random.randint(1, len(self.espChar))
            b = np.random.randint(1, len(self.email))
            char[b] = self.espChar[a]
        return char 

    def arroba(self):
        h = "@"
        e = self.CharEsp()
        e.append(h)
        return e
        
    def Host(self):
        h = self.host
        e = self.arroba()
        e.append(h)
        return e 
        
    def com(self):
        h = ".com,"
        e = self.Host()
        e.append(h)
        return e
            
    def __str__(self):
        a = self.com()
        b = ''.join(a)
        self.clean()
        return b
    
    def clean(self):
        self.email = []

def email_generator(host='#', numbers = 1, Nesp_char = 1, nt = 1, doctxt = True):
    
    num_char = ['1','2','3','4','5','6','7','8','9','0']
    esp_char = ['$','&','_','-']
    x = np.loadtxt('first_name.txt', dtype=str)
    y = np.loadtxt('last_name.txt', dtype=str)
    
    k = email(host, x, num_char, esp_char,numbers,Nesp_char, y)
    g = ''
    for i in range(nt):
        g += k.__str__()
        
    li = g.split(',')
    if doctxt:
        txt(li)
    else:
        print(li)

    
def txt(a):
    f = open('Emails.txt', 'w')
    for i in a:
        f.write(i+'\n')
    print('Tu fichero se creo correctamente')
    f.close()
    
