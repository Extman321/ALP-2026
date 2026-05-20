N = int(input("Quantos números quer digitar?"))
contador = 0
#o contador deve ser 0 pois não houve nenhuma tentativa
impares = 0

while contador <= N:
    #não é <= e sim < pois se for <= ira ter um numero a mais para ser digitado
    num = int(input("Digite um número: "))
    #o while nunca vai ser true pois falta a variavel contador += 1
    contador += 1
    if num % 2 != 0:
        impares += 1
print(f"voce digitou {impares} numeros impares")
#erro de logica pois a variavel N é quantos numeros a pessoa ira digitar

