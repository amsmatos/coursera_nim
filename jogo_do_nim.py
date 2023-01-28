def computador_escolhe_jogada(n,m):
	m2 = 1

	while m2 != m:
		resultado = n - m2
		if resultado % (m + 1) == 0:
			return m2
		else:
			m2 = m2 + 1
			resultado = n - m2
	return m2
				

def usuario_escolhe_jogada(n,m):
	tira = int(input("Quantas peças você vai tirar? "))
	
	while tira <=0 or tira > m or tira >n:
		print("Oops! Jogada inválida! Tente de novo.\n")
		tira = int(input("Quantas peças você vai tirar? "))
	if tira > 1:
		print("Você tirou ", tira," peças.")
	else:
		print("Você tirou uma peça.")
	return tira
	
def partida():
	print("Voce escolheu uma partida!\n")
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	fim = bool(False)
	
	while m >= n:
		print("Valores inválidos\n")
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
	if n >0:
		pc = bool(True)
		a = 1
		
		while a <= n:	
			quem_joga = (m * a)+1
			if quem_joga == n:
				pc = bool(False)
				print("\nVoce começa!")
				a = n + a
			else:
				if  quem_joga > n:
					pc = bool(True)
					print("\nComputador começa!")
					a = n + a
				a = a + 1
				
		while n>=1:
			if pc == False:
				desconta = usuario_escolhe_jogada(n,m)
				n = n - desconta
				pc = True
				if n >1:
					print("Agora restam ",n," peças no tabuleiro.")
				else:
					if n == 1:
						print("Agora resta apenas uma peça no tabuleiro.")
				if n == 0 and fim != True:
					print("Fim do jogo! Você ganhou!")
					fim = True
			if pc == True:
				desconta = computador_escolhe_jogada(n,m)
				n = n - desconta
				pc = False
				if desconta > 1:
					print("O computador tirou ", desconta," peças.")
				else:
					print("O computador tirou uma peça.")			
				if n >1:
					print("Agora restam ",n," peças no tabuleiro.")
				else:
					if n == 1:
						print("Agora resta apenas uma peça no tabuleiro.")
				if n == 0 and fim != True:
					print("Fim do jogo! O computador ganhou!")
					fim = True

def campeonato():
		print("Voce escolheu um campeonato!\n")
		i = 1
		vitoria_humano = 0
		vitoria_computador = 0
		
		while i <=3:
			print("**** Rodada ",i," ****\n")
			n = int(input("Quantas peças? "))
			m = int(input("Limite de peças por jogada? "))
			fim = bool(False)
			
			while n < m or n == 0:
				print("Valores inválidos\n")
				n = int(input("Quantas peças? "))
				m = int(input("Limite de peças por jogada? "))
			if n >0:
				pc = bool(True)
				a = 1
				
				while a <= n:
					quem_joga = (m * a) + 1
					if quem_joga == n and m != 1:
						pc = bool(False)
						print("\nVoce começa!")
						a = a + n
					else:
						if quem_joga > n or m == 1:
							pc = bool(True)
							print("\nComputador começa!")
							a = a + n
					a = a + 1
					
			while n>=1:
				if pc == False:
					desconta = usuario_escolhe_jogada(n,m)
					n = n - desconta
					pc = True
					if n >1:
						print("Agora restam ",n," peças no tabuleiro.\n")
					else:
						if n == 1:
							print("Agora resta apenas uma peça no tabuleiro.\n")
						if n == 0 and fim != True:
							print("Fim do jogo! Você ganhou!\n")
							vitoria_humano = vitoria_humano + 1
							fim = True
							pc = False
				if pc == True:
					desconta = computador_escolhe_jogada(n,m)
					n = n - desconta
					pc = False
					if desconta > 1:
						print("O computador tirou ", desconta," peças.")
					else:
						print("O computador tirou uma peça.")
					if n >1:
						print("Agora restam ",n," peças no tabuleiro.\n")
					else:
						if n == 1:
							print("Agora resta apenas uma peça no tabuleiro.")
						if n == 0 and fim != True:
							print("Fim do jogo! O computador ganhou!\n")
							vitoria_computador = vitoria_computador + 1
							fim = True
			i = i +1            
			if i >3:
				print("**** Final do campeonato! ****\n")
				print("Placar: Você ",vitoria_humano," X ",vitoria_computador," Computador")

def inicio():
        print("Bem-vindo ao jogo do NIM! Escolha:\n")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        a = int(input())
        
        while a < 1 or a > 2:
                a = int(input())
        if a == 1:
                partida()
        if a == 2:
                campeonato()

# inicia o programa
inicio()