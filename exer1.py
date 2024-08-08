n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n2 < 101:
    for i in range(n1, n2, 1):
        print(i+1)

else:
    print("Número muito grande")