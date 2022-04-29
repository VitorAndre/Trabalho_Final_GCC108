class Soma:
    def __init__(self):
        self.fita = ['B']
        self.posCabecote = 0 #posição do cabeçote
    
    def soma(self, num1, num2):
        for i in list(num1):
            self.fita.append(i)
        
        self.fita.append('B')
    
        for i in list(num2):
            self.fita.append(i)

        self.fita.append('B')
        self.q0()
    
    def q0(self):
        if (self.fita[self.posCabecote] == 'B'):
            self.posCabecote += 1
            self.q0()
        elif self.fita[self.posCabecote] == '1' or self.fita[self.posCabecote] == '0':
            self.posCabecote += 1
            self.q1()

    def q1(self):
        if self.fita[self.posCabecote] == 'B':
            self.posCabecote += 1
            self.q2()
        else:
            self.posCabecote += 1
            self.q1()    

    def q2(self):
        if (self.fita[self.posCabecote] == 'B'):
            self.posCabecote -= 1
            self.q3()
        elif(self.fita[self.posCabecote] == '0' or self.fita[self.posCabecote] == '1'):
            self.posCabecote += 1
            self.q2()
    
    def q3(self):
        if (self.fita[self.posCabecote] == '0'):
            self.fita[self.posCabecote] = 'B'
            self.posCabecote -= 1
            self.q4()
        elif self.fita[self.posCabecote] == '1':
            self.fita[self.posCabecote] = 'B'
            self.posCabecote -= 1
            self.q6()
        elif self.fita[self.posCabecote] == 'B':
            self.posCabecote -= 1
            self.q9()
    
    def q4(self):
        if (self.fita[self.posCabecote] == 'B'):
            self.posCabecote -= 1
            self.q5()
        elif(self.fita[self.posCabecote] == '0' or self.fita[self.posCabecote] == '1'):
            self.posCabecote -= 1
            self.q4()
    
    def q5(self):
        if (self.fita[self.posCabecote] == 'X' or self.fita[self.posCabecote] == 'Y'):
            self.posCabecote -= 1
            self.q5()
        elif(self.fita[self.posCabecote] == '0'):
            self.fita[self.posCabecote] = 'X'
            self.posCabecote += 1
            self.q1() 
        elif self.fita[self.posCabecote] == '1':
            self.fita[self.posCabecote] = 'Y'
            self.posCabecote += 1
            self.q1()
    
    def q6(self):
        if (self.fita[self.posCabecote] == 'B'):
            self.posCabecote -= 1
            self.q7()
        elif(self.fita[self.posCabecote] == '0' or self.fita[self.posCabecote] == '1'):
            self.posCabecote -= 1
            self.q6()
    
    def q7(self):
        if (self.fita[self.posCabecote] == '1'):
            self.fita[self.posCabecote] = 'X'
            self.posCabecote -= 1
            self.q8()
        elif self.fita[self.posCabecote] == '0':
            self.fita[self.posCabecote] = 'Y'
            self.posCabecote += 1
            self.q1()
        elif(self.fita[self.posCabecote] == 'X' or self.fita[self.posCabecote] == 'Y'):
            self.posCabecote -= 1
            self.q7()

    def q8(self):
        if (self.fita[self.posCabecote] == '1'):
            self.fita[self.posCabecote] = '0'
            self.posCabecote -= 1
            self.q8()
        elif(self.fita[self.posCabecote] == 'B'):
            self.fita.insert(0, 'B')
            self.posCabecote += 1
            self.fita[self.posCabecote] = '1'
            self.posCabecote += 1
            self.q1()
        elif self.fita[self.posCabecote] == '0':
            self.fita[self.posCabecote] = '1'
            self.posCabecote += 1
            self.q1()

    def q9(self):
        if (self.fita[self.posCabecote] == 'B'):
            self.q10()
        elif(self.fita[self.posCabecote] == '0' or self.fita[self.posCabecote] == '1'):
            self.posCabecote -= 1
            self.q9()
        elif(self.fita[self.posCabecote] == 'X'):
            self.fita[self.posCabecote] = '0'
            self.posCabecote -= 1
            self.q9()
        elif self.fita[self.posCabecote] == 'Y':
            self.fita[self.posCabecote] = '1'
            self.posCabecote -= 1
            self.q9()
    
    def q10(self):
        print(''.join(self.fita))

    
m = Soma()
num1 = input("Primeiro numero: ")
num2 = input("Segundo numero: ")
if (len(num2) > len(num1)):
    num1, num2 = num2, num1
m.soma(num1, num2)