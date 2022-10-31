
#• Crie um programa para calcular as notas obtidas pelo aluno do ensino médio
# deverá mostrar mensagem para ser digitado a nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho.
# Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4ºbimestre.
# E depois o total informado se o aluno foi aprovado, esta em recuperação ou foi reprovado sem recuperação.

nota1p = float(input("digite a nota da prova no primeiro bimestre "))
nota1t = float(input("digite a nota do trabalho no primeiro bimestre "))
resultadobimestral1 = nota1p + nota1t
print("a nota obtida pelo aluno no primeiro bimestre foi: " , resultadobimestral1)

nota2p = float(input("digite a nota da prova no segundo bimestre "))
nota2t = float(input("digite a nota do trabalho no segundo bimestre "))
resultadobimestral2 = nota2p + nota2t
print("a nota obtida pelo aluno no segundo bimestre foi: " , resultadobimestral2)

nota3p = float(input("digite a nota da prova terceiro bimestre "))
nota3t = float(input("digite a nota do trabalho terceiro bimestre "))
resultadobimestral3 = nota3p + nota3t
print("a nota obtida pelo aluno no terceiro bimestre foi: " , resultadobimestral3)


nota4p = float(input("digite a nota da prova quarto bimestre "))
nota4t = float(input("digite a nota do trabalho quarto bimestre "))
resultadobimestral4 = nota4p + nota4t
print("a nota obtida pelo aluno no quarto bimestre foi: " , resultadobimestral4)

resultadofinal = resultadobimestral1 + resultadobimestral2 + resultadobimestral3 + resultadobimestral4

print("a nota total obtida pelo aluno foi: " , resultadofinal)

if (resultadofinal >= 60):
    print("o aluno está aprovado")
elif (resultadofinal< 40):
    print("o aluno foi reprovado")
elif (resultadofinal < 60 or resultadofinal >= 40):
    print("o aluno está em recuperação")