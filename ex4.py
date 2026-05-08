valor = float(input("Escreva o valor do carro: "))
imposto = valor * 0.45
lucro_distribuidor = (valor + imposto) * 0.12
preco_total = valor + imposto + lucro_distribuidor

print(
    "O veículo de valor", valor,
    "possui", imposto, "de imposto e",
    lucro_distribuidor, "de lucro do distribuidor, com o preço total de",
    preco_total)