# Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# Mostre as consoantes.

lista = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    lista[i] = input("Digite uma letra para a posição " + str(i)+ ": ")
print(lista)

consoante = 0

for i in range(10):
   if not (lista[i] == str ('a') or lista[i] == str ('e') or lista[i] == str ('i') or lista[i] == str ('o') or lista[i] == str ('u')):
       print("consoante na posição: " + str(i+1) + ":" , lista[i])
       consoante=consoante+1

print("a quantidade de consoante é :" , consoante)
