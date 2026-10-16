# Leia o preço de um lanche, a quantidade comprada e o valor que o cliente pagou. Mostre o total da compra e 
# o troco. Considere que o valor pago é sempre suficiente. 

preco = float(input("Digite o preço do lanche: "))
quantidade = int(input("Digite a quantidade de lanches: "))

valorTotal = preco * quantidade

print(f"O valor a ser pago é de: {valorTotal}")

troco = float(input("Digite o valor recebido: "))

trocoCliente = troco - valorTotal

print(f"O valor total da compra ficou em: {valorTotal}")
print(f"O cliente pagou {troco}e o valor do troco é de: {trocoCliente}")