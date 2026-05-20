soma = 0
#adicionamos um contador
contador = 0
while contador < 10: 
 #não é <= e sim < pois se for <= ira ter um numero a mais para ser digitado
 #o while vai ser true quando a soma for 10 e não quando vc digitar 10 numeros
    num = int(input("Digite um número para somar: "))
    soma += num
    contador += 1
#falta um print para imprimir a soma dos 10 numeros
print('a soma dos numeros é', soma)
    

