import random 
import time
while True: 
    pergunta = input('Você deseja fazer uma pergunta? (s/n): ')
    if pergunta == 'n':
        break
    elif pergunta == 's':
        pergunta_s = input('Digite sua pergunta de sim ou não: ')
        prob = random.randint(1, 10)
        print('Estou pensando')
        time.sleep(2)
        print('Calma lá')
        time.sleep(2)
        print('So mais um minuto')
        print
        if prob <=5:
            print('Sim')
            resposta='SIM'
            continue
        else: 
            print('Não')
            continue
    else: 
        print('Resposta invalida')

    