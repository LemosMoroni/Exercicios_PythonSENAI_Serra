# Leia o preço de um lanche, a quantidade comprada e o valor que o cliente pagou. Mostre o total da compra e 
# o troco. Considere que o valor pago é sempre suficiente. 

#Entrada de dados inicial dos clientes
preco = float(input("Digite o preço do lanche: "))
quantidade = int(input("Digite a quantidade de lanches: "))

#Cálculo do valor total da compra
valorTotal = preco * quantidade

#Mostra na tela o valor total e pede para o usuário digitar o valor total recebido
print(f"O valor a ser pago é de: {valorTotal}")
troco = float(input("Digite o valor recebido: "))

#Cálculo do troco do cliente
trocoCliente = troco - valorTotal

#Resultado final com todas as informações na tela
print(f"O valor total da compra ficou em: {valorTotal}")
print(f"O cliente pagou {troco} e o valor do troco é de: {trocoCliente}")