maior = float('-inf')
#o certo é ser -inf
soma = 0
while soma <= 10: 
    #não existe a variavel soma para o loop ser feito
    soma += 1
    #a variavel soma serve como um contador
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
print('O maior número é', maior)

