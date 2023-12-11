#define a soma e subtração de a e b

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

## 1 - Faça uma função de multiplicação de
##     dois números inteiros usando apenas soma

def multiplicacao(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado

## 2 - Faça uma função de exponenciação de
##     dois números inteiros usando a função acima.

def exponenciacao(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado = multiplicacao(resultado, base)
    return resultado


## 3 - Faça uma função de divisão inteira de
##     dois números inteiros usando só subtração.


def divisao_inteira(dividendo, divisor):
    quociente = 0
    while dividendo >= divisor:
        dividendo = subtracao(dividendo, divisor)
        quociente = soma(quociente, 1)
    return quociente

## 4 - Faça uma função de resto de uma divisão inteira de
##     dois números inteiros usando só subtração.

def resto(dividendo, divisor):
    while dividendo >= divisor:
        dividendo = subtracao(dividendo, divisor)
    return dividendo

## 5 - Um botânico dedicou-se, durante anos de estudos, a conseguir
##     criar uma função exponencial que medisse o crescimento dos
##     pinheiros no decorrer do tempo. Sua conclusão foi que, ao
##     plantar-se essa árvore, seu crescimento em centímetros, no
##     decorrer dos anos, é dado por C(t) = 5 x 2^(t – 1).  Faça um
##     programa que leia t (número de anos) e mostre qual o tamanho
##     esperado de um pinheiro em centímetros.  Use apenas as funções
##     criadas anteriormente.

print("\n================================")

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

## 6 - Faça um programa que leia um número de segundos e mostre o
##     equivalente em horas, minutos e segundos. Ex.: 7321 ->
##     02h02m01s. Use apenas as funções anteriormente.

print("\n================================")

def divisao_inteira(dividendo, divisor):
    quociente = 0
    while dividendo >= divisor:
        dividendo = subtracao(dividendo, divisor)
        quociente = soma(quociente, 1)
    return quociente

def resto(dividendo, divisor):
    while dividendo >= divisor:
        dividendo = subtracao(dividendo, divisor)
    return dividendo

segundos = int(input("Digite o número de segundos: "))
horas = divisao_inteira(segundos, 3600)
segundos_restantes = resto(segundos, 3600)
minutos = divisao_inteira(segundos_restantes, 60)
segundos_final = resto(segundos_restantes, 60)

print(f"{horas:02}h{minutos:02}m{segundos_final:02}s")

