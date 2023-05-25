valor = float(input("Digite o valor: "))
taxa = float(input("Digite o valor da taxa: "))
tempo = float(input("Digite o valor do tempo: "))

prestacao = valor + (valor * (taxa/100) * tempo)

print(f"O valor da prestação é {prestacao}!")