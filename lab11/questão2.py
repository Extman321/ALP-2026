respostav = 's', 'S', 'sim', 'SIM','n', 'N', 'nao', 'NAO'
while True: 
    resposta = input('Você quer saber como deixar uma pessoa ingenua ocupada por horas? S/N ')
    if resposta == 's' or resposta == 'S' or resposta == 'sim' or resposta == 'SIM':
        continue
    elif resposta == 'n' or resposta == 'N' or resposta == 'nao' or resposta == 'NAO':
        print('Obrigado, tenha um bom dia!')
        break
    else: 
        print('Isso não é uma resposta valida')