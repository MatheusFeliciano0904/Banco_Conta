class Conta:
    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            return True

    def extrato(self):
        print(f"Número: {self._numero}\nSaldo: R$ {self._saldo:.2f}")

    def transfere_para(self, destino, valor):
        if self.saca(valor):
            destino.deposita(valor)
            return True
        return False

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

    def __str__(self):
        return f"Número: {self._numero}, Titular: {self._titular}, Saldo: R$ {self._saldo:.2f}"


class ContaCorrente(Conta):
    def atualiza(self, taxa):
        super().atualiza(taxa * 2)

    def deposita(self, valor):
        if valor > 0:
            self._saldo += valor - 0.10


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        super().atualiza(taxa * 3)


class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5 + 50


class AtualizadorDeContas:
    def __init__(self, selic):
        self._selic = selic
        self._saldo_total = 0

    def roda(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("O objeto passado não é uma conta válida.")
        
        saldo_anterior = conta._saldo
        print(f"Conta: {conta._numero}")
        print(f"Saldo Anterior: R$ {saldo_anterior:.2f}")

        conta.atualiza(self._selic)
        saldo_novo = conta._saldo

        print(f"Saldo Atualizado: R$ {saldo_novo:.2f}\n")

        self._saldo_total += saldo_novo

    def get_saldo_total(self):
        return self._saldo_total


class Banco:
    def __init__(self):
        self._contas = []

    def adiciona(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("Apenas objetos do tipo Conta podem ser adicionados.")
        self._contas.append(conta)

    def pegaConta(self, posicao):
        return self._contas[posicao]

    def pegaTotalDeContas(self):
        return len(self._contas)

    def listar_contas(self):
        for conta in self._contas:
            print(conta)


if __name__ == '__main__':
    
    c = Conta("123-4", "João", 1000.0)
    cc = ContaCorrente("134-8", "Matheus", 2500.00)
    cp = ContaPoupanca("324-9", "Maria", 2000.00)
    ci = ContaInvestimento("555-7", "Lucas", 5000.00)

    banco = Banco()
    banco.adiciona(c)
    banco.adiciona(cc)
    banco.adiciona(cp)
    banco.adiciona(ci)
    
    atualizador = AtualizadorDeContas(0.01)
    
    for i in range(banco.pegaTotalDeContas()):
        atualizador.roda(banco.pegaConta(i))

    print(f"Saldo Total Acumulado: R$ {atualizador.get_saldo_total():.2f}")
