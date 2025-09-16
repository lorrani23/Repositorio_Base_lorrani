numero = int(input("digite um numero para fazer a tabuada? "))
numero_inicio = int(input("digite um numero de inicio: "))
numero_fim = int(input("digite um numero para terminar: "))
for i in range(1, 11):
    print(f" {i} x {numero} = {i * numero}")
