n = 0
soma = 0
while n < 100:
    escolha = int(input('Escolha um numero: '))
    if escolha < 0 :
        print('Escolha apenas numeros positivos')
    elif escolha == 0:
        break
    else:
        n += escolha
print(f'A soma deu {n}')
    