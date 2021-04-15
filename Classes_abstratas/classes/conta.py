from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

        @property
        def agencia(self):
            return self._agencia
        
        @property
        def numero(self):
            return self._numero
        
        @property
        def saldo(self):
            return self._saldo
        
        @saldo.setter
        def saldo(self, saldo):
            if not isinstance(saldo, (int, float)):
                raise ValueError("Não é um número")
            self._saldo = saldo

        def depositar(self, valor):
            if not isinstance(valor, (int, float)):
                raise ValueError("Não é um número")
            self._saldo += valor

        def ver_saldo(self):
            print(f'O saldo é {self._saldo}')

        # Não será implementado aqui somente para forçar que as classes especializadas (Filhas) tenham o metodo
        @abstractmethod
        def sacar(self, valor):
            pass
