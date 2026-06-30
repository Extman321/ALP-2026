import random
import time
N = random.randint(0, 10)
print(f"O número misterioso sorteado foi: {N}\n")
for volta in range(1, N + 1):
    print(f"Volta {volta}: Mais uma volta!")
    time.sleep(1)  # Pausa de 1 segundos