import random
from forca_art import artes, logo
from forca_palavras import lista_palavras
from replit import clear

print(logo)
fim_de_jogo = False
vida = len(artes) - 1

palavra_escolhida = random.choice(lista_palavras)
word_length = len(palavra_escolhida)

display = []
for _ in range(word_length):
	display += "_"
	
while not fim_de_jogo:
	palpite = input("Adivinhe uma letra ").lower()

	#Use a função clear() importada de replit para limpar a saída entre suposições.
	clear()

	if palpite in display: 
			print(f"Você já adivinhou {palpite}")

			for lugar in range(lista_palavras):
				letra = palavra_escolhida[lugar]
				if letra == palpite:
						display[lugar] == letra
			print(f"{ ' ' .join(display)}")

			if palpite not in palavra_escolhida: 
				print(f"Você adivinhou {palpite}, isso não está na palavra. Você perde uma vida.")
			vida -= 1
			if vida == 0:
				fim_de_jogo = True
				print("Fim de Jogo!")

			if not "_" in display:
				fim_de_jogo = True
			
			print(artes[vida])	
			