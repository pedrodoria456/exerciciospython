id = str(input("Digite o ID do vendedor: "))
codp = str(input("Digite o codigo do produto: "))
precuni = float(input("Digite o preço unitario do produto: "))
qtd = int(input("Digite a quantidade vendida: ") )

comissao = (precuni * qtd) *   0.05



print("Id vendedor:", id, "Comissão:", comissao)