import datetime
hoje = datetime.datetime.now()
data_prova = datetime.datetime(2026, 7, 14)
diferenca = data_prova - hoje
print(f"Faltam exatamente {diferenca.days} dias para a sua prova!")