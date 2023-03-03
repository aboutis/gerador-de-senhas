#Projeto gerador de senhas
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senhas Python!")
nr_letras= int(input("Quantas letras você gostaria de ter na sua senha?\n"))
nr_simbolos = int(input(f"Quantos símbolos você gostaria de ter na sua senha?\n"))
nr_numeros = int(input(f"Quantos números você gostaria de ter na sua senha?\n"))

senha = []
for i in range(nr_letras):
    letra = random.choice(letras)
    senha.append(letra)

for i in range(nr_simbolos):
    simbolo = random.choice(simbolos)
    senha.append(simbolo)

for i in range(nr_numeros):
    numero = random.choice(numeros)
    senha.append(numero)

senha_final = random.shuffle(senha)

for i in range(len(senha)):
  print(senha[i], end='')
