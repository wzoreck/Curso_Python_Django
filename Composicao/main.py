# Exemplo de composição, endereços compoêm clientes,
# sempre que um cliente for deletado todos os endereços que pertencem a ele serão deletados

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    
    def lista_enderecos(self):
        for e in self.enderecos:
            print(e.cidade, e.estado)

    def __del__(self):
        print(f'{self.nome} foi apagado')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade} | {self.estado} foi apagado')

# MAIN
c1 = Cliente('Daniel', 20)
c1.insere_endereco('Canoinhas', 'SC')
c1.insere_endereco('Três Barras', 'SC')
c1.insere_endereco('Curitiba', 'PR')

print(c1.nome)
c1.lista_enderecos()

c2 = Cliente('Maria', 18)
c2.insere_endereco('Porto União', 'SC')
c2.insere_endereco('Tubarão', 'SC')
c2.insere_endereco('Orleans', 'SC')

print()
print(c2.nome)
c2.lista_enderecos()
print()
del c2 # Se for deletado aqui o objeto não aparecerá abaixo pois o garbageCollector não precisá deletar

print()
print('###################################')
print('Demonstração do GarbageCollector do Pyhon removendo objetos não utilizados mais,')
print('a função __del__ é executada por ele quando se quer apresentar algo')
print()