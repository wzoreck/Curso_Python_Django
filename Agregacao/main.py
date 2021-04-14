# Exemplo de agragação, CarrinhoDeCompras pode existir sem nemnhum produto,
# mas produto agreaga ele, sem produtos não funciona corretamente
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = [] # Lista
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def lista_produtos(self):
        for p in self.produtos:
            print(p.nome, p.valor)
    
    def soma_total(self):
        total = 0
        for p in self.produtos:
            total += p.valor

        return total 

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


# MAIN
p1 = Produto('Sabonete', 1.5)
p2 = Produto('Pasta de dente', 4.75)
p3 = Produto('Desodorante', 8.80)

c1 = CarrinhoDeCompras()
c1.inserir_produto(p1)
c1.inserir_produto(p2)
c1.inserir_produto(p3)

c1.lista_produtos()
print(f'O valor total do carrinho é {c1.soma_total()}')