
import random
secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    if palpite == secreto:
        print('Você acertou parabens!!')
        break
    elif 1 > palpite > 10:
        continue
    chances -= 1
    print('Agora vc tem',chances,'chances')
if chances == 0:
    print('Vc perdeu todas as sua chances')
    
    
    

