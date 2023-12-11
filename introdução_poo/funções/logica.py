## 5 - Um botânico dedicou-se, durante anos de estudos, a conseguir
##     criar uma função exponencial que medisse o crescimento dos
##     pinheiros no decorrer do tempo. Sua conclusão foi que, ao
##     plantar-se essa árvore, seu crescimento em centímetros, no
##     decorrer dos anos, é dado por C(t) = 5 x 2^(t – 1).  Faça um
##     programa que leia t (número de anos) e mostre qual o tamanho
##     esperado de um pinheiro em centímetros.  Use apenas as funções
##     criadas anteriormente.

import functions

def exponenciacao(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado = multiplicacao(resultado, base)
    return resultado

def tamanho_pinheiro_em_cm(anos):
    crescimento = exponenciacao(2, anos - 1)
    tamanho = multiplicacao(5, crescimento)
    return tamanho

anos = int(input("Digite o número de anos: "))
tamanho_esperado = tamanho_pinheiro_em_cm(anos)
print("O tamanho esperado do pinheiro em centímetros é:", tamanho_esperado)

