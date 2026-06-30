import datetime
nome1 = input("Digite o nome da primeira pessoa: ")
data_str1 = input("Digite a data de nascimento (dd/mm/aaaa): ")
data1 = datetime.datetime.strptime(data_str1, "%d/%m/%Y")
nome2 = input("Digite o nome da segunda pessoa: ")
data_str2 = input("Digite a data de nascimento (dd/mm/aaaa): ")
data2 = datetime.datetime.strptime(data_str2, "%d/%m/%Y")
if data1 < data2:
    print(f"\n{nome1} é mais velho(a) que {nome2}.")
elif data2 < data1:
    print(f"\n{nome2} é mais velho(a) que {nome1}.")
else:
    print(f"\n{nome1} e {nome2} têm exatamente a mesma idade!")