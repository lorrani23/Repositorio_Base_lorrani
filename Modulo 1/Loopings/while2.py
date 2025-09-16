while True:
    numero = int(input("digite um numero inteiro:"))
    if numero % 2 == 0:
        print("o numero é PAR. :")
    else:
        print("o numero é IMPAR. : ")
repetir = input("deseja verificar outro numero? (s para sim): ")
if repetir.lower() != "S":
    print("progresso encerrado")
