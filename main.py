import tkinter as tk
from tkinter import *
from classes import *

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Montar Pilha", width=15,bg='brown',fg='white',
                                command=self.create_window)
        self.button.place(x=200,y=130)
        self.button = tk.Button(self, text="Selecionar Pilha", width=15,bg='brown',fg='white',
                                command=self.select_window)
        self.button.place(x=200,y=230)


    def create_window(self):
        t = tk.Toplevel(self)
        t.geometry('500x500')
        t.wm_title("Montar Pilha")

        listMetal = ['Ferro(2+)','Ferro(3+)','Cobre','Cromo','Lítio','Níquel','Chumbo','Prata','Cobalto','Zinco'];

        label_0 = Label(t, text="Montar Pilha",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        self.met1=StringVar()
        droplist=OptionMenu(t,self.met1, *listMetal)
        droplist.config(width=15)
        self.met1.set('Metal 1')
        droplist.place(x=192,y=130)

        self.met2 = StringVar()
        droplist=OptionMenu(t,self.met2, *listMetal)
        droplist.config(width=15)
        self.met2.set('Metal 2')
        droplist.place(x=192,y=180)

        label_1 = Label(t, text="Concentração da Solução do metal 1 em mol/L",width=37,font=("bold", 9))
        label_1.place(x=20,y=230)

        self.entry_1 = Entry(t)
        self.entry_1.place(x=280,y=230)

        label_2 = Label(t, text="Concentração da Solução do metal 2 em mol/L",width=37,font=("bold", 9))
        label_2.place(x=20,y=280)

        self.entry_2 = Entry(t)
        self.entry_2.place(x=280,y=280)


        label_3 = Label(t, text="Temperatura em graus Celcius",width=30,font=("bold", 10))
        label_3.place(x=40,y=330)

        self.entry_3 = Entry(t)
        self.entry_3.place(x=280,y=330)

        label_4 = Label(t, text="Massa do Metal 1 em g",width=30,font=("bold", 10))
        label_4.place(x=40,y=380)

        self.entry_4 = Entry(t)
        self.entry_4.place(x=280,y=380)

        label_5 = Label(t, text="Massa do Metal 2 em g",width=30,font=("bold", 10))
        label_5.place(x=40,y=430)

        self.entry_5 = Entry(t)
        self.entry_5.place(x=280,y=430)


        Button(t, text='Montar Pilha',width=20,bg='brown',fg='white',command=self.crtd_window).place(x=180,y=470)

    def crtd_window(self):
    	## Referencia as entradas da tela anterior
        temp = self.entry_3.get()
        c2 = self.entry_2.get()
        c1 = self.entry_1.get()
        m1 = self.met1.get()
        m2 = self.met2.get()
        mm1 = self.entry_4.get()
        mm2 = self.entry_5.get()

        for metal in Metais:
            if (m1 == metal.Nome):
                metal1 = metal
            if (m2 == metal.Nome):
                metal2 = metal

        sol1 = Solucoes(c1)
        sol2 = Solucoes(c2)
        pilha = Pilha(metal1,metal2,mm1,mm2,sol1,sol2,temp)

        pilha.catado_anodo()

        pilha.coeficientes()

        pilha.calcula_ddp()

        pilha.calcula_cap_carga()

        pilha.calcula_densidade_carga()

        pilha.calcula_densidade_energia()

        pilha.calcula_custo()


        potencia_pilha = round(pilha.E * pilha.CapCarga , 2)

        c = tk.Toplevel(self)
        c.geometry('500x600')
        c.wm_title("Pilha criada")

        ##Variaveis que serao mostradas
        concentracao_a_ser_usada1 = "cloreto de " + metal1.Nome
        concentracao_a_ser_usada2 = "cloreto de " + metal2.Nome

        ddp = pilha.E0
        esp = pilha.E
        capa = round(pilha.CapCarga , 4)
        densiC = round(pilha.DensCarga,4)
        densi = round(pilha.DensEnergia,4)
        preco = round(pilha.pfinal,2)




        label_0 = Label(c, text="Pilha Criada",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        label_sol1 = Label(c, text="Solução metal 1:",width=20,font=("bold", 10))
        label_sol1.place(x=20,y=130)
        label_sol12 = Label(c, text=concentracao_a_ser_usada1,width=30,font=("bold", 10))
        label_sol12.place(x=180,y=130)

        label_sol2 = Label(c, text="Solução metal 2:",width=20,font=("bold", 10))
        label_sol2.place(x=20,y=150)
        label_sol22 = Label(c, text=concentracao_a_ser_usada2,width=30,font=("bold", 10))
        label_sol22.place(x=180,y=150)

        label_ddp = Label(c, text="DDP padrão",width=20,font=("bold", 10))
        label_ddp.place(x=20,y=180)
        label_ddp2 = Label(c, text=(ddp,"Volts"),width=30,font=("bold", 10))
        label_ddp2.place(x=180,y=180)

        label_esp = Label(c, text="DDP especifica",width=20,font=("bold", 10))
        label_esp.place(x=20,y=230)
        label_esp2 = Label(c, text=(esp,"Volts"),width=30,font=("bold", 10))
        label_esp2.place(x=180,y=230)

        label_capa = Label(c, text="Capacidade de Carga",width=20,font=("bold", 10))
        label_capa.place(x=20,y=280)
        label_capa2 = Label(c, text=(capa,"Ah"),width=30,font=("bold", 10))
        label_capa2.place(x=180,y=280)

        label_pot = Label(c, text="Potência",width=20,font=("bold", 10))
        label_pot.place(x=20,y=330)
        label_pot2 = Label(c, text=(potencia_pilha,"Wh"),width=30,font=("bold", 10))
        label_pot2.place(x=180,y=330)

        label_densi = Label(c, text="Densidade de Energia",width=20,font=("bold", 10))
        label_densi.place(x=20,y=380)
        label_densi2 = Label(c, text=(densi,"J/kg"),width=30,font=("bold", 10))
        label_densi2.place(x=180,y=380)

        label_densic = Label(c, text="Densidade de Carga",width=20,font=("bold", 10))
        label_densic.place(x=20,y=430)
        label_densic2 = Label(c, text=(densiC,"Ah/kg"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=430)

        label_densic = Label(c, text="Preço total da pilha",width=20,font=("bold", 10))
        label_densic.place(x=20,y=480)
        label_densic2 = Label(c, text=("R$",preco),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=480)

    def select_window(self):
        s = tk.Toplevel(self)
        s.geometry('500x500')
        s.wm_title("Selecionar Pilha")

        label_0 = Label(s, text="Selecionar Pilha",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        label_ddp = Label(s, text="D.D.P. em Volts desejada",width=30,font=("bold", 10))
        label_ddp.place(x=40,y=130)

        entry_ddp = Entry(s)
        entry_ddp.place(x=280,y=130)

        label_pot = Label(s, text="Potência desejada ",width=30,font=("bold", 10))
        label_pot.place(x=40,y=180)

        entry_pot = Entry(s)
        entry_pot.place(x=280,y=180)

        label_cap = Label(s, text="Capacidade de Carga desejada",width=30,font=("bold", 10))
        label_cap.place(x=40,y=230)

        entry_cap = Entry(s)
        entry_cap.place(x=280,y=230)

        label_temp = Label(s, text="Tempo de duração",width=30,font=("bold", 10))
        label_temp.place(x=40,y=280)

        entry_temp = Entry(s)
        entry_temp.place(x=280,y=280)

        Button(s, text='Procurar Pilha',width=20,bg='brown',fg='white',command=self.found_window).place(x=180,y=470)

    def found_window(self):
        s = tk.Toplevel(self)
        s.geometry('500x500')
        s.wm_title("Selecionar Pilha")

        ddp = self.entry_ddp.get()
        pot = self.entry_pot.get()
        cap = self.entry_cap.get()
        time = self.entry_temp.get()

        Button(s, text='Procurar Pilha',width=20,bg='brown',fg='white',command=self.final_window).place(x=180,y=470)


    def final_window(self):

        ddp = self.entry_ddp.get()
        pot = self.entry_pot.get()
        cap = self.entry_cap.get()
        time = self.entry_temp.get()

        s = tk.Toplevel(self)
        s.geometry('500x500')
        s.wm_title("Pilha Final")

        label_0 = Label(s, text=("Pilha Final",preco),width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        label_ddp = Label(s, text="Preço",width=30,font=("bold", 10))
        label_ddp.place(x=40,y=130)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Catalogo de Pilhas")
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
