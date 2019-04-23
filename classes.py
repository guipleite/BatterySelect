import math
# from chempy import balance_stoichiometry , Equilibrium

class Metal:

    def __init__(self,nome,ered,coef,eletrons,mmolar):
        self.Nome = nome
        self.Ered = ered
        self.Coef = coef
        self.Eletrons = eletrons
        self.MMolar = mmolar


class Solucoes:

    def __init__(self,concetracao):
        self.Concetracao = float(concetracao)
        # self.Ion1 = Ion1
        # self.Ion2 = ion2

class Pilha:

    def __init__(self,metal1,metal2,solucao1,solucao2,temperatura):
        self.Metal1 = metal1
        self.Metal2 = metal2
        self.Solucao1 = solucao1
        self.Solucao2 = solucao2
        self.Temp = int(temperatura) + 273 # C para K


    def catado_anodo(self):
        if(self.Metal1.Ered>self.Metal2.Ered):
            self.catodo = self.Metal1
            self.sol_catodo = self.Solucao1
            self.anodo = self.Metal2
            self.sol_anodo = self.Solucao2
            self.E0 = self.Metal1.Ered - self.Metal2.Ered
        else:
            self.catodo = self.Metal2
            self.sol_catodo = self.Solucao2
            self.anodo = self.Metal1
            self.sol_anodo = self.Solucao1
            self.E0 = self.Metal2.Ered - self.Metal1.Ered

    def coeficientes(self):
        if self.catodo.Eletrons==self.anodo.Eletrons:
            self.coef_catodo = self.catodo.Coef
            self.coef_anodo = self.anodo.Coef
        elif (self.catodo.Eletrons%self.anodo.Eletrons==0):
            self.coef_catodo = self.catodo.Coef
            self.coef_anodo = self.catodo.Eletrons
        elif (self.anodo.Eletrons%self.catodo.Eletrons==0):
            self.coef_anodo = self.anodo.Coef
            self.coef_catodo = self.anodo.Eletrons
        else:
            self.coef_catodo = self.anodo.Eletrons
            self.coef_anodo = self.catodo.Eletrons





    def calcula_ddp(self):

        R = 8.31
        F = 96500
        n = self.anodo.Eletrons + self.catodo.Eletrons # errado

        self.E = self.E0 - ((R*self.Temp)/(n*F)) * math.log( ((self.sol_anodo.Concetracao)**self.coef_anodo )/
                                                   ((self.sol_catodo.Concetracao)**self.coef_catodo ) )


    def calcula_cap_carga(self):
        # capacidade de carga é número de mols de elétrons vezes a
        # carga em coulomb de 1 eletrons(xNumero de avogrado) %3600(As(C) para Ah)
        n = self.anodo.Eletrons + self.catodo.Eletrons
        self.CapCarga = (n*1.6021E-19*6.0225E23)/3600

    def calcula_densidade_energia(self,massa_eletrodo1,massa_eletrodo2):

        Pothora = self.CapCarga * self.E
        # Pothora * 3600 = Joule
        self.DensEnergia = ( (Pothora * 3600) ) / (0.001*(float(massa_eletrodo1)+float(massa_eletrodo2)))






Ferro2 = Metal("Ferro(2+)",-0.44,1,2,56)
Ferro3 = Metal("Ferro(3+)",-0.04,1,3,56)
Cobre = Metal("Cobre",0.34,1,2,63.546)
Cromo = Metal("Cromo",-0.74,1,3,52)
Litio = Metal("Lítio",-3.04,1,1,6.94)
Niquel = Metal("Níquel",-0.23,1,2,58.7)
Chumbo = Metal("Chumbo",-0.13,1,2,207)
Prata = Metal("Prata",0.80,1,1,108)
Cobalto = Metal("Cobalto",-0.28,1,2,59)
Aluminio = Metal("Alumínio",-1.66,1,3,27)

Metais = [Ferro2,Ferro3,Cobre,Cromo,Litio,Niquel,Chumbo,Prata,Cobalto,Aluminio]
