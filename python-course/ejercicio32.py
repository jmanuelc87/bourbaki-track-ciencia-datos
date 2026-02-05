a = input("Dame un numero: ")

a = int(a)
if a > 0:
    for i in range(1, a + 1):
        print(f"{i}", end=" ")
    print()
elif a < 0:
    while a <= 0:
        print(f"{a}", end=" ")
        a += 1
else:
    print("Ingresaste el numero cero")