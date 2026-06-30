import random
import time
print("Prepare o dedo no ENTER e aguarde o sinal...")
tempo_espera = random.randint(2, 10)
time.sleep(tempo_espera)
print("\nAGORA!")
tempo0 = time.time()
input()
tempo1 = time.time()
tempo_final = tempo1 - tempo0
print(f"Você levou {tempo_final:.4f} segundos para responder!")