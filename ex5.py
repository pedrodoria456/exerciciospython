nome = str(input("Digite o seu nome: "))
satual = float(input("Digite o salario: "))
snovo = 0

if satual <= 1000:
    snovo = satual * 1.20
elif satual <= 5000:
    snovo = satual * 1.10
else:
    snovo = satual * 1.05
    
print ("Jogador:", nome, "Salario novo", snovo)