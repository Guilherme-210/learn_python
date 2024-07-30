import random

r1 = random.randint(0, 9)
print(r1)
v1 = int(input('Qual foi o valor gerado: '))

while v1 != r1:
    print('Número errado, tente de novo')
    v1 = int(input('Qual foi o valor gerado: '))

print('Parabéns, o número está correto!')