class Calc:
    result = 0
    def setData(self, fir, sec):
        self.fir = fir
        self.sec = sec
    def add(self):
        Calc.result += 1
        self.result = self.fir + self.sec
    def getData(self):
        print(self.result, end=" ")
        print(Calc.result)

a = Calc()
b = Calc()
a.setData(5,10)
b.setData(3,2)
a.add()
a.getData()
b.add()
b.getData()