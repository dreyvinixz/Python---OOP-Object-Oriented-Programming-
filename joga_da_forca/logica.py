import random

class Frutas:
    palavras = [
        "ABACAXI",
        "BANANA",
        "MELANCIA",
        "LARANJA",
        "MORANGO",
        "UVA",
        "ACEROLA",
        "CARAMBOLA",
        "GOIABA",
        "CAJU"
    ]

class Animais:
    palavras = [
        "LEAO",
        "ELEFANTE",
        "GIRASSOL",
        "PAPAGAIO",
        "GOLFINHO",
        "MACACO",
        "BORBOLETA",
        "JACARE",
        "PANDA",
        "TUCANO"
    ]

class Paises:
    palavras = [
        "BRASIL",
        "ESTADOS UNIDOS",
        "CANADA",
        "AUSTRALIA",
        "JAPAO",
        "ALEMANHA",
        "ITALIA",
        "INDIA",
        "ARGENTINA",
        "FRANCA"
    ]

class Profissoes:
    palavras = [
        "MEDICO",
        "ENGENHEIRO",
        "ADVOGADO",
        "PROFESSOR",
        "POLICIAL",
        "BOMBEIRO",
        "ARTISTA",
        "FARMACEUTICO",
        "ARQUITETO",
        "PROGRAMADOR"
    ]

def carrega_palavra_secreta(categoria):
    if categoria == "frutas":
        return random.choice(Frutas.palavras)
    elif categoria == "animais":
        return random.choice(Animais.palavras)
    elif categoria == "paises":
        return random.choice(Paises.palavras)
    elif categoria == "profissoes":
        return random.choice(Profissoes.palavras)
    else:
        raise ValueError("Categoria inválida. Escolha entre 'frutas', 'animais', 'paises' ou 'profissoes'.")

def letraInPalavra(letra, palavra):
    if letra in palavra:
        return True
    else:
        return False

def mostrarPalavraComLetra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def verificarFimDeJogo(palavra, letras_corretas):
    for letra in palavra:
        if letra not in letras_corretas:
            return False
    return True

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

