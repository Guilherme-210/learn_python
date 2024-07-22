'''Aumento salário funcionário
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.'''

vs = float(input('Qual e o valor do seu salario atual? '))

if vs > 1250:
    va = vs * 0.10
    aumento = vs + va
    print(f'O valor do seu aumento salarial e de R$:{va:.2f}')
    print(f'Seu salario atual e R$:{aumento:.2f}')
else:
    va = vs * 0.15
    aumento = vs + va
    print(f'O valor do seu aumento salarial e de R$:{va:.2f}')
    print(f'Seu salario atual e R$:{aumento:.2f}')