#desafio 1

#3 numeros primos
num=int(input("ingrese numero: "))
if num < 4 and num > 0 or (num%2) == 0 :
    print("el numero", num, "es primo")
else :
    print("el numero", num, "no es primo")