
def verificar_edad(edad):
    if edad < 0 or edad > 150:
        raise Exception(f"Error: la edad debe estar en el rango 0..150 años")

def verificar_numero(num):
    if num < 0:
        raise Exception(f"Error: el numero es negativo")

def dividir(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print("Error: Error no se puede dividir entre cero")