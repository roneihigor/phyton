# Crie um programa para calcular as notas obtidas pelo aluno do ensino médio
# deverá mostrar mensagem para ser digitado a nota do 1º, 2º, 3º e 4º bimestre.
# Após deverá mostrar na tela se o aluno foi aprovado, se está em recuperação ou foi reprovado sem chance de recuperação.

nota1 = float(input("digite a nota do primeiro bimestre do aluno (valor de 0-25) "))
nota2 = float(input("digite a nota do segundo bimestre do aluno (valor de 0-25) "))
nota3 = float(input("digite a nota do terceira bimestre do aluno (valor de 0-25) "))
nota4 = float(input("digite a nota do quarto bimestre do aluno (valor de 0-25) "))
resultado = nota1 + nota2 + nota3 + nota4

print("a nota obtida pelo aluno foi: " , resultado)

if (resultado >= 60):
    print("o aluno está aprovado")
elif (resultado < 40):
    print("o aluno foi reprovado")
elif (resultado < 60 or resultado >= 40):
    print("o aluno está em recuperação")
