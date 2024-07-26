# Verificar-conteúdo-da-string.py
# Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).

import re

def Check_character(string):
  rule = re.compile(r'[^a-zA-Z0-9]')
  string = rule.search(string)
  return not bool(string)

print(Check_character('fdjtgJTYJGHFDJrjhgdfj4654324'))
print(Check_character('fdjtgJTYJGHFD Jrjhgd.fj4654324'))
print(Check_character('fdjtgJTYJáGHFDJrjhgdfj4654324'))