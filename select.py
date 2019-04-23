import math 

class Seleciona_pilha:
	
	#opcao 1 - Niquel-Cadmio
	#opcao 2 - Ni-Mh
	#opcao 3 - Alcalina
	#opcao 4 - Chumbo
	#opcao 5 - Litio
	
	def __init__(self, ddp, pot, cc, duracao, cons, var):
		self.ddp = ddp
		self.pot = pot
		self.cc = cc
		self.duracao = duracao
		self.cons = cons
		self.var = var
		self.o1 = 0.005
		self.o2 = 0.002
		self.o3 = 0.001
		self.o4 = 0.004
		self.o5 = 0.003
		
    
	def soma(self, a, b, c, d, e):
		self.o1 += a
		self.o2 += b
		self.o3 += c
		self.o4 += d
		self.o5 += e
		self.lista = [self.o1,self.o2,self.o3,self.o4,self.o5]
		self.lista.sort(reverse = True)

	
	def filtragem_inicial(self):
		if self.ddp < 6:
			self.soma(1,1,1,0,1)
		if self.ddp >= 6:
			self.soma(1,1,1,1,1)
		if self.pot < 7.8:
			self.soma(1,1,1,0,1)
		if self.pot >= 7.8:
			self.soma(1,1,0,1,1)
		if self.cc <= 0.045:
			self.soma(0,0,1,0,1)
		if self.cc > 0.045 and self.cc <= 8:
			self.soma(1,1,1,1,1)
		if self.cc > 8:
			self.soma(1,1,0,1,1)
		if self.pot > 8 and self.ddp >= 12:
			self.soma(0,0,0,1,0)
		if self.cc >= 1.3 and self.ddp >= 12:
			self.soma(0,0,0,1,0)
		if self.ddp <= 3.7 and self.cc > 1:
			self.soma(1,1,1,0,0)
		if self.ddp >= 9 and self.cc <= 0.32:
			self.soma(0,0,1,0,0)
		if self.var == 1:
			self.soma(0.5,1,0,0,1)
		if self.var == 0:
			self.soma(0,1,1,1,0)

		

	
	def tresops(self):
		
		self.filtragem_inicial()
		self.a = "NÍQUEL CÁDMIO (NiCd)\n\n- Vida longa com média de 1000 ciclos de carga de descarga perdendo sua capacidade com o tempo.\n - Necessidade de descarte próprio, contém material tóxico em sua composição.\n- Efeito memória menor que NiCd, mas existente.\n - Perde performance com variações de temperatura no ambiente.\n - Custo baixo." 
		self.b = "NÍQUEL HIDRETO METÁLICO (NiMH)\n\n- Vida menor que a NiCd com média de 500 ciclos de carga e descarga, porém capacidade maior.\n - Menos nociva para o meio ambiente.\n- Mais cara que a NiCd."
		self.c = "BATERIAS ALCALINAS\n\n- Custo baixo e alta facilidade para encontrar.\n- Durabilidade e potência alta em relação ao peso.\n- Geralmente não recarregável."
		self.d = "BATERIAS DE CHUMBO (seladas)\n\n- Não lida bem com descargas totais, e não pode ser armazenada sem carga.\n- Grande durabilidade, resistência e custo baixo.\n- Altamente tóxica ao meio ambiente."
		self.e = "BATERIAS DE LÍTIO\n\n- Armazena em média o dobro da energia de uma NiMH e o triplo de uma NiCd.\n- Dura aproximadamente de 300 a 800 cilos de carga e descarga, tendo vantagem de não viciar.\n- Custo elevado. "
		
	
		self.dic = {
			self.lista.index(self.o1):self.a,
			self.lista.index(self.o2):self.b,
			self.lista.index(self.o3):self.c,
			self.lista.index(self.o4):self.d,
			self.lista.index(self.o5):self.e
		}

		return self.dic[0], self.dic[1], self.dic[2]


	def selecao1(self):
		self.tresops()
		if self.dic[0] == self.a:
			#NiCd C 1.2V - 2.5Ah   || #NiCd AAA 1.2V - 0.150Ah
			nome = ["NiCd Tamanho C 1.2V - 2.5Ah", "NiCd Tamanho AAA 1.2V - 0.150Ah"]
			ddp = [1.2, 1.2]
			cc = [round(2.5,2), round(0.15,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 1.2
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 2.5
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				cc[0] += 2.5
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 0.15
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://produto.mercadolivre.com.br/MLB-717208180-bateria-c-2500mah-ni-cd-12v-energy-power-_JM?quantity=1
			preco = [round(n[0]*18.50,2),round(n[0]*25.0,2)]
			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome
		
		elif self.dic[0] == self.b:
			#NiMH C 1.2V - 4Ah  || #NiMH AAA 1.2V - 1.1Ah
			nome = ["NiMH Tamanho C 1.2V - 4Ah", "NiMH Tamanho AAA 1.2V - 1.1Ah"]
			ddp = [1.2, 1.2]
			cc = [round(4.0,2), round(1.1,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 1.2
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 4
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 1.2
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 1.1
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://produto.mercadolivre.com.br/MLB-714808856-bateria-media-c-4000mah-12v-cartela-com-02-_JM?quantity=1
			preco = [round(n[0]*37.0,2),round(n[0]*7.2,2)]
			#https://pt.aliexpress.com/item/Sofirn-4-pcs-Aaa-1100-mAh-NiMh-Recarreg-veis-Baterias-1-2-V-3A-C-lula/32879872149.html?albbt=Google_7_shopping&isdl=y&slnk=&albslr=231501123&src=google&acnt=494-037-6276&aff_platform=google&crea=pt32879872149&netw=u&plac=&albcp=1626568036&mtctp=&aff_short_key=UneMJZVf&gclid=CjwKCAjw7_rlBRBaEiwAc23rhmzndpV_79deJCIUZcMm9T2Lsh_Ks2LooAsqtUPdHIj4-7vxynHqwhoCkfQQAvD_BwE&albag=65942329430&albch=shopping&albagn=888888&trgt=296904914040&device=c&gclsrc=aw.ds			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome

		elif self.dic[0] == self.c:
			#Alcalina 9V - 0.32Ah  || #Alcalina 12V - 0.052Ah
			nome = ["Bateria Alcalina 9V - 0.32Ah", "Bateria Alcalina 12V - 0.052Ah"]
			ddp = [9, 12]
			cc = [round(0.32,2), round(0.052,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 9
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 0.32
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 9
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 0.052
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://www.americanas.com.br/produto/62865101/bateria-alcalina-duracell-9v-original?WT.srch=1&acc=e789ea56094489dffd798f86ff51c7a9&epar=bp_pl_00_go_cf_todas_geral_gmv&gclid=CjwKCAjwzPXlBRAjEiwAj_XTERsYzPIRwOC8ocaA4XPgJ-olkC6I3ZUQna-9soWLXxlS0GXhatDMIBoC-6oQAvD_BwE&i=596ed215eec3dfb1f8cca386&o=5cab93d16c28a3cb509d3e00&opn=YSMESP&sellerId=7661688000108
			preco = [round(n[0]*12.81,2),round(n[0]*10.50,2)]
			#https://www.zxcontato.com.br/item/68-matriz?parceiro=5941&gclid=CjwKCAjw7_rlBRBaEiwAc23rhjP29Q5CW_o0RzLBUtbh1d_EwBMhEoxL1otd07g6NB33R3obljtKTRoCus4QAvD_BwE			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome

		elif self.dic[0] == self.d:
			#Chumbo 6V - 1.3Ah  || #Chumbo 12V - 1.3Ah
			nome = ["Bateria de Chumbo 6V - 1.3Ah", "Bateria de Chumbo 12V - 1.3Ah"]
			ddp = [6, 12]
			cc = [round(1.3,2), round(1.3,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 6
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 1.3
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 6
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 1.3
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://www.americanas.com.br/produto/51985356/bateria-selada-ep-6v-1-3ah?WT.srch=1&acc=e789ea56094489dffd798f86ff51c7a9&epar=bp_pl_00_go_inf-aces_acessorios_geral_gmv_a&gclid=CjwKCAjwzPXlBRAjEiwAj_XTEeMzekB42mEmdpI2eF-gU1ErmSWkrGNuaoswAp04s3C8ND9RlhXu4RoCVuYQAvD_BwE&i=5bdd11aeeec3dfb1f89a257c&o=5c5b2cfd6c28a3cb50631013&opn=YSMESP&sellerId=26164580000146
			preco = [round(n[0]*38.30,2),round(n[0]*55.90,2)]
			#https://www.eletronicasantana.com.br/bateria-selada-vrla-12v-13ah-f187-up1213-rt-06c001-unipower/p?idsku=9002755&utm_source=google_shoppping&utm_medium=cpc&gclid=CjwKCAjw7_rlBRBaEiwAc23rhoCkiE4nXZBYAvz8g9InC9qTIwvTlOpA8xPuTYfi-E8yG4V8svsW9xoCN60QAvD_BwE
			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome
			
		elif self.dic[0] == self.e:
			#Litio Polimer 3.7V - 1.8Ah  || #Litio Ion 3.7 - 2.2Ah
			nome = ["Li-Polymer 3.7V - 1.8Ah", "Li-Ion 3.7V - 2.2Ah"]
			ddp = [3.7, 3.7]
			cc = [round(1.8,2), round(2.2,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 3.7
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 1.8
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 3.7
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 3.7
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 2.2
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 3.7
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://pt.aliexpress.com/item/3-7-V-1800-mAh-102560-c-lulas-Li-Po-Bateria-de-i-es-de-l/32834397284.html?spm=a2g03.search0306.3.7.361917bdNKS5tX&ws_ab_test=searchweb0_0%2Csearchweb201602_0_10084_10083_10547_10887_10307_321_453_10548_322_454_10618_536_10065_317_537_10068_319_10059_10103_10884_10696%2Csearchweb201603_0%2CppcSwitch_0&algo_pvid=bfedf084-8128-4d0d-8581-125e33114f36&algo_expid=bfedf084-8128-4d0d-8581-125e33114f36-3
			preco = [round(n[0]*29.21,2),round(n[0]*52.11,2)]
			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome


	def selecao2(self):
		self.tresops()
		if self.dic[1] == self.a:
			#NiCd C 1.2V - 2.5Ah   || #NiCd AAA 1.2V - 0.150Ah
			nome = ["NiCd Tamanho C 1.2V - 2.5Ah", "NiCd Tamanho AAA 1.2V - 0.150Ah"]
			ddp = [1.2, 1.2]
			cc = [round(2.5,2), round(0.15,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 1.2
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 2.5
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				cc[0] += 2.5
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 0.15
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://produto.mercadolivre.com.br/MLB-717208180-bateria-c-2500mah-ni-cd-12v-energy-power-_JM?quantity=1
			preco = [round(n[0]*18.50,2),round(n[0]*25.0,2)]
			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome
		
		elif self.dic[1] == self.b:
			#NiMH C 1.2V - 4Ah  || #NiMH AAA 1.2V - 1.1Ah
			nome = ["NiMH Tamanho C 1.2V - 4Ah", "NiMH Tamanho AAA 1.2V - 1.1Ah"]
			ddp = [1.2, 1.2]
			cc = [round(4.0,2), round(1.1,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 1.2
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 4
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 1.2
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 1.1
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://produto.mercadolivre.com.br/MLB-1208575234-pilha-bateria-rontek-12v-4000mah-ni-mh-tamanho-c-unidade-_JM?quantity=1
			preco = [round(n[0]*37.0,2),round(n[0]*7.2,2)]
			#https://pt.aliexpress.com/item/Sofirn-4-pcs-Aaa-1100-mAh-NiMh-Recarreg-veis-Baterias-1-2-V-3A-C-lula/32879872149.html?albbt=Google_7_shopping&isdl=y&slnk=&albslr=231501123&src=google&acnt=494-037-6276&aff_platform=google&crea=pt32879872149&netw=u&plac=&albcp=1626568036&mtctp=&aff_short_key=UneMJZVf&gclid=CjwKCAjw7_rlBRBaEiwAc23rhmzndpV_79deJCIUZcMm9T2Lsh_Ks2LooAsqtUPdHIj4-7vxynHqwhoCkfQQAvD_BwE&albag=65942329430&albch=shopping&albagn=888888&trgt=296904914040&device=c&gclsrc=aw.ds			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome

		elif self.dic[1] == self.c:
			#Alcalina 9V - 0.32Ah  || #Alcalina 12V - 0.052Ah
			nome = ["Bateria Alcalina 9V - 0.32Ah", "Bateria Alcalina 12V - 0.052Ah"]
			ddp = [9, 12]
			cc = [round(0.32,2), round(0.052,3)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 9
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 0.32
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 9
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 0.052
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://www.americanas.com.br/produto/62865101/bateria-alcalina-duracell-9v-original?WT.srch=1&acc=e789ea56094489dffd798f86ff51c7a9&epar=bp_pl_00_go_cf_todas_geral_gmv&gclid=CjwKCAjwzPXlBRAjEiwAj_XTERsYzPIRwOC8ocaA4XPgJ-olkC6I3ZUQna-9soWLXxlS0GXhatDMIBoC-6oQAvD_BwE&i=596ed215eec3dfb1f8cca386&o=5cab93d16c28a3cb509d3e00&opn=YSMESP&sellerId=7661688000108
			preco = [round(n[0]*12.81,2),round(n[0]*10.50,2)]
			#https://www.zxcontato.com.br/item/68-matriz?parceiro=5941&gclid=CjwKCAjw7_rlBRBaEiwAc23rhjP29Q5CW_o0RzLBUtbh1d_EwBMhEoxL1otd07g6NB33R3obljtKTRoCus4QAvD_BwE			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome

		elif self.dic[1] == self.d:
			#Chumbo 6V - 1.3Ah  || #Chumbo 12V - 1.3Ah
			nome = ["Bateria de Chumbo 6V - 1.3Ah", "Bateria de Chumbo 12V - 1.3Ah"]
			ddp = [6, 12]
			cc = [round(1.3,2), round(1.3,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 6
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 1.3
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 6
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 1.3
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://www.americanas.com.br/produto/51985356/bateria-selada-ep-6v-1-3ah?WT.srch=1&acc=e789ea56094489dffd798f86ff51c7a9&epar=bp_pl_00_go_inf-aces_acessorios_geral_gmv_a&gclid=CjwKCAjwzPXlBRAjEiwAj_XTEeMzekB42mEmdpI2eF-gU1ErmSWkrGNuaoswAp04s3C8ND9RlhXu4RoCVuYQAvD_BwE&i=5bdd11aeeec3dfb1f89a257c&o=5c5b2cfd6c28a3cb50631013&opn=YSMESP&sellerId=26164580000146
			preco = [round(n[0]*38.30,2),round(n[0]*55.90,2)]
			#https://www.eletronicasantana.com.br/bateria-selada-vrla-12v-13ah-f187-up1213-rt-06c001-unipower/p?idsku=9002755&utm_source=google_shoppping&utm_medium=cpc&gclid=CjwKCAjw7_rlBRBaEiwAc23rhoCkiE4nXZBYAvz8g9InC9qTIwvTlOpA8xPuTYfi-E8yG4V8svsW9xoCN60QAvD_BwE
			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome
			
		elif self.dic[1] == self.e:
			#Litio Polimer 3.7V - 1.8Ah  || #Litio Ion 3.7 - 2.2Ah
			nome = ["Li-Polymer 3.7V - 1.8Ah", "Li-Ion 3.7V - 2.2Ah"]
			ddp = [3.7, 3.7]
			cc = [round(1.8,2), round(2.2,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 3.7
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 1.8
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 3.7
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 3.7
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 2.2
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 3.7
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://pt.aliexpress.com/item/3-7-V-1800-mAh-102560-c-lulas-Li-Po-Bateria-de-i-es-de-l/32834397284.html?spm=a2g03.search0306.3.7.361917bdNKS5tX&ws_ab_test=searchweb0_0%2Csearchweb201602_0_10084_10083_10547_10887_10307_321_453_10548_322_454_10618_536_10065_317_537_10068_319_10059_10103_10884_10696%2Csearchweb201603_0%2CppcSwitch_0&algo_pvid=bfedf084-8128-4d0d-8581-125e33114f36&algo_expid=bfedf084-8128-4d0d-8581-125e33114f36-3
			preco = [round(n[0]*29.21,2),round(n[0]*52.11,2)]
			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome

	def selecao3(self):
		self.tresops()
		if self.dic[2] == self.a:
			#NiCd C 1.2V - 2.5Ah   || #NiCd AAA 1.2V - 0.150Ah
			nome = ["NiCd Tamanho C 1.2V - 2.5Ah", "NiCd Tamanho AAA 1.2V - 0.150Ah"]
			ddp = [1.2, 1.2]
			cc = [round(2.5,2), round(0.15,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 1.2
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 2.5
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				cc[0] += 2.5
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 0.15
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://produto.mercadolivre.com.br/MLB-717208180-bateria-c-2500mah-ni-cd-12v-energy-power-_JM?quantity=1
			preco = [round(n[0]*18.50,2),round(n[0]*25.0,2)]
			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome
		
		elif self.dic[2] == self.b:
			#NiMH C 1.2V - 4Ah  || #NiMH AAA 1.2V - 1.1Ah
			nome = ["NiMH Tamanho C 1.2V - 4Ah", "NiMH Tamanho AAA 1.2V - 1.1Ah"]
			ddp = [1.2, 1.2]
			cc = [round(4.0,2), round(1.1,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 1.2
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 4
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 1.2
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 1.1
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 1.2
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://produto.mercadolivre.com.br/MLB-1208575234-pilha-bateria-rontek-12v-4000mah-ni-mh-tamanho-c-unidade-_JM?quantity=1
			preco = [round(n[0]*37.0,2),round(n[0]*7.2,2)]
			#https://pt.aliexpress.com/item/Sofirn-4-pcs-Aaa-1100-mAh-NiMh-Recarreg-veis-Baterias-1-2-V-3A-C-lula/32879872149.html?albbt=Google_7_shopping&isdl=y&slnk=&albslr=231501123&src=google&acnt=494-037-6276&aff_platform=google&crea=pt32879872149&netw=u&plac=&albcp=1626568036&mtctp=&aff_short_key=UneMJZVf&gclid=CjwKCAjw7_rlBRBaEiwAc23rhmzndpV_79deJCIUZcMm9T2Lsh_Ks2LooAsqtUPdHIj4-7vxynHqwhoCkfQQAvD_BwE&albag=65942329430&albch=shopping&albagn=888888&trgt=296904914040&device=c&gclsrc=aw.ds			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome

		elif self.dic[2] == self.c:
			#Alcalina 9V - 0.32Ah  || #Alcalina 12V - 0.052Ah
			nome = ["Bateria Alcalina 9V - 0.32Ah", "Bateria Alcalina 12V - 0.052Ah"]
			ddp = [9, 12]
			cc = [round(0.32,2), round(0.052,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 9
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 0.32
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 9
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 0.052
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://www.americanas.com.br/produto/62865101/bateria-alcalina-duracell-9v-original?WT.srch=1&acc=e789ea56094489dffd798f86ff51c7a9&epar=bp_pl_00_go_cf_todas_geral_gmv&gclid=CjwKCAjwzPXlBRAjEiwAj_XTERsYzPIRwOC8ocaA4XPgJ-olkC6I3ZUQna-9soWLXxlS0GXhatDMIBoC-6oQAvD_BwE&i=596ed215eec3dfb1f8cca386&o=5cab93d16c28a3cb509d3e00&opn=YSMESP&sellerId=7661688000108
			preco = [round(n[0]*12.81,2),round(n[0]*10.50,2)]
			#https://www.zxcontato.com.br/item/68-matriz?parceiro=5941&gclid=CjwKCAjw7_rlBRBaEiwAc23rhjP29Q5CW_o0RzLBUtbh1d_EwBMhEoxL1otd07g6NB33R3obljtKTRoCus4QAvD_BwE			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome

		elif self.dic[2] == self.d:
			#Chumbo 6V - 1.3Ah  || #Chumbo 12V - 1.3Ah
			nome = ["Bateria de Chumbo 6V - 1.3Ah", "Bateria de Chumbo 12V - 1.3Ah"]
			ddp = [6, 12]
			cc = [round(1.3,2), round(1.3,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 6
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 1.3
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 6
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 1.3
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 12
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://www.americanas.com.br/produto/51985356/bateria-selada-ep-6v-1-3ah?WT.srch=1&acc=e789ea56094489dffd798f86ff51c7a9&epar=bp_pl_00_go_inf-aces_acessorios_geral_gmv_a&gclid=CjwKCAjwzPXlBRAjEiwAj_XTEeMzekB42mEmdpI2eF-gU1ErmSWkrGNuaoswAp04s3C8ND9RlhXu4RoCVuYQAvD_BwE&i=5bdd11aeeec3dfb1f89a257c&o=5c5b2cfd6c28a3cb50631013&opn=YSMESP&sellerId=26164580000146
			preco = [round(n[0]*38.30,2),round(n[0]*55.90,2)]
			#https://www.eletronicasantana.com.br/bateria-selada-vrla-12v-13ah-f187-up1213-rt-06c001-unipower/p?idsku=9002755&utm_source=google_shoppping&utm_medium=cpc&gclid=CjwKCAjw7_rlBRBaEiwAc23rhoCkiE4nXZBYAvz8g9InC9qTIwvTlOpA8xPuTYfi-E8yG4V8svsW9xoCN60QAvD_BwE
			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome
			
		elif self.dic[2] == self.e:
			#Litio Polimer 3.7V - 1.8Ah  || #Litio Ion 3.7 - 2.2Ah
			nome = ["Li-Polymer 3.7V - 1.8Ah", "Li-Ion 3.7V - 2.2Ah"]
			ddp = [3.7, 3.7]
			cc = [round(1.8,2), round(2.2,2)]
			n = [1,1]
			paralelo = [0,0]
			serie = [0,0]
			while(self.ddp > ddp[0]):
				ddp[0] += 3.7
				serie[0] += 1
				n[0] += 1

			while(self.cc > cc[0]):
				cc[0] += 1.8
				paralelo[0] += 1
				n[0] += 1

			pot = [ddp[0]*cc[0],ddp[1]*cc[1]]

			while(self.pot > pot[0]):
				ddp[0] += 3.7
				serie[0] += 1
				n[0] += 1
				pot[0] = ddp[0]*cc[0]

	
			while(self.ddp > ddp[1]):
				ddp[1] += 3.7
				serie[1] += 1
				n[1] += 1

			while(self.cc > cc[1]):
				cc[1] += 2.2
				paralelo[1] += 1
				n[1] += 1

			pot = [round(ddp[0]*cc[0],2),round(ddp[1]*cc[1],2)]
			
			while(self.pot > pot[1]):
				ddp[1] += 3.7
				serie[1] += 1
				n[1] += 1
				pot[1] = ddp[1]*cc[1]

			if self.cons == -1:
				cons = [cc[0]/self.duracao, cc[1]/self.duracao]
			else:
				cons = [self.cons, self.cons]

			tempomax = [round(cc[0]/cons[0],2), round(cc[1]/cons[1],2)]
			relacao = [round(self.duracao/tempomax[0],2), round(self.duracao/tempomax[1],2)]
			#https://pt.aliexpress.com/item/3-7-V-1800-mAh-102560-c-lulas-Li-Po-Bateria-de-i-es-de-l/32834397284.html?spm=a2g03.search0306.3.7.361917bdNKS5tX&ws_ab_test=searchweb0_0%2Csearchweb201602_0_10084_10083_10547_10887_10307_321_453_10548_322_454_10618_536_10065_317_537_10068_319_10059_10103_10884_10696%2Csearchweb201603_0%2CppcSwitch_0&algo_pvid=bfedf084-8128-4d0d-8581-125e33114f36&algo_expid=bfedf084-8128-4d0d-8581-125e33114f36-3
			preco = [round(n[0]*29.21,2),round(n[0]*52.11,2)]

			
			return preco, serie, paralelo, n, tempomax, relacao, ddp, cc, pot, nome



	







			













