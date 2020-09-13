from tkinter import *

class Kalkulator():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x300')
        self.root.configure(background='#F0F8FF')

        self.pole = Entry(self.root).grid(row=0,column=0,columnspan=4)
        self.B7 = Button(self.root, text ="7", command = self.dodawanie).grid(row=1,column=0)
        #self.B7.config(height=100, width=100)
        self.B8 = Button(self.root, text ="8", command = self.dodawanie).grid(row=1,column=1)
        self.B9 = Button(self.root, text ="9", command = self.dodawanie).grid(row=1,column=2)
        self.Bx = Button(self.root, text ="x", command = self.dodawanie).grid(row=1,column=3)
        self.B4 = Button(self.root, text ="4", command = self.dodawanie).grid(row=2,column=0)
        self.B5 = Button(self.root, text ="5", command = self.dodawanie).grid(row=2,column=1)
        self.B6 = Button(self.root, text ="6", command = self.dodawanie).grid(row=2,column=2)
        self.Bminus = Button(self.root, text ="-", command = self.dodawanie).grid(row=2,column=3)

        self.root.mainloop()
        pass
    def dodawanie(self):
        pass

if __name__ == "__main__":
    calc = Kalkulator()
    
