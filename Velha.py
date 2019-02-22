jogador = ["",""]
jogador[0] = input("Digite o Nome do jogador1: ")
jogador[1] = input("Digite o Nome do jogador2: ")
print("os jogadores são:", jogador[0],"e", jogador[1])
j = 0
vitoria = True
espacito = ["_","_","_","_","_","_","_","_","_"] 

def printaTabuleiro():
	print("\n%s|%s|%s\n%s|%s|%s\n%s|%s|%s" %(espacito[0],espacito[1], espacito[2], espacito[3], espacito[4], espacito[5], espacito[6], espacito[7], espacito[8] ))
	k = 0
	
	if (espacito[0] == "X" and espacito[4]== "X" and espacito[8] == "X") or (espacito[2] == "X" and espacito[4] == "X" and espacito[6] == "X" ):
		print("Vitoria do %s" %jogador[0])
		return False

	if (espacito[0] == "O" and espacito[4]== "O" and espacito[8] == "O") or (espacito[2] == "O" and espacito[4] == "O" and espacito[6] == "O" ):
		print("Vitoria do %s" %jogador[1])
		return False

	for c in range(0, 3):
		if(espacito[c] == "X" and espacito[c + 3] == "X" and espacito[c + 6] == "X" ):
			print("Vitoria do %s" %jogador[0])
			return False
		elif(espacito[c] == "O" and espacito[c + 3] == "O" and espacito[c + 6] == "O" ):
			print("Vitoria do %s" %jogador[1])
			return False
		elif(espacito[c*3] == "X" and espacito[c*3 + 1] == "X" and espacito[c*3 + 2] == "X" ):
			print("Vitoria do %s" %jogador[0])
			return False
		elif(espacito[c*3] == "O" and espacito[c*3 + 1] == "O" and espacito[c*3 + 2] == "O" ):
			print("Vitoria do %s" %jogador[1])
			return False

	for x in range(0, len(espacito)):
		if espacito[x] == "_":
			k +=1
	if k == 0:
		return False
	
	return True

print("0|1|2\n3|4|5\n6|7|8")
while vitoria:
	i = int(input("%s Digite o numero da casa desejada" %jogador[j] ))
	if i > 8: print("Jogada Invalida")
	elif i >= 0:

		if espacito[i] == "_":

			if j == 0:
				espacito[i] = "X"
				j += 1
				if j == 2:
					j = 0
			else:
				espacito[i] = "O"
				j += 1
				if j == 2:
					j = 0
			vitoria = printaTabuleiro()
		else: print("Jogada Invalida")
	else:
		print("Jogada Invalida")


print("Jogo terminou")