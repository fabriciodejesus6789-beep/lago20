
"""
testando o git
"""

"""

Questão 1

A maquina esta sorteando um numero entre 1 e 100 usando random o usuario continua ate acertar
a cada erro o programa informa se o numero secreto é maior ou menor.

"""

"""
Questão 2
import random

senha = random.randint(1, 10)

tentativas = 0
acertou = False

while tentativas < 3:

    palpite = int(input("Digite a senha do cofre (1 a 10): "))

    tentativas += 1

    if palpite == senha:
        print("Cofre desbloqueado!")
        acertou = True
        break

    else:
        print("Senha incorreta!")

        if tentativas < 3:

            if senha > palpite:
                print("Dica: a senha é MAIOR que o número digitado.")
            else:
                print("Dica: a senha é MENOR que o número digitado.")

        else:
            print("Você não possui mais tentativas.")

if not acertou:
    print("COFRE BLOQUEADO!")


    """

"""
Questão 3

salario = float(input("Digite o salário do funcionário: R$ "))

reajuste = salario * 0.15

novo_salario = salario + reajuste

print(f"Salário antigo: R$ {salario:.2f}")
print(f"Valor do reajuste: R$ {reajuste:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

"""

"""
QUESTÃO 4

a = 9.81
vi = 0
xi = 0

t = float(input("Digite o tempo de queda em segundos: "))

x = 0.5 * a * (t ** 2) + vi * t + xi

print(f"A altura da queda é: {x:.2f} metros")

"""

"""
Questão 5

n = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
contador = 1

while contador <= n:

    fatorial = fatorial * contador

    contador += 1

print(f"{n}! = {fatorial}")


"""

"""
Questão 6

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


print("===== CALCULADORA =====")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Escolha uma opção: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:

    resultado = somar(num1, num2)
    print(f"Resultado: {resultado}")

elif opcao == 2:

    resultado = subtrair(num1, num2)
    print(f"Resultado: {resultado}")

elif opcao == 3:

    resultado = multiplicar(num1, num2)
    print(f"Resultado: {resultado}")

elif opcao == 4:

    if num2 != 0:
        resultado = dividir(num1, num2)
        print(f"Resultado: {resultado}")
    else:
        print("Não é possível dividir por zero.")

else:
    print("Opção inválida.")

"""

"""
Questão 7

def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    anterior = 0
    atual = 1

    contador = 2

    while contador <= n:

        proximo = anterior + atual

        anterior = atual
        atual = proximo

        contador += 1

    return atual

def soma_ate_n(n):

    soma = 0

    for i in range(n + 1):
        soma += fibonacci(i)

    return soma

def soma_x_ate_y(x, y):

    soma = 0

    for i in range(x, y + 1):
        soma += fibonacci(i)

    return soma

# Testando a função Fibonacci
n = int(input("Digite o elemento n da sequência: "))

print(f"Elemento {n} da sequência: {fibonacci(n)}")

# Testando o somatório até n
print(f"Somatório até o elemento {n}: {soma_ate_n(n)}")

# Testando o somatório entre x e y
x = int(input("Digite o elemento inicial x: "))
y = int(input("Digite o elemento final y: "))

print(f"Somatório de {x} até {y}: {soma_x_ate_y(x, y)}")

"""

"""
Questão 8

numero = int(input("Digite um número inteiro positivo: "))

if numero % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é ÍMPAR.")

"""

"""
Questão 9

def analisar_numeros():

    n = int(input("Quantos números serão digitados? "))

    quantidade_impares = 0

    for i in range(n):

        numero = int(input(f"Digite o {i + 1}º número: "))

        if numero % 2 != 0:
            quantidade_impares += 1

    percentual = (quantidade_impares / n) * 100

    print(f"Quantidade de números ímpares: {quantidade_impares}")
    print(f"Percentual de números ímpares: {percentual:.2f}%")


analisar_numeros()

"""

"""
Questão 10

import random

def analisar_numeros():

    n = int(input("Quantos números serão gerados? "))

    quantidade_impares = 0

    for i in range(n):

        numero = random.randint(0, 1000)

        print(f"Número {i + 1}: {numero}")

        if numero % 2 != 0:
            quantidade_impares += 1

    percentual = (quantidade_impares / n) * 100

    print()
    print(f"Quantidade de números ímpares: {quantidade_impares}")
    print(f"Percentual de números ímpares: {percentual:.2f}%")

analisar_numeros()
"""
