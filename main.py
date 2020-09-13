
class Kalkulator():
    def __init__(self):
        self.historia = []
        pass

    def dodawanie(self,x,y):
        return print('wynik dodawania to: ',x+y)
    def odejmowanie(self,x,y):
        return print('wynik odejmowania to: ',x-y)
    def mnozenie(self,x,y):
        return print('wynik mnożenia to: ',x*y)
    def dzielenie(self,x,y):
        return print('wynik dzielenia to: ',x/y)
    def potegowanie(self,x,y):
        if x == 0:
            return 1
        elif x == 1:
            return x
        else:
            return print('wynik pierwiastowania to: ',x**y)
    def pierwiastkowanie(self,x,y):
        return print('wynik pierwiastowania to: ',x**(1.0/y))
        
    def menu(self):
        i=-1
        while i <=10:
            print('- Menu -')
            print('- 1.Dodawanie -')
            print('- 2.Odejmowanie -')
            print('- 3.Mnożenie -')
            print('- 4.Dzielenie -')
            print('- 5.Potęgowanie -')
            print('- 6.Pierwiaskowanie -')
            print('- 10.Exit -')
            i = int(input())
            if i == 1:
                print('Podaj pierwszą liczbę')
                x = int(input())
                print('Podaj drugą liczbę')
                y = int(input())
                calc.dodawanie(x,y)
            if i == 2:
                print('Podaj pierwszą liczbę')
                x = int(input())
                print('Podaj drugą liczbę')
                y = int(input())
                calc.odejmowanie(x,y)
            if i == 3:
                print('Podaj pierwszą liczbę')
                x = int(input())
                print('Podaj drugą liczbę')
                y = int(input())
                calc.mnozenie(x,y)
            if i == 4:
                print('Podaj pierwszą liczbę')
                x = int(input())
                print('Podaj drugą liczbę')
                y = int(input())
                calc.dzielenie(x,y)
            if i == 5:
                print('Podaj pierwszą liczbę')
                x = int(input())
                print('Podaj stopień potęgi')
                y = int(input())
                calc.potegowanie(x,y)
            if i == 6:
                print('Podaj pierwszą liczbę')
                x = int(input())
                print('Podaj stopień pierwiastka')
                y = int(input())
                calc.pierwiastkowanie(x,y)
            if i == 10:
                break
            i +=1
        
if __name__ == "__main__":
    calc = Kalkulator()
    calc.menu()

    
    
