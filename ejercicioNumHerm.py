
n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

suma_divisores_n1 = 0
for i in range(1, n1):
    if n1 % i == 0:
        suma_divisores_n1 += i

suma_divisores_n2 = 0
for j in range(1, n2):
    if n2 % j == 0:
        suma_divisores_n2 += j

if suma_divisores_n1 == n2 and suma_divisores_n2 == n1:
    print(f"{n1} y {n2} son números hermanos")
else:
    print(f"{n1} y {n2} no son números hermanos")
