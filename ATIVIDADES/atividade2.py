#  Crie um programa para realizar as operações de uma tabuada de multiplicação
#  onde será solicitado ao usuário digitar qual numero será a tabuada e qual intervalo do inicio e fim da tabuada
#  e exibir na tela o resultado conforme intervalo.

divisor = int(input("digite qual o numero da tabuada "))
inicio = int(input("digite de qual numero inicirá "))
final = int(input("digite em qual numero finaliza sua tabuada "))

for i in range(inicio , final + 1):
    resultado = (divisor * inicio)
    print("resultado de " , divisor , " * " , inicio , " = " , resultado )
    inicio = inicio + 1