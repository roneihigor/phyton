# Crie um programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Em qual turno você estuda ? Caso seja noturno, digite n, se vespertino, digite v, caso matutino, digite m")

match turno:
    case "m":
        print("Bom dia!")
    case "v":
        print("Boa tarde")
    case "n":
        print("Boa noite!")
    case _:
        print("Valor inválido")

