# Aula 1 - Atividade 1

'''1 - Conversão de graus Celsius para Fahrenheit - Crie um programa que converta graus Celsius em Fahrenheit. A fórmula é a seguinte: F = 9 / 5 C +32. O programa deve solicitar ao usuário que insira uma temperatura em graus Celsius e, em seguida, exiba a temperatura convertida em Fahrenheit. Após construir esse programa, modifique-o para que converta graus Fahrenheit em graus Celsius.'''

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em graus fahrenheit é:", fahrenheit, "F")


fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit - 32) / (9/5)
print("A temperatura em graus celsius é:", celsius, "C")


'''2 - Escreva um programa que receba um número e escreva “Par” caso esse número seja par e escreva “Impar” caso esse número seja ímpar.'''

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")



'''3 - Escreva um programa que receba dois números, exiba as opções:
1 - adição
2 - subtração
Então peça ao usuário para escolher uma das opções. Caso escolha a opção 1 o programa deve realizar a soma dos dois números lidos e exibir. Caso escolha a opção 2 o programa deve realizar a subtração dos dois números lidos e exibir.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Selecione a operação:")
print("1 - Adição")
print("2 - Subtração")
opcao = input("Digite o número da operação desejada: ")

if opcao == '1':
    resultado = num1 + num2
    print("O resultado da adição é:", resultado)
elif opcao == '2':
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)
else:
    print("Opção inválida.")



'''4 - Numa determinada escola, os critérios de aprovação são os seguintes:
- O aluno deve ter, no máximo, 25% de faltas;
- A nota final deve ser igual ou superior a 7,00.
Construa um programa para ler as notas que um aluno tirou nos 4 bimestres, o número total de aulas e o número de faltas, mostrando ao final a situação do aluno como sendo “Aprovado”, “Reprovado por Faltas” e “Reprovado por média”, considerando que a reprovação por faltas se sobrepõe a reprovação por nota.'''

nota_bimestre1 = float(input("Digite a nota do primeiro bimestre: "))
nota_bimestre2 = float(input("Digite a nota do segundo bimestre: "))
nota_bimestre3 = float(input("Digite a nota do terceiro bimestre: "))
nota_bimestre4 = float(input("Digite a nota do quarto bimestre: "))
total_aulas = int(input("Digite o número total de aulas: "))
faltas = int(input("Digite o número de faltas: "))

if nota_bimestre1 >= 0 and nota_bimestre2 >= 0 and nota_bimestre3 >= 0 and nota_bimestre4 >= 0 and total_aulas > 0:
    media = (nota_bimestre1 + nota_bimestre2 + nota_bimestre3 + nota_bimestre4) / 4
    percentual_faltas = (faltas / total_aulas) * 100

    if percentual_faltas > 25:
        print("Reprovado por faltas")
    elif media >= 7.0:
        print("Aprovado")
    else:
        print("Reprovado por média")
else:
    print("As notas devem ser maiores ou iguais a zero, e o número total de aulas deve ser maior que zero.")


'''5 - Após construir o programa anterior, crie mais duas versões dele para prever as seguintes situações:
- Um aluno pode ficar em recuperação se possuir frequência suficiente (superior a 75%) e média superior a 5 mas inferior a 7;
- Caso um aluno reprove por média e faltas, sua situação deve ser “Reprovado por Média e Faltas” (ao invés de simplesmente “Reprovado por Faltas” como antes).'''

#Versão 1

nota_bimestre1 = float(input("Digite a nota do primeiro bimestre: "))
nota_bimestre2 = float(input("Digite a nota do segundo bimestre: "))
nota_bimestre3 = float(input("Digite a nota do terceiro bimestre: "))
nota_bimestre4 = float(input("Digite a nota do quarto bimestre: "))

total_aulas = int(input("Digite o número total de aulas: "))
faltas = int(input("Digite o número de faltas: "))

media = (nota_bimestre1 + nota_bimestre2 + nota_bimestre3 + nota_bimestre4) / 4
percentual_faltas = (faltas / total_aulas) * 100

if percentual_faltas > 25:
    print("Reprovado por faltas")
elif media >= 7.0:
    print("Aprovado")
elif media >= 5.0 and percentual_faltas <= 75:
    print("Recuperação")
else:
    print("Reprovado por média")

#Versão 2

nota_bimestre1 = float(input("Digite a nota do primeiro bimestre: "))
nota_bimestre2 = float(input("Digite a nota do segundo bimestre: "))
nota_bimestre3 = float(input("Digite a nota do terceiro bimestre: "))
nota_bimestre4 = float(input("Digite a nota do quarto bimestre: "))

total_aulas = int(input("Digite o número total de aulas: "))
faltas = int(input("Digite o número de faltas: "))

media = (nota_bimestre1 + nota_bimestre2 + nota_bimestre3 + nota_bimestre4) / 4
percentual_faltas = (faltas / total_aulas) * 100

if percentual_faltas > 25 and media < 7.0:
    print("Reprovado por média e faltas")
elif percentual_faltas > 25:
    print("Reprovado por faltas")
elif media >= 7.0:
    print("Aprovado")
elif media >= 5.0 and percentual_faltas <= 75:
    print("Recuperação")
else:
    print("Reprovado por média")



'''6 - Escreva um programa que peça ao usuário para fornecer um dia, mês e ano arbitrários e determine se esses dados correspondem a uma data válida. Não deixe de considerar que existem meses com 30 e 31 dias, e que fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto. Considere que um ano é bissexto quando for divisível por 4.'''

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if mes < 1 or mes > 12:
    print("Data inválida.")
else:
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        max_dias = 31
    elif mes in {4, 6, 9, 11}:
        max_dias = 30
    else:
        max_dias = 29 if bissexto else 28

    if 1 <= dia <= max_dias:
        print("Data válida.")
    else:
        print("Data inválida.")


'''7 - Construa um programa que leia uma data qualquer (dia, mês e ano) e calcule a data do próximo dia. Lembre-se que em anos bissextos o mês de fevereiro tem 29 dias. Lembre-se que um ano é bissexto quando for divisível por 4.'''

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

bissexto = (ano % 4 == 0)
dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if bissexto:
    dias_por_mes[2] = 29

if dia < 1 or dia > dias_por_mes[mes]:
    print("Data inválida.")
else:
    if dia == dias_por_mes[mes]:
        dia = 1
        if mes == 12:
            mes = 1
            ano += 1
        else:
            mes += 1
    else:
        dia += 1

    print("Data do próximo dia: " + str(dia) + "/" + str(mes) + "/" + str(ano))


'''8 - Faça um programa que leia duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento
- Entre 9.0 e 10.0 Conceito - A
- Entre 7.5 e 8.9 - B
- Entre 6.0 e 7.4 - C
- Entre 4.0 e 5.9 - D
- Entre 0 e 3.9 - E
O programa deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem:
APROVADO se o conceito for A, B ou C.
REPROVADO se o conceito for D ou E.'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

