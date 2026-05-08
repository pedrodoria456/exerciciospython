def valorTotal (a, b):
    valor = a * b
    return valor

unidade = float(input("Digite o preço do produto: "))
quantidade = float(input("Digite a quantidade comprada: "))
print(valorTotal(unidade, quantidade))