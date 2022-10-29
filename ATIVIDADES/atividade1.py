# Crie um programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Em qual turno você estuda ? Caso seja noturno, digite n, se vespertino, digite v, caso matutino, digite m ").upper()

match turno:
    case "M":
        print("Bom dia!")
    case "V":
        print("Boa tarde")
    case "N":
        print("Boa noite!")
    case _:
        print("Valor inválido")
