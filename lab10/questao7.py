jogos = int(input())

vitorias = 0
empates = 0
derrotas = 0

for i in range(jogos):
    gols_galo = int(input())
    gols_oponente = int(input())

    if gols_galo > gols_oponente:
        vitorias += 1
    elif gols_galo == gols_oponente:
        empates += 1
    else:
        derrotas += 1

pontuacao = vitorias * 3 + empates

print("Vitórias:", vitorias)
print("Empates:", empates)
print("Derrotas:", derrotas)
print("Pontuação:", pontuacao)