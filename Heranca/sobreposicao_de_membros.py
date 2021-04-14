class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print('Pessoa está falando')
    
class Aluno(Pessoa):
    # Sobreposição do metodo construtor
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    # Sobreposição/sobreescrita do metodo falar
    def falar(self):
        print('Aluno está falando')
    
    def apresentar(self):
        print(f'Aluno {self.nome} matricula {self.matricula}')

# MAIN
p1 = Pessoa('Joao', 20)
a1 = Aluno('Daniel', 20, '123456789')
p1.falar()
a1.falar()
a1.apresentar()