print("Notas: " + str(nota1) + " e " + str(nota2))
print("Média: " + str(media))
print("Conceito: " + conceito)

if conceito in {"A", "B", "C"}:
    print("APROVADO")
else:
    print("REPROVADO")


'''9 - As organizações XTC resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calcula os reajustes. Faça um programa que recebe o salário de um colaborador e o reajustes segundo o seguinte critério, baseado no salário atual:
- Salários até R$ 280 (incluindo): aumento de 20%
- Salários entre R$ 280 e R$ 700: aumento de 15%
- Salários entre R$ 700 e 1500: aumento de 10%
- Salários de R$1500 em diante: aumento de 5%
Após o aumento ser realizado informe na tela:
- O salário antes do reajuste;
- O percentual de aumento aplicado;
- O valor do aumento;
- O novo salário, após o aumento.'''

salario = float(input("Digite o salário do colaborador: "))

if salario <= 280.00:
    aumento = 20
elif salario <= 700.00:
    aumento = 15
elif salario <= 1500.00:
    aumento = 10
else:
    aumento = 5

aumento_valor = salario * (aumento / 100)
novo_salario = salario + aumento_valor

print("Salário antes do reajuste: R$", salario)
print("Percentual de aumento aplicado:", aumento, "%")
print("Valor do aumento: R$", aumento_valor)
print("Novo salário, após o aumento: R$", novo_salario)



