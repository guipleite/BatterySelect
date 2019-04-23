import tkinter as tk
from tkinter import *
from classes import *
import select

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

        listMetal = ['Ferro(2+)','Ferro(3+)','Cobre','Cromo','Lítio','Níquel','Chumbo','Prata','Cobalto','Alumínio'];

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
        pilha = Pilha(metal1,metal2,sol1,sol2,temp)

        pilha.catado_anodo()

        pilha.coeficientes()

        pilha.calcula_ddp()

        pilha.calcula_cap_carga()

        pilha.calcula_densidade_energia(mm1,mm2)

        pilha.calcula_densidade_carga(mm1,mm2)

        potencia_pilha = round(pilha.E * pilha.CapCarga , 2)

        c = tk.Toplevel(self)
        c.geometry('500x500')
        c.wm_title("Pilha criada")

        ##Variaveis que serao mostradas
        ddp = pilha.E0
        esp = pilha.E
        capa = round(pilha.CapCarga , 2)
        densi = pilha.DensEnergia
        densi = round(densi,2)
        densiC = round(pilha.DensCarga,2)

        label_0 = Label(c, text="Pilha Criada",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        label_ddp = Label(c, text="DDP padrão",width=20,font=("bold", 10))
        label_ddp.place(x=20,y=130)
        label_ddp2 = Label(c, text=(ddp,"Volts"),width=30,font=("bold", 10))
        label_ddp2.place(x=180,y=130)

        label_esp = Label(c, text="DDP especifica",width=20,font=("bold", 10))
        label_esp.place(x=20,y=180)
        label_esp2 = Label(c, text=(esp,"Volts"),width=30,font=("bold", 10))
        label_esp2.place(x=180,y=180)

        label_capa = Label(c, text="Capacidade de Carga",width=20,font=("bold", 10))
        label_capa.place(x=20,y=230)
        label_capa2 = Label(c, text=(capa,"mAh"),width=30,font=("bold", 10))
        label_capa2.place(x=180,y=230)

        label_pot = Label(c, text="Potência",width=20,font=("bold", 10))
        label_pot.place(x=20,y=280)
        label_pot2 = Label(c, text=(potencia_pilha,"W"),width=30,font=("bold", 10))
        label_pot2.place(x=180,y=280)

        label_densi = Label(c, text="Densidade de Energia",width=20,font=("bold", 10))
        label_densi.place(x=20,y=330)
        label_densi2 = Label(c, text=(densi,"J/kg"),width=30,font=("bold", 10))
        label_densi2.place(x=180,y=330)

        label_densic = Label(c, text="Densidade de Carga",width=20,font=("bold", 10))
        label_densic.place(x=20,y=380)
        label_densic2 = Label(c, text=(densiC,"Ah/kg"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=380)

    def select_window(self):
        s = tk.Toplevel(self)
        s.geometry('500x500')
        s.wm_title("Selecionar Pilha")

        label_0 = Label(s, text="Selecionar Pilha",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)

        label_ddp = Label(s, text="D.D.P. em Volts desejada",width=30,font=("bold", 10))
        label_ddp.place(x=40,y=130)

        self.entry_ddp = Entry(s)
        self.entry_ddp.place(x=280,y=130)

        label_pot = Label(s, text="Potencia desejada (Watts) ",width=30,font=("bold", 10))
        label_pot.place(x=40,y=180)

        self.entry_pot = Entry(s)
        self.entry_pot.place(x=280,y=180)

        label_cap = Label(s, text="Capacidade de Carga desejada (Ah)",width=30,font=("bold", 10))
        label_cap.place(x=40,y=230)

        self.entry_cap = Entry(s)
        self.entry_cap.place(x=280,y=230)

        label_cons = Label(s, text="Consumo (A) (Se não souber digite -1)",width=30,font=("bold", 10))
        label_cons.place(x=40,y=280)

        self.entry_cons = Entry(s)
        self.entry_cons.place(x=280,y=280)


        label_temp = Label(s, text="Tempo de duracao (Hora)",width=30,font=("bold", 10))
        label_temp.place(x=40,y=330)

        self.entry_temp = Entry(s)
        self.entry_temp.place(x=280,y=330)


        label_temp = Label(s, text="A aplicação exige uma durabilidade maior \ncom altas taxas de carga e descarga?",width=60,font=("bold", 10))
        label_temp.place(x=-100,y=390)
        self.var1 = IntVar()
        C1=Checkbutton(s, variable=self.var1, onvalue = 1, offvalue = 0)
        C1.place(x=330,y=400)

        
        
        Button(s, text='Montar Pilha',width=20,bg='brown',fg='white', command=self.crtd_window1).place(x=180,y=470)

    def crtd_window1(self):
        g = tk.Toplevel(self)
        g.geometry('500x500')
        g.wm_title("Montar Pilha")

        self.ops = select.Seleciona_pilha(float(self.entry_ddp.get()), float(self.entry_pot.get()), float(self.entry_cap.get()), float(self.entry_temp.get()), float(self.entry_cons.get()), self.var1.get())

        label_0 = Label(g, text="Melhores Opções",width=20,font=("bold", 20))
        label_0.place(x=90,y=30)
        
        label_op1 = Label(g, text=self.ops.tresops()[0],width=100,font=("bold", 8))
        label_op1.place(x=-50,y=80)
        Button(g, text='Selecionar',width=20,bg='brown',fg='white', command=self.crtd1).place(x=180,y=190)

        label_op2 = Label(g, text=self.ops.tresops()[1],width=100,font=("bold", 8))
        label_op2.place(x=-50,y=220)
        Button(g, text='Selecionar',width=20,bg='brown',fg='white', command=self.crtd2).place(x=180,y=330)

        label_op3 = Label(g, text=self.ops.tresops()[2],width=100,font=("bold", 8))
        label_op3.place(x=-50,y=360)
        Button(g, text='Selecionar',width=20,bg='brown',fg='white', command=self.crtd3).place(x=180,y=470)

    
    def crtd1(self):
        c = tk.Toplevel(self)
        c.geometry('500x580')
        c.wm_title("Pilhas Selecionadas")
        m=30
        label_0 = Label(c, text="Pilhas Selecionadas",width=20,font=("bold", 20))
        label_0.place(x=90,y=10)

        label_name = Label(c, text=self.ops.selecao1()[9][0],width=25,font=("bold", 13))
        label_name.place(x=90,y=60)

        label_ddp = Label(c, text="Preço Total",width=20,font=("bold", 10))
        label_ddp.place(x=20,y=50+m)
        label_ddp2 = Label(c, text=(self.ops.selecao1()[0][0],"reais"),width=30,font=("bold", 10))
        label_ddp2.place(x=180,y=50+m)

        label_esp = Label(c, text="Número de Pilhas",width=20,font=("bold", 10))
        label_esp.place(x=20,y=70+m)
        label_esp2 = Label(c, text=(self.ops.selecao1()[3][0]),width=30,font=("bold", 10))
        label_esp2.place(x=180,y=70+m)

        label_capa = Label(c, text="Ligações em paralelo",width=20,font=("bold", 10))
        label_capa.place(x=20,y=90+m)
        label_capa2 = Label(c, text=(self.ops.selecao1()[2][0]),width=30,font=("bold", 10))
        label_capa2.place(x=180,y=90+m)

        label_pot = Label(c, text="Ligações em série",width=20,font=("bold", 10))
        label_pot.place(x=20,y=110+m)
        label_pot2 = Label(c, text=(self.ops.selecao1()[1][0]),width=30,font=("bold", 10))
        label_pot2.place(x=180,y=110+m)

        label_densic = Label(c, text="Capacidade de Carga",width=20,font=("bold", 10))
        label_densic.place(x=20,y=130+m)
        label_densic2 = Label(c, text=(self.ops.selecao1()[7][0],"Ah"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=130+m)

        label_densic = Label(c, text="DDP",width=20,font=("bold", 10))
        label_densic.place(x=20,y=150+m)
        label_densic2 = Label(c, text=(self.ops.selecao1()[6][0],"Volts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=150+m)

        label_densic = Label(c, text="Potência",width=20,font=("bold", 10))
        label_densic.place(x=20,y=170+m)
        label_densic2 = Label(c, text=(self.ops.selecao1()[8][0],"Watts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=170+m)

        label_name = Label(c, text=self.ops.selecao1()[9][1],width=30,font=("bold", 13))
        label_name.place(x=90,y=60+m+210+m)

        label_ddp = Label(c, text="Preço Total",width=20,font=("bold", 10))
        label_ddp.place(x=20,y=50+m+m+210+m)
        label_ddp2 = Label(c, text=(self.ops.selecao1()[0][1],"reais"),width=30,font=("bold", 10))
        label_ddp2.place(x=180,y=50+m+m+210+m)

        label_esp = Label(c, text="Número de Pilhas",width=20,font=("bold", 10))
        label_esp.place(x=20,y=70+m+m+210+m)
        label_esp2 = Label(c, text=(self.ops.selecao1()[3][1]),width=30,font=("bold", 10))
        label_esp2.place(x=180,y=70+m+m+210+m)

        label_capa = Label(c, text="Ligações em paralelo",width=20,font=("bold", 10))
        label_capa.place(x=20,y=90+m+m+210+m)
        label_capa2 = Label(c, text=(self.ops.selecao1()[2][1]),width=30,font=("bold", 10))
        label_capa2.place(x=180,y=90+m+m+210+m)

        label_pot = Label(c, text="Ligações em série",width=20,font=("bold", 10))
        label_pot.place(x=20,y=110+m+m+210+m)
        label_pot2 = Label(c, text=(self.ops.selecao1()[1][1]),width=30,font=("bold", 10))
        label_pot2.place(x=180,y=110+m+m+210+m)

        label_densic = Label(c, text="Capacidade de Carga",width=20,font=("bold", 10))
        label_densic.place(x=20,y=130+m+m+210+m)
        label_densic2 = Label(c, text=(self.ops.selecao1()[7][1],"Ah"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=130+m+m+210+m)

        label_densic = Label(c, text="DDP",width=20,font=("bold", 10))
        label_densic.place(x=20,y=150+m+m+210+m)
        label_densic2 = Label(c, text=(self.ops.selecao1()[6][1],"Volts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=150+m+m+210+m)

        label_densic = Label(c, text="Potência",width=20,font=("bold", 10))
        label_densic.place(x=20,y=170+m+m+210+m)
        label_densic2 = Label(c, text=(self.ops.selecao1()[8][1],"Watts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=170+m+m+210+m)

        if float(self.entry_cons.get()) == -1:
            label_densi = Label(c, text="Tempo Ligado",width=20,font=("bold", 10))
            label_densi.place(x=20,y=190+m)
            label_densi2 = Label(c, text=(self.ops.selecao1()[4][0],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m)

            label_densi = Label(c, text="Tempo Ligado",width=20,font=("bold", 10))
            label_densi.place(x=20,y=190+m+m+210+m)
            label_densi2 = Label(c, text=(self.ops.selecao1()[4][1],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m+m+210+m)
        
            label_densic = Label(c, text="Consumo",width=20,font=("bold", 10))
            label_densic.place(x=20,y=210+m+m+210+m)
            label_densic2 = Label(c, text=(self.ops.selecao1()[10][1], "A"),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m+m+210+m)

            label_densic = Label(c, text="Consumo",width=20,font=("bold", 10))
            label_densic.place(x=20,y=210+m)
            label_densic2 = Label(c, text=(self.ops.selecao1()[10][0], "A"),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m)

        else:
            label_densi = Label(c, text="Tempo Até Bateria Esgotar",width=19,font=("bold", 10))
            label_densi.place(x=20,y=190+m)
            label_densi2 = Label(c, text=(self.ops.selecao1()[4][0],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m)

            label_densi = Label(c, text="Tempo Até Bateria Esgotar",width=19,font=("bold", 10))
            label_densi.place(x=20,y=190+m+m+210+m)
            label_densi2 = Label(c, text=(self.ops.selecao1()[4][1],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m+m+210+m)

            label_densic = Label(c, text="Porcentagem da bateria gasta\n no tempo selecionado",width=27,font=("bold", 8))
            label_densic.place(x=20,y=210+m+m+210+m)
            label_densic2 = Label(c, text=(self.ops.selecao1()[5][1]),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m+m+210+m)

            label_densic = Label(c, text="Porcentagem da bateria gasta\n no tempo selecionado",width=27,font=("bold", 8))
            label_densic.place(x=20,y=210+m)
            label_densic2 = Label(c, text=(self.ops.selecao1()[5][0]),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m)
    

    def crtd2(self):
        c = tk.Toplevel(self)
        c.geometry('500x580')
        c.wm_title("Pilhas Selecionadas")
        m=30
        label_0 = Label(c, text="Pilhas Selecionadas",width=20,font=("bold", 20))
        label_0.place(x=90,y=10)

        label_name = Label(c, text=self.ops.selecao2()[9][0],width=25,font=("bold", 13))
        label_name.place(x=90,y=60)

        label_ddp = Label(c, text="Preço Total",width=20,font=("bold", 10))
        label_ddp.place(x=20,y=50+m)
        label_ddp2 = Label(c, text=(self.ops.selecao2()[0][0],"reais"),width=30,font=("bold", 10))
        label_ddp2.place(x=180,y=50+m)

        label_esp = Label(c, text="Número de Pilhas",width=20,font=("bold", 10))
        label_esp.place(x=20,y=70+m)
        label_esp2 = Label(c, text=(self.ops.selecao2()[3][0]),width=30,font=("bold", 10))
        label_esp2.place(x=180,y=70+m)

        label_capa = Label(c, text="Ligações em paralelo",width=20,font=("bold", 10))
        label_capa.place(x=20,y=90+m)
        label_capa2 = Label(c, text=(self.ops.selecao2()[2][0]),width=30,font=("bold", 10))
        label_capa2.place(x=180,y=90+m)

        label_pot = Label(c, text="Ligações em série",width=20,font=("bold", 10))
        label_pot.place(x=20,y=110+m)
        label_pot2 = Label(c, text=(self.ops.selecao2()[1][0]),width=30,font=("bold", 10))
        label_pot2.place(x=180,y=110+m)

        label_densic = Label(c, text="Capacidade de Carga",width=20,font=("bold", 10))
        label_densic.place(x=20,y=130+m)
        label_densic2 = Label(c, text=(self.ops.selecao2()[7][0],"Ah"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=130+m)

        label_densic = Label(c, text="DDP",width=20,font=("bold", 10))
        label_densic.place(x=20,y=150+m)
        label_densic2 = Label(c, text=(self.ops.selecao2()[6][0],"Volts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=150+m)

        label_densic = Label(c, text="Potência",width=20,font=("bold", 10))
        label_densic.place(x=20,y=170+m)
        label_densic2 = Label(c, text=(self.ops.selecao2()[8][0],"Watts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=170+m)

        label_name = Label(c, text=self.ops.selecao2()[9][1],width=25,font=("bold", 13))
        label_name.place(x=90,y=60+m+210+m)

        label_ddp = Label(c, text="Preço Total",width=20,font=("bold", 10))
        label_ddp.place(x=20,y=50+m+m+210+m)
        label_ddp2 = Label(c, text=(self.ops.selecao2()[0][1],"reais"),width=30,font=("bold", 10))
        label_ddp2.place(x=180,y=50+m+m+210+m)

        label_esp = Label(c, text="Número de Pilhas",width=20,font=("bold", 10))
        label_esp.place(x=20,y=70+m+m+210+m)
        label_esp2 = Label(c, text=(self.ops.selecao2()[3][1]),width=30,font=("bold", 10))
        label_esp2.place(x=180,y=70+m+m+210+m)

        label_capa = Label(c, text="Ligações em paralelo",width=20,font=("bold", 10))
        label_capa.place(x=20,y=90+m+m+210+m)
        label_capa2 = Label(c, text=(self.ops.selecao2()[2][1]),width=30,font=("bold", 10))
        label_capa2.place(x=180,y=90+m+m+210+m)

        label_pot = Label(c, text="Ligações em série",width=20,font=("bold", 10))
        label_pot.place(x=20,y=110+m+m+210+m)
        label_pot2 = Label(c, text=(self.ops.selecao2()[1][1]),width=30,font=("bold", 10))
        label_pot2.place(x=180,y=110+m+m+210+m)

        label_densic = Label(c, text="Capacidade de Carga",width=20,font=("bold", 10))
        label_densic.place(x=20,y=130+m+m+210+m)
        label_densic2 = Label(c, text=(self.ops.selecao2()[7][1],"Ah"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=130+m+m+210+m)

        label_densic = Label(c, text="DDP",width=20,font=("bold", 10))
        label_densic.place(x=20,y=150+m+m+210+m)
        label_densic2 = Label(c, text=(self.ops.selecao2()[6][1],"Volts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=150+m+m+210+m)

        label_densic = Label(c, text="Potência",width=20,font=("bold", 10))
        label_densic.place(x=20,y=170+m+m+210+m)
        label_densic2 = Label(c, text=(self.ops.selecao2()[8][1],"Watts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=170+m+m+210+m)

        if float(self.entry_cons.get()) == -1:
            label_densi = Label(c, text="Tempo Ligado",width=20,font=("bold", 10))
            label_densi.place(x=20,y=190+m)
            label_densi2 = Label(c, text=(self.ops.selecao2()[4][0],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m)

            label_densi = Label(c, text="Tempo Ligado",width=20,font=("bold", 10))
            label_densi.place(x=20,y=190+m+m+210+m)
            label_densi2 = Label(c, text=(self.ops.selecao2()[4][1],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m+m+210+m)
        
            label_densic = Label(c, text="Consumo",width=20,font=("bold", 10))
            label_densic.place(x=20,y=210+m+m+210+m)
            label_densic2 = Label(c, text=(self.ops.selecao2()[10][1], "A"),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m+m+210+m)

            label_densic = Label(c, text="Consumo",width=20,font=("bold", 10))
            label_densic.place(x=20,y=210+m)
            label_densic2 = Label(c, text=(self.ops.selecao2()[10][0], "A"),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m)

        else:
            label_densi = Label(c, text="Tempo Até Bateria Esgotar",width=19,font=("bold", 10))
            label_densi.place(x=20,y=190+m)
            label_densi2 = Label(c, text=(self.ops.selecao2()[4][0],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m)

            label_densi = Label(c, text="Tempo Até Bateria Esgotar",width=19,font=("bold", 10))
            label_densi.place(x=20,y=190+m+m+210+m)
            label_densi2 = Label(c, text=(self.ops.selecao2()[4][1],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m+m+210+m)

            label_densic = Label(c, text="Porcentagem da bateria gasta\n no tempo selecionado",width=27,font=("bold", 8))
            label_densic.place(x=20,y=210+m+m+210+m)
            label_densic2 = Label(c, text=(self.ops.selecao2()[5][1]),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m+m+210+m)

            label_densic = Label(c, text="Porcentagem da bateria gasta\n no tempo selecionado",width=27,font=("bold", 8))
            label_densic.place(x=20,y=210+m)
            label_densic2 = Label(c, text=(self.ops.selecao2()[5][0]),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m)

 
    def crtd3(self):
        c = tk.Toplevel(self)
        c.geometry('500x580')
        c.wm_title("Pilhas Selecionadas")
        m=30
        label_0 = Label(c, text="Pilhas Selecionadas",width=20,font=("bold", 20))
        label_0.place(x=90,y=10)

        label_name = Label(c, text=self.ops.selecao3()[9][0],width=25,font=("bold", 13))
        label_name.place(x=90,y=60)

        label_ddp = Label(c, text="Preço Total",width=20,font=("bold", 10))
        label_ddp.place(x=20,y=50+m)
        label_ddp2 = Label(c, text=(self.ops.selecao3()[0][0],"reais"),width=30,font=("bold", 10))
        label_ddp2.place(x=180,y=50+m)

        label_esp = Label(c, text="Número de Pilhas",width=20,font=("bold", 10))
        label_esp.place(x=20,y=70+m)
        label_esp2 = Label(c, text=(self.ops.selecao3()[3][0]),width=30,font=("bold", 10))
        label_esp2.place(x=180,y=70+m)

        label_capa = Label(c, text="Ligações em paralelo",width=20,font=("bold", 10))
        label_capa.place(x=20,y=90+m)
        label_capa2 = Label(c, text=(self.ops.selecao3()[2][0]),width=30,font=("bold", 10))
        label_capa2.place(x=180,y=90+m)

        label_pot = Label(c, text="Ligações em série",width=20,font=("bold", 10))
        label_pot.place(x=20,y=110+m)
        label_pot2 = Label(c, text=(self.ops.selecao3()[1][0]),width=30,font=("bold", 10))
        label_pot2.place(x=180,y=110+m)

        label_densic = Label(c, text="Capacidade de Carga",width=20,font=("bold", 10))
        label_densic.place(x=20,y=130+m)
        label_densic2 = Label(c, text=(self.ops.selecao3()[7][0],"Ah"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=130+m)

        label_densic = Label(c, text="DDP",width=20,font=("bold", 10))
        label_densic.place(x=20,y=150+m)
        label_densic2 = Label(c, text=(self.ops.selecao3()[6][0],"Volts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=150+m)

        label_densic = Label(c, text="Potência",width=20,font=("bold", 10))
        label_densic.place(x=20,y=170+m)
        label_densic2 = Label(c, text=(self.ops.selecao3()[8][0],"Watts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=170+m)


        label_name = Label(c, text=self.ops.selecao3()[9][1],width=30,font=("bold", 13))
        label_name.place(x=90,y=60+m+210+m)

        label_ddp = Label(c, text="Preço Total",width=20,font=("bold", 10))
        label_ddp.place(x=20,y=50+m+m+210+m)
        label_ddp2 = Label(c, text=(self.ops.selecao3()[0][1],"reais"),width=30,font=("bold", 10))
        label_ddp2.place(x=180,y=50+m+m+210+m)

        label_esp = Label(c, text="Número de Pilhas",width=20,font=("bold", 10))
        label_esp.place(x=20,y=70+m+m+210+m)
        label_esp2 = Label(c, text=(self.ops.selecao3()[3][1]),width=30,font=("bold", 10))
        label_esp2.place(x=180,y=70+m+m+210+m)

        label_capa = Label(c, text="Ligações em paralelo",width=20,font=("bold", 10))
        label_capa.place(x=20,y=90+m+m+210+m)
        label_capa2 = Label(c, text=(self.ops.selecao3()[2][1]),width=30,font=("bold", 10))
        label_capa2.place(x=180,y=90+m+m+210+m)

        label_pot = Label(c, text="Ligações em série",width=20,font=("bold", 10))
        label_pot.place(x=20,y=110+m+m+210+m)
        label_pot2 = Label(c, text=(self.ops.selecao3()[1][1]),width=30,font=("bold", 10))
        label_pot2.place(x=180,y=110+m+m+210+m)

        label_densic = Label(c, text="Capacidade de Carga",width=20,font=("bold", 10))
        label_densic.place(x=20,y=130+m+m+210+m)
        label_densic2 = Label(c, text=(self.ops.selecao3()[7][1],"Ah"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=130+m+m+210+m)

        label_densic = Label(c, text="DDP",width=20,font=("bold", 10))
        label_densic.place(x=20,y=150+m+m+210+m)
        label_densic2 = Label(c, text=(self.ops.selecao3()[6][1],"Volts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=150+m+m+210+m)

        label_densic = Label(c, text="Potência",width=20,font=("bold", 10))
        label_densic.place(x=20,y=170+m+m+210+m)
        label_densic2 = Label(c, text=(self.ops.selecao3()[8][1],"Watts"),width=30,font=("bold", 10))
        label_densic2.place(x=180,y=170+m+m+210+m)

        if float(self.entry_cons.get()) == -1:
            label_densi = Label(c, text="Tempo Ligado",width=20,font=("bold", 10))
            label_densi.place(x=20,y=190+m)
            label_densi2 = Label(c, text=(self.ops.selecao3()[4][0],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m)

            label_densi = Label(c, text="Tempo Ligado",width=20,font=("bold", 10))
            label_densi.place(x=20,y=190+m+m+210+m)
            label_densi2 = Label(c, text=(self.ops.selecao3()[4][1],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m+m+210+m)
        
            label_densic = Label(c, text="Consumo",width=20,font=("bold", 10))
            label_densic.place(x=20,y=210+m+m+210+m)
            label_densic2 = Label(c, text=(self.ops.selecao3()[10][1], "A"),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m+m+210+m)

            label_densic = Label(c, text="Consumo",width=20,font=("bold", 10))
            label_densic.place(x=20,y=210+m)
            label_densic2 = Label(c, text=(self.ops.selecao3()[10][0], "A"),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m)

        else:
            label_densi = Label(c, text="Tempo Até Bateria Esgotar",width=19,font=("bold", 10))
            label_densi.place(x=20,y=190+m)
            label_densi2 = Label(c, text=(self.ops.selecao3()[4][0],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m)

            label_densi = Label(c, text="Tempo Até Bateria Esgotar",width=19,font=("bold", 10))
            label_densi.place(x=20,y=190+m+m+210+m)
            label_densi2 = Label(c, text=(self.ops.selecao3()[4][1],"hora(s)"),width=30,font=("bold", 10))
            label_densi2.place(x=180,y=190+m+m+210+m)

            label_densic = Label(c, text="Porcentagem da bateria gasta\n no tempo selecionado",width=27,font=("bold", 8))
            label_densic.place(x=20,y=210+m+m+210+m)
            label_densic2 = Label(c, text=(self.ops.selecao3()[5][1]),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m+m+210+m)

            label_densic = Label(c, text="Porcentagem da bateria gasta\n no tempo selecionado",width=27,font=("bold", 8))
            label_densic.place(x=20,y=210+m)
            label_densic2 = Label(c, text=(self.ops.selecao3()[5][0]),width=30,font=("bold", 10))
            label_densic2.place(x=180,y=210+m)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Catalogo de Pilhas")
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
