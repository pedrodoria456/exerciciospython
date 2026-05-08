notas = []
print("Digite -1 para encerrar")
while True:
    nota = float(input("Digite a nota: "))
    if nota == -1:
        break
    else:
        notas.append(nota)

maiornota = 0
menornota = 1000000
media = 0

for valor in notas:
    if valor > maiornota:
        maiornota = valor
    if valor < menornota:
        menornota = valor

    media+=valor
print("A media é:", media / len(notas))
print("A maior nota é:", maiornota)
print("A menor nota é:", menornota)