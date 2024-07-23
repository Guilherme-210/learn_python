''' Cálculo da Distância
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.'''

km = float(input('Qual e a distancia que vc quer percorrer em km? '))

if km <= 200:
    vp = km * 0.5
    print('O valor da passagem ta R$:0,50 centavos por km.')
    print(f'Vai ficar um total de R$:{vp:.2f}.')

else:
    vp = km * 0.35
    print('O valor da passagem ta R$:0,35 centavos por km.')
    print(f'Vai ficar um total de R$:{vp:.2f}.')
