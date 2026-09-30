"""
nome = "Alice"
idade = 30
print("Nome: ", nome)
print("Idade: ", idade) 
"""
"""
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Nome: {nome}, Idade: {idade}")

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

print("Digite um nuemro para verificar se é ára ou impar")
numero = int(input("Digite um numero: "))
if numero %2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")
"""
"""
fruta = input("Digite o nome de uma fruta: ").strip().capitalize()

match fruta:
    case "Banana":
        print("Torta de banana")
    case "Maçã":
        print("Torta de maçã")
    case "Abacaxi":
        print("Suco de abacaxi")
"""

from classes import Vendedor


vendedor1 = Vendedor("Lira")
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

vendedor2 = Vendedor("João")
vendedor2.vendeu(500)
vendedor2.bateu_meta(600)   

print(f"Vendas do {vendedor1.nome}: {vendedor1.vendas}")
print(f"Vendas do {vendedor2.nome}: {vendedor2.vendas}")