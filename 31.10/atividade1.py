# Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# Mostre as consoantes.

lista = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    lista[10] = input("Digite uma letra para cada posição ")

vogal = input("digite uma vogal para localizar no vetor")

for i in range(10):
    if (lista[10] == vogal):
        print("vogal encontrada")
        vogal = True

if(vogal is False):
    print("vogal não encontrada!")



print(lista)
print(vogal)



