usuarios = []
idades = []
print("Digite 'encerrar' para encerrar (No usuario ou na idade)")
while True:
    usuario = input("Digite seu nome de usuario: ")
    idade = int(input("Digite sua idade: "))
    if usuario == "encerrar" or idade == "encerrar":
        break
    else:
        usuarios.append(usuario)
        idades.append(idade)

print(len(usuarios))

qtd = 0
for i in idades:
    if i >= 18:
        qtd += 1

print("Tem", qtd, "Maiores de idade")