# Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um programa que permita a entrada das seguintes informações:

# a) o nome e o número total de mercadorias no estoque;
# b) o valor da mercadoria.
# Ao final imprimir o valor total em R$ do estoque total do produto e o valor de venda de um item acrescido de 30%. Ao final pergunte se deseja continuar a operação com um novo produto

continuar = 'S'
while continuar == 'S':

    Nmercadoria = str(input("Digite o nome da mercadoria: "))
    Qmercadoria = int(input("Qual a quntidade em estoque dessa mercadoria? "))
    Vmercadoria = float(input("Qual o valor dessa mercadoria? "))
    venda = Vmercadoria + Vmercadoria*30/100
    Vtotal = Qmercadoria * Vmercadoria
    print("Você venderá esse produto por: R$" , venda)
    print("O total em reais do estoque total dessa mercadoria é de R$: " , Vtotal)

    continuar = input("você deseja continuar? s ou n").upper()
