'''Tabuada
Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário'''

number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1