#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance.
# Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros
class CuentaBancaria:

    def __init__(self, numero_cuenta, cliente, balance=10000, estado=True):
        self.numero = numero_cuenta
        self.cliente = cliente
        self.balance = balance
        self.estado = estado

    def depositar(self, cantidad):
        """
        Deposita cierta cantidad de dinero en la cuenta.

        :cantidad: Cantidad de dinero a depositar.
        """
        if self.estado and cantidad > 0:
            self.balance += cantidad

    def retirar(self, cantidad):
        """
        Retira cierta cantidad de dinero.

        :cantidad: Cantidad de dinero a retirar.
        """
        if self.estado and cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad

    def cerrar_cuenta(self):
        """
        Cierra la cuenta bancaria.
        """
        self.estado = False