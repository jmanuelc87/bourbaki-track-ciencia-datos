a = input("Dame el primer numero: ")
b = input("Dame el segundo numero: ")

try:
    a = int(a)
    b = int(b)
    
    if a == b:
        print("Los numeros son iguales")
    
    if a < 0 and b < 0:
        raise Exception("Los numeros son negativos")
    
    c = list(range(1,6))
    for i in [a, b]:
        if i in c:
            print(f"El numero {i} se encuentra dentro de {c}")
except Exception as e:
    print(f"Error: {e}")
    


    