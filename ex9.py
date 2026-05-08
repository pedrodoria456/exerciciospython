peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print("Seu imc é", imc, "categoria: abaixo do peso normal")
elif imc > 18.5 and imc <= 24.9:
    print("Seu imc é", imc, "categoria: Peso normal")
elif imc >25 and imc <=29.9:
    print("Seu imc é", imc, "categoria: Excesso de peso")
elif imc >30 and imc <= 34.9:
    print("Seu imc é", imc, "categoria: Obesidade classe 1")
elif imc >35 and imc <=39.9:
    print("Seu imc é", imc, "categoria: Obesidade classe 2")
else:
    print("Seu imc é", imc, "categoria: Obesidade classe 3")