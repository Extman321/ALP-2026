total = 0 
while True:
    
    print("\n--- CARDÁPIO ---")
    print("1. Açaí 300ml - R$ 12,00")
    print("2. Mousse - R$ 6,50")
    print("3. Salada de frutas - R$ 10,00")
    print("4. Fechar a conta")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        total += 12
        print("Açaí adicionado!")
        
    elif opcao == 2:
        total += 6.50
        print("Mousse adicionada!")
        
    elif opcao == 3:
        total += 10
        print("Salada de frutas adicionada!")
        
    elif opcao == 4:
        print(f"Total da conta: R$ {total:.2f}")
        print("Conta fechada. Obrigado!")
        break  
        
    else:
        print("Opção inválida!")
        continue