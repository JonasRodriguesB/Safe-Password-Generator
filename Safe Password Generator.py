import random

letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', 'Y', 'W']
letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'x', 'z', 'y', 'w']
simbolos = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
           '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '"', "'", '<',
           '>', '.', '?', '/']

senha = ''

for c in range(15):
    x = random.randint(1, 10)
    if 1 <= x <= 3:
        senha += random.choice(letras_maiusculas)
    elif 4 <= x <= 6:
        senha += random.choice(letras_minusculas)
    elif 7 <= x <= 9:
        senha += str(random.randint(0, 9))
    else:
        senha += random.choice(simbolos)

print('SENHA GERADA!')
print(senha)
