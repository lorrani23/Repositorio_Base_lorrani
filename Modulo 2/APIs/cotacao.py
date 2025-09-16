def dolar_para_real (dolar):
    cotaçao = 5.30 #exemplo de cotaçao
    return dolar * cotaçao 
def real_para_dolar(real):
    cotaçao  = 5.30 #exemplo de cotaçao 
    return real / cotaçao 
#menu interativo
print("conversor de moedas")
print("[1] - converter dolar para real ")
print("[2] - converter real para dolar ")
opçao = int (input("escolha a opçao:"))
if opçao == 1:
    valor = float(input("digite o valor em dolar: $ "))

    dolar_para_real(valor)
print = float(input("digite o valor em real: $"))
