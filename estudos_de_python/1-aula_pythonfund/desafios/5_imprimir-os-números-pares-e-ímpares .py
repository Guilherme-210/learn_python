'''imprimir-os-números-pares-e-ímpares
Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.'''

def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(check_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))