# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado

n1 = float(input("digite a nota 1: "))
n2 = float(input("digite a nota2: "))
n3 = float(input("digite a nota 3: "))

# calcule a média

média = (n1 + n2 + n3) / 3
print (f"a média é {média}")

# aprovação

if média >=7:
    print("aprovado")
else:
    print("recuperação")