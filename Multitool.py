Nome = input("Digite seu nome: ")
Idade = int(input("Digite sua idade: "))

print("Escolha a Operação:\n 1: Calculadora \n 2: Conversor de Temperatura \n 3: Media de notas \n -1: Sair")
OP = int(input())
# Apos o usuario escolher o numero da operação começa os checks, se ele for -1 o codigo acaba.

# Metodo Para reiniciar o codigo
def meuMetodo():
	print("Escolha a Operação:\n 1: Calculadora \n 2: Conversor de Temperatura \n 3: Media de notas \n -1: Sair")
	return int(input())


while OP != -1:
	if OP > 0 and OP<4:

	# Aqui o programa ve se o input é valido

		if(OP == 1):
			#O usuario colocou operação 1 e ele vai decidir o tipo de calculo
			Metodo = input("Operação 1: Calculadora \n Selecione o Tipo de calculo: \n A: Adição \n S: Subtração \n M: Multiplicação \n D: Divisão:")
			if Metodo == "A" or Metodo == "a":
				n1 = float(input("Primeiro Número"))
				n2 = float(input("Segundo Número"))
				soma = n1 + n2
				print ("O Resultado é:",soma)
				
				#Aqui o Codigo volta ao inicio
				OP = meuMetodo()
				
			elif Metodo == "S" or Metodo == "s":
				n1 = float(input("Primeiro Número"))
				n2 = float(input("Segundo Número"))
				soma = n1 - n2
				print("O resultado é:",soma)
				
				#Aqui o codigo volta ao inicio
				OP = meuMetodo()

			elif Metodo == "M" or Metodo == "m":
				n1 = float(input("Primeiro Número"))
				n2 = float(input("Segundo Número"))
				soma = n1 * n2
				print("O resultado é:",soma)
				
				#Aqui o codigo volta ao inicio
				OP = meuMetodo()

			elif Metodo == "D" or Metodo == "d":
				n1 = float(input("Primeiro Número"))
				n2 = float(input("Segundo Número"))
				soma = n1 / n2
				print("O resultado é:",soma)

				#Aqui o codigo volta ao inicio

				OP = meuMetodo()
			else:
				#Erro, volta ao inicio
				print("Operação invalida")
				OP = meuMetodo()
#------------------------------- separação do codigo ----------------------------------------------------------

		elif(OP == 2):
			print("Operação 2: Conversor de Temperaturas: \n Digite 1 para converter Celsius para fahrenheit \n Digite 2 para converter fahrenheit para Celsius: ")
			escolha = float(input())
			if escolha == 1:
				#celsiu
				n1 = float (input("Temperatura em Celsius:"))
				temperatura = n1 * 1.8 + 32
				print("A Temperatura em Fahrenheit é:", temperatura)

				OP= meuMetodo()
			elif escolha == 2:
				#fahrenheit
				n1 = float(input("Digite a Temperatura em Fahrenheit:"))
				temperatura = (n1 -32)/1.8 
				print("A temperatura em Celsius é:", temperatura)
				OP= meuMetodo()
			else:
				print("Operação invalida")
				OP = meuMetodo()
#--------------------------------------------------------------------------------------------------------------
		elif(OP == 3):
			#O usuario escolheu medias, ele digita 4 numeros e ele calcula a media simples
			print ("Operação 3: Media simples de 4 notas")
			n1= float(input("Digite a Primeira Nota:"))
			n2= float(input("Digite a Segunda Nota:"))
			n3= float(input("Digite a Terceira Nota:"))
			n4= float(input("Digite a Quarta Nota:"))
			soma = (n1+n2+n3+n4)/4
			print("A media é:",soma)
			OP = meuMetodo()

	else:
	   print("Operação invalida")
	   OP = meuMetodo()

#Aqui o codigo acaba pois ele não aceita -1
print ("Programa terminado, Adeus", Nome)