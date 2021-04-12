from pessoa import Pessoa
from metodos_estaticos import MetodosEstaticos

p1 = Pessoa('Daniel', 20)
p1.falar()
p1.pular()
p1.pular(True)

# Acessando o atributo da classe Pessoa
print(Pessoa.ano_atual)

p2 = Pessoa.criar_pessoa_por_ano_de_nascimento('Joao', 1990)
print(f'{p2.nome} foi criado com {p2.idade} anos, conforme o metodo de classe')

# Metodo estático, não é necessário uma instância de MetodosEstaticos
print(f'{MetodosEstaticos.mtd_estatico()} - chamado sem uma instância')

# mas nada impede que o metodo estático seja chamado através de uma instância 
mtd_est = MetodosEstaticos(10, 20)
print(f'{mtd_est.mtd_estatico()} - chamado a partir de uma instância')