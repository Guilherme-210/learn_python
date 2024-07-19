'''Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

Ex: fifa 23 → **fi#a 23
    restart→ resta#t'''

nome = 'Fifa 23'

caracter = nome[0].lower()
new = nome.replace(caracter, '#')
new = caracter + new[1:]

print(new)