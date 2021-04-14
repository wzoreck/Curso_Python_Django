class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__
    
    def apresentar_pessoa(self):
        print(f'O {self.nome_classe} chamado {self.nome} está falando')
    
# Através do () ao lado do nome da classe informamos a classe generalizada para fazermos a especialização
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando')

# MAIN
p1 = Pessoa('Joao', 20)
p1.apresentar_pessoa()
a1 = Aluno('Daniel', 20)
a1.apresentar_pessoa()
a1.estudar()