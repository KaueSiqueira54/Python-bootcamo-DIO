from abc import ABC, abstractclassmethod, abstractproperty


class Conta():
    def __init__(self, _saldo, _numero, _agencia, _cliente, _historico):
        self._saldo = _saldo
        self._numero = _numero
        self._agencia = _agencia
        self._cliente = _cliente
        self._historico = _historico

class Cliente():
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente()):
    def __init__(self, _cpf, _nome, _data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = _cpf
        self._nome = _nome
        self._data_nascimento = _data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("OPERAÇÃO INVÁLIDA!")
            print("SALDO INSUFICIENTE!")

        elif valor > 0:
            self._saldo -= valor
            print("SALDO REALIZADO COM SUCESSO!")
            return True

        else:
            print("VALOR INVÁLIDO PARA SAQUE! ")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("DEPÓSITO REALIZADO COM SUCESSO!")
            return True
        else:
            print("OPERAÇÃO INVÁLIDA!")
            print("VALOR INFORMADO É INVÁLIDO!")
            return False
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] = Saque.__name]
        )

        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saques > self.limite_saque

        if excedeu_limite:
            print("O VALOR A SER SACADO EXCEDE O LIMITE!")

        elif excedeu_saque:
            print("O NÚMERO MÁXIMO DE SAQUES EXCEDIDO!")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""
            Agencia = {self.agencia}
            Conta/c = {self.numero}
            Titular = {self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicioanar_transacao(self, transacao):
        self.transacoes.append(
            {
                "Tipo":transacao.__class__.__name__,
                "valor": transacao.valor
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        
class Depositar(Transacao):
    def __init__(self, _valor):
        self._valor = _valor

    @property
    def valor(self):
        return self.valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
