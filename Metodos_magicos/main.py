class A:
    # Esses dois metodos juntos podem ser chamados de "construtor da classe", pois __new__ é executado antes de __init__ 
    
    # Se o metodo __new__ for sobreescrito e não for adicionado um comportamento a ele não realizará nada ao criar objetos
    # é necessário adicionar um comportamento a ele 
    def __new__(cls, *args, **kwargs):
        """
        Aqui podemos fazer coisas mais avançadas como:
            - Criar atributos de classe;
            - criar metodos que possam ser usados como atributos
        """
        def falar_oi(*args, **kwargs):
            print('Oi')
        
        # Atributo de classe
        cls.falar_oi = falar_oi

        print('Novo')
        #pass
        # Aqui estamos utilizando o método super() sem informar que A é uma especialização de alguma classe
        # isso ocorre pois toda classe é filha de Object em Python
        return super().__new__(cls) # Mesma coisa que -> object.__new__(cls) 

    def __init__(self):
        print('Inicializou')


# MAIN
a = A()
a.falar_oi()