chances = 5
palavra_secreta = 'batata'
while chances > 0: 
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances")
    chances -= 1
    if palavra == 'batata':
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        break
#quando vc acerta a palavra o comando break encerra automaticamente sem fazer outro loop
#quando vc erra a palavra 5 vezes o while se torna verdadeiro e encerra o codigo

