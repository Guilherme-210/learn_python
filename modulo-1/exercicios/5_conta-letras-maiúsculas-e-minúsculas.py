'''Conta letras maiúsculas e minúsculas
Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.'''

def check_char(text):
    type={"Uppercase":0, "Lowercase":0}
    for char in text:
        if char.isupper():
            type["Uppercase"]+=1
        elif char.islower():
            type["Lowercase"]+=1
    print ("Texto original: ", text)
    print ("Número de letras maiúsculas: ", type["Uppercase"])
    print ("Número de letras minúsculas: ", type["Lowercase"])

#string_test
check_char("A melhor forMa de Prever o futuro é Criá-Lo")
