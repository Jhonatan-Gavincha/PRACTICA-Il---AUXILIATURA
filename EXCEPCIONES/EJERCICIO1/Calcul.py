# Excepción personalizada
class NumeroInvalidoException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Clase Calculadora
class Calculadora:

    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ZeroDivisionError("Error: No se puede dividir entre cero")
        return a / b

    @staticmethod
    def convertir_a_entero(valor):
        try:
            return int(valor)
        except ValueError:
            raise NumeroInvalidoException(f"'{valor}' no es un número válido")


# -----------------------------
# Programa principal para probar
# -----------------------------
def main():
    print("=== Pruebas Calculadora ===\n")

    # Operaciones normales
    print("Suma 5 + 3 =", Calculadora.sumar(5, 3))
    print("Resta 10 - 7 =", Calculadora.restar(10, 7))
    print("Multiplicación 4 * 6 =", Calculadora.multiplicar(4, 6))

    # División con manejo de error
    try:
        print("División 10 / 0 =", Calculadora.dividir(10, 0))
    except ZeroDivisionError as e:
        print(e)

    # División correcta
    try:
        print("División 10 / 2 =", Calculadora.dividir(10, 2))
    except ZeroDivisionError as e:
        print(e)

    # Conversión a entero correcta
    try:
        num = Calculadora.convertir_a_entero("25")
        print("Conversión a entero de '25':", num)
    except NumeroInvalidoException as e:
        print(e)

    # Conversión a entero incorrecta
    try:
        num = Calculadora.convertir_a_entero("abc")
        print("Conversión a entero de 'abc':", num)
    except NumeroInvalidoException as e:
        print(e)


if __name__ == "__main__":
    main()
