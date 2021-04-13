class Aluno:
    def __init__(self, nome, sexo):
        self.__nome = nome
        self.__sexo = sexo
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @ property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

class Curso:
    def __init__(self, nome, aluno):
        self.__nome = nome
        self.__aluno = aluno
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def aluno(self):
        return self.__aluno
    
    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno
    
    def mostrar_aluno(self):
        print(f'O aluno {self.__aluno.nome} está cadastrado no curso {self.__nome}')

# MAIN
a1 = Aluno('Daniel', 'Masculino')
a1.nome = 'Daniel Wzoreck'
print(a1.nome, a1.sexo)
c1 = Curso('ADS', a1)
c1.mostrar_aluno()