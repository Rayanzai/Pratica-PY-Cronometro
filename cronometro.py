from tkinter import *
import sys
import time
global count
count = 0

class Cronometro():

    def comecar(self): #função de começar a contagem
        global count
        count = 0 
        self.timer()
    
    def parar(self): #função de parar 
        global count
        count = 1
    
    def resetar(self): #função de zerar a contagem
        global count
        count = 1
        self.t.set("00:00:00")

    def fechar(self): #Usado pra fechar a janela do cronômetro
        self.root.destroy()

    def timer(self): #função lógica do cronômetro
        global count
        if count == 0:
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)

            if s < 59:
                s += 1
            elif s == 59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    m = 0
                    h += 1
            
            if h < 10:
                h = str(0) + str(h) 
            else:
                h = str(h)
            if m < 10:
                m = str(0) + str(m)
            else: 
                m = str(m)
            if s < 10:
                s = str(0) + str(s)
            else:
                s = str(s)

            self.d = h + ":" + m + ":" + s  #concatenação
            self.t.set(self.d)

            if count == 0:
                self.root.after(1000, self.timer) #A cada 1 segundo ele atualiza e roda a função lógica de novo.


    def __init__(self):
        self.root = Tk() #Abre janela
        self.root.title("Cronômetro") #titulo janela
        self.root.geometry("700x300") #Tamanho Janela
        self.t = StringVar()
        self.t.set("00:00:00")

        self.lb = Label(self.root, textvariable= self.t, font=("Times 70"), background="lightgrey", borderwidth= 1, relief="solid", padx=20)
        self.button1 = Button(self.root, text="Começar", command=self.comecar, font=("Times 12"), background=("red"))
        self.button2 = Button(self.root, text="Pausar", command=self.parar, font=("Times 12"), background=("red"))
        self.button3 = Button(self.root, text="Recomeçar", command=self.resetar, font=("Times 12"), background=("red"))
        self.button4 = Button(self.root, text="Fechar", command=self.fechar, font=("Times 12"), background=("red"))

        self.lb.place(x = 180, y = 40)
        self.button1.place(x = 190, y = 160)
        self.button2.place(x = 290, y = 160)
        self.button3.place(x = 380, y = 160)
        self.button4.place(x = 490, y = 160)
        self.label = Label(self.root, text="", font=("Times 40"))
        self.root.configure(background="lightgrey")
        self.root.mainloop()

cronometro = Cronometro()
