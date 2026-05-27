cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0: 
        continue
    print(f'{num} é um número ímpar')
#Quando o numero é impar o IF se torna falso e o programa le o print e diz que ele é impar 
#Quando o numero é par o programa roda o comando continue e reinicia o loop mas n diz se ele é par ou impar 