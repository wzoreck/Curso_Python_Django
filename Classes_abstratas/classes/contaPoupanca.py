from classes.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente')
            return
        self._saldo -= valor
        print(f'Saldo: {self._saldo}')
    