class ContaCorrente:
    def __init__(self, numero, saldo=0):
        self._numero = numero
        self._saldo = saldo

    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
      return self._numero

    def sacar(self, valor):
      self._saldo -= valor+2
      print('O valor foi debitado')

    def creditar(self, valor):
        self._saldo += valor
        print('O crédito foi efetuado')

  
    def debitar(self, valor):
        if valor < self._saldo:
            self._saldo -= valor
            print('O valor foi debitado')
        else:
            print('Não é possível debitar um valor menor do que o saldo existente')


    def transferir(self, valor, conta):
        if self._saldo >= valor:
            self._saldo -= valor
            conta._saldo += valor
            print(f'Valor transferido com sucesso. Você agora tem R${self._saldo}')
            print(f'A conta que foi efetuada o saque, agora possui R${conta._saldo}')
        else:
            print('Você não tem saldo suficiente')
  
    def __str__(self):
        return 'CONTA ==> '+ str(self._numero) + f' // saldo: R${self._saldo},00'

#Na classe ContaPoupança que é filha de ContaCorrente, reescreva o método sacar(self,valor). Este método cobra R$ 0,50 para
# cada saque efetuado a partir do 5º saque. Ou seja, Toda instancia de ContaPoupanca pode efetuar 4 saques sem cobrança de tarifa. 
#A partir do 5º saque, é debitado o valor do saque mais R$ 0,50. 

class ContaPoupanca(ContaCorrente):
  def __init__(self, numero, tx_juros, saldo=0):
    super().__init__(numero, saldo)
    self._tx_juros = tx_juros
    self._saques = 0
  
  @property
  def saques(self):
    return self._saques

  @property
  def tx_juros(self):
    return self._tx_juros
  
  def sacar(self, valor):
    self._saques += 1
    if self._saques > 4:
      self._saldo -= valor+0.50
      print('Saque efetuado com cobrança extra de 0,50 centavos')
    else:
      self._saldo -= valor
      print('Saque efetuado com sucesso')
      


  def render_juros(self):
    if self._saldo != 0:
      self._saldo += ((self._tx_juros/100)*self._saldo)
      print(f'O juros rendeu. Seu saldo agora é R${self._saldo},00')
    else:
      print('Impossível fazer o seu dinheiro render, invista primeiro!')

  def __str__(self):
    return super().__str__()+ f' // tx juros:{self._tx_juros}%' #AQUI COM O super(). CHAMO O __str__() da classe ContaCorrente


class ContaImposto(ContaCorrente):
  def __init__(self, numero, percentual_imposto, saldo=0):
    super().__init__(numero, saldo)
    self._percentual_imposto = percentual_imposto
  
  @property
  def percentual_imposto(self):
    return self._percentual_imposto
  
  
  def calcula_imposto(self):
    self._saldo -= self._saldo*(self._percentual_imposto/100)
    print(f'O valor do atual do saldo é {self._saldo}')

  def __str__(self):
    return super().__str__()+  '\n' f'O seu percentual de desconto foi de {self._percentual_imposto}%'


contalucas = ContaCorrente('01', 5000)

contakleber = ContaPoupanca('02', 5, 10000)

contakleber.sacar(1000)


contakleber.sacar(1000)
contakleber.sacar(1000)
contakleber.sacar(1000)
contakleber.sacar(1000)
print(contakleber.saldo)
