multiplicacao = int(input("Digite um número? "))
resultado = 0

print(f"--A tabuada deste número é {multiplicacao}--")
for i in range(1, 11):
    resultado = multiplicacao * i
    print(f"{multiplicacao} x {i} = {resultado}")