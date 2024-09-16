import os
def limpa():
    os.system('cls')
limpa()

string = input('Digite um texto: ')
inversa = ' '
for x in string:
    inversa = x + inversa
    
print(inversa)
