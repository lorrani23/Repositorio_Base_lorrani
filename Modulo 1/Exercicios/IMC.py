nome = input("qual o seu nome?")
peso = float(input("qual o seu peso ?"))
altura = float(input("qual a sua altura?"))

IMC = peso/(altura*altura)
if IMC <=18.5:
    print("abaixo do peso")
elif IMC <=29.9:
    print("peso normal") 
elif IMC <=34.9:
    print("obesidade grau 1")
elif IMC <= 39.9:
    print("obesidade grau 2")

else:
    print("obesidade grau 3(morbida)")   
