soma = 0
for i in range (1, 4):
    n = float (input("Digite a sua nota: "))
    soma = n + soma

media = soma / 3
if media >= 8:
    print("Sua media foi:", media, "A")
elif media >= 5 and media <8:
    print("Sua media foi:", media, "B")
elif media <5:
    print("Sua media foi:", media, "C")