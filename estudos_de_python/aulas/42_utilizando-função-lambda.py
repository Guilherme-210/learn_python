#função de potencia de numero
power = lambda num: num ** 2

print(power(5))
print(power(9))

#função que verifica se o numero e par
pair = lambda x: x%2==0

print(pair(27))
print(pair(30))

#função que divide um numero por outro
divNum = lambda x,y : x/y

print(divNum(10,2))
print(divNum(7,2))

#função que inverte uma string
reverse = lambda s: s[::-1]

print(reverse("Função"))
print(reverse("Tecnologia"))