# snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe.
# Todas as letras serão minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.

# Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.

class Pessoa:

    # Atributo público da classe Pessoa, não é necessário uma instância para ser acessado
    ano_atual = 2021

    # Metodo construtor
    def __init__(self, nome, idade):
        # Os que iniciam com self. se tornam atributos da classe pessoa
        self.nome = nome
        self.idade = idade

        # Caso não tenha o self. será apenas uma variável interna do metodo
        exemplo = 'Variável interna de Pessoa'
        print(exemplo)


    
    def falar(self):
        print(f'{self.nome} está falando')
    

    # É possivel definir valores padrões passagens por parametro, neste caso:
    # se não for passado nada para 'sentado' estão seu valor será False
    def pular(self, sentado = False):
        if (sentado != False):
            print(f'{self.nome} pulou')
        else:
            print(f'{self.nome} não pode pular pois está sentado')
    

    # Metodos de classe são métos proprios da classe que podem ser usados sem uma instância,
    # chamando apenas o nome da classe e o metodo
    @classmethod # Utilizamos essa notação conehcida como decorator para definir que o método será de classe
    def criar_pessoa_por_ano_de_nascimento(cls, nome, ano_nascimento): # Ao inves de self criamos uma variável de nome qualquer para nos referirmos a classe
        # Como esse metodo não tem o self, somente teremos acesso a variável de classe que no caso é ano_atual
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade) # cls refre-se a classe Pessoa, é igual Pessoa(nome, idade)