import random
import time
print("Prepare seu dedo no ENTER...")
tempo_espera = random.randint(2, 10)
time.sleep(tempo_espera)
print("\nAGORA!")
tempo_inicial = time.time()
input()
tempo_final = time.time()
tempo_reacao = tempo_final - tempo_inicial
print(f"Você levou {tempo_reacao:.4f} segundos para pressionar ENTER!")