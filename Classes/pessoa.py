# snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe.
# Todas as letras serão minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.

# Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.

class Pessoa:

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