"""
Modificadores de visibilidade:
 public, protected, private

    # Antes do nome do atributo
     _nome_atributo = protected # É possível acessar o atributo (este é meio confuso é protect/private mas na vdd é public com um _ antes)
     __nome_atributo = private

    No python temos apenas os atributos private e public, por convenção colocamos 1 ou 2 underlines antes do
    nome do atributo para informar se é protected ou private, 1 underline para informar que é protected e 2
    para informar que é private, mas nada impede que sejam acessados como os públicos os protected,
    já o private realmente impede, "Um programador python deve saber o que faz"

    ESSA FILOSOFIA SERVE TANTO PARA ATRIBUTO QUANTO PARA MÉTODOS!!!
"""

class Carro:

    def __init__(self):
        self.__cores = {}

    @property
    def cores(self):
        return self.__cores

    @cores.setter
    def cores(self, msg): # Feito errado de propósito
        self.__cores = msg

    def inserir_cor(self, id, cor):
        # Na primeira vez será criado o dicionario nas outras vezes será atualizado
        if 'cores' not in self.__cores:
            self.__cores['cores'] = {id: cor}
        else:
            self.__cores['cores'].update({id: cor})
    
    def listar_cores(self):
        for id, cor in self.__cores['cores'].items():
            print(id, cor)

    def deletar_cor(self, id):
        del self.__cores['cores'][id]

# MAIN
fusca = Carro()
fusca.inserir_cor(1, 'Preto')
fusca.inserir_cor(2, 'Azul')
fusca.inserir_cor(3, 'Branco')
fusca.inserir_cor(4, 'Verde')
fusca.deletar_cor(4)
# print(fusca.cores)
print('Cores disponíveis:')
fusca.listar_cores()

# __private
# Não será possível pois o private impede, será criado um novo atributo para armazenar esse valor
fusca.__cores = 'Tentando quebrar o código' 
print()
fusca.listar_cores()
print(fusca.__cores) # Atributo criado
print(fusca._Carro__cores) # Atributo original

# Testando getters e setters
print()
print(fusca.cores)
fusca.cores = 'Sobreescreveu o dicionário'
print(fusca.cores)
fusca.listar_cores() # Vai dar esso neste pois o dicionário foi sobreescrito