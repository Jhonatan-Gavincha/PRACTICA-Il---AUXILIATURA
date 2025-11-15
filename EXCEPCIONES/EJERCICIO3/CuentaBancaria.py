class FondosInsuficientesException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    # Depositar
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a cero")
        self.saldo += monto
        print(f"Depósito realizado: ${monto}. Saldo actual: ${self.saldo}")

    # Retirar
    def retirar(self, monto):
        if monto > self.saldo:
            raise FondosInsuficientesException(f"Fondos insuficientes. Saldo disponible: ${self.saldo}")
        self.saldo -= monto
        print(f"Retiro realizado: ${monto}. Saldo actual: ${self.saldo}")

    # Mostrar información
    def mostrar_info(self):
        print(f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: ${self.saldo}")
def main():
    # Crear cuenta
    cuenta = CuentaBancaria("12345", "Juan Pérez", 1000)
    cuenta.mostrar_info()
    
    print("\n--- Depósitos ---")
    # Depósito válido
    try:
        cuenta.depositar(500)
    except ValueError as e:
        print(e)
    
    # Depósito inválido
    try:
        cuenta.depositar(-200)
    except ValueError as e:
        print("Error:", e)
    
    print("\n--- Retiros ---")
    # Retiro válido
    try:
        cuenta.retirar(300)
    except FondosInsuficientesException as e:
        print("Error:", e)
    
    # Retiro que supera saldo
    try:
        cuenta.retirar(2000)
    except FondosInsuficientesException as e:
        print("Error:", e)

    print("\n--- Información final de la cuenta ---")
    cuenta.mostrar_info()


if __name__ == "__main__":
    main()
