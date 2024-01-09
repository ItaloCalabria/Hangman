import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "desenvolvimento"]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 6

    while tentativas > 0:
        palavra_atual = ""

        for letra in palavra:
            if letra in letras_certas:
                palavra_atual += letra + " "
            else:
                palavra_atual += "_ "

        print("\nPalavra: ", palavra_atual)
        print("Tentativas restantes:", tentativas)
        print("Letras erradas:", letras_erradas)

        if "_" not in palavra_atual:
            print("\nParabéns! Você ganhou!")
            break

        letra_usuario = input("\nDigite uma letra: ").lower()

        if letra_usuario in palavra:
            letras_certas.append(letra_usuario)
        else:
            letras_erradas.append(letra_usuario)
            tentativas -= 1

    else:
        print("\nGame Over! A palavra era:", palavra)

jogar_forca()
