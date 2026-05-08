usuario = input("Digite seu usuario: ")
senha = "admin"
i = 1
while i < 4:
    tentativa = input("Digite sua senha: ")
    if tentativa == senha:
        print("Acesso permitido")
        break
    elif i < 3:
        print("Senha errada. Tentativa nº", i)
        i += 1
    else:
        print ("Acesso negado")
        break