class MetodosEstaticos:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    

    # Metodos estáticos, não precisa nem de uma instância nem da classe
    # funciona com uma função qualquer fora de classes, porem por uma questão de organização precisa estar dentro de uma classe
    @staticmethod
    def mtd_estatico(): # Pode receber parametros, porem não recebe referência nem da instância (self) nem da classe (exemplo cls)
        msg = 'Este é um metodo estático'
        return msg