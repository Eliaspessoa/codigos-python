logado = False
senha_correta = "Python"

while not logado:

    senha_digitada = input("Digite a senha: ")

    if senha_digitada == senha_correta:
        logado = True
        print("✅ Login bem-sucedido!")
        break
    else:
        print("❌ Senha incorreta. Tente novamente.")