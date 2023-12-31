import logica

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def pede_categoria():
    while True:
        print("Escolha uma categoria:")
        print("1 - Frutas")
        print("2 - Animais")
        print("3 - Países")
        print("4 - Profissões")
        opcao = input("Digite o número da categoria desejada: ")

        if opcao == "1":
            return "frutas"
        elif opcao == "2":
            return "animais"
        elif opcao == "3":
            return "paises"
        elif opcao == "4":
            return "profissoes"
        else:
            print("Opção inválida. Escolha novamente.")

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    imprime_mensagem_abertura()

    categoria = pede_categoria()
    palavra_secreta = logica.carrega_palavra_secreta(categoria)
    letras_acertadas = logica.inicializa_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(letras_acertadas)

    while not acertou and not enforcou:
        chute = pede_chute()

        if logica.letraInPalavra(chute, palavra_secreta):
            if chute not in letras_acertadas:
                letras_acertadas.append(chute)
                letras_acertadas.sort()

        else:
            erros += 1
            print(letras_acertadas)
            print('Ainda faltam acertar {} letras'.format(letras_faltando))
            print('Você ainda tem {} tentativas'.format(7 - erros))
            desenha_forca(erros)

        logica.mostrarPalavraComLetra(palavra_secreta, letras_acertadas)

        letras_faltando = str(letras_acertadas.count('_'))
        if letras_faltando == "0":
            print("PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(palavra_secreta.upper()))

        enforcou = erros == 7
        acertou = logica.verificarFimDeJogo(palavra_secreta, letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

if __name__ == '__main__':
    jogar()
