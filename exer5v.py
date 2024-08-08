tabuada = int(input("digite a tabuada q deseja:"))

resultado = 0

for num in range(1, 10 + 1,1):
    resultado = tabuada * num

    print(f"{tabuada} X {num} = {resultado}")
