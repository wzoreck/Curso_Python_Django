# Exemplo de getters e setters
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
    


    # Em toda parte da classe onde for se obter ou setar um valor, automaticamente chamará sempre os getters e setters definidos
    # como exemplo, no metodo construtor o preco recebera o valor do retorno da função preco decorada com @preco.setter 

    # Getter - por convenção coloca-se um _ antes do nome do atributo para evitar erro de loop no python
    @property
    def preco(self):
        return self._preco
    
    # Setter - è necessário criar em ordem o getter e setter para os atributos, se misturar a ordem não funciona
    @preco.setter
    def preco(self, valor):
        print('Passou pelo setter do atributo preco')
        self._preco = valor


# Main
produto1 = Produto('Camiseta', 50)
produto1.desconto(10)
print(f'O preço do produto {produto1.nome} com desconto ficou {produto1.preco}')