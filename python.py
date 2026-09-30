class Vendedor:
    def __init__(self, nome, vendas):
        self.nome = nome
        self.vendas = vendas

    def resgistrar_vendas(self, valor):
        self.vendas += valor

    def calcular_comissao(self):
        if self.vendas <= 1000:
            return self.vendas * 0.05
        elif self.vendas <= 5000:
            return self.vendas * 0.10
        else:
            return self.vendas * 0.15


vendedor1 = Vendedor("João", 2000)
vendedor1.resgistrar_vendas(3000)
comissao = vendedor1.calcular_comissao()
print(f"Vendedor: {vendedor1.nome}")
print(f"Comissão: {comissao}")