
#3 numeros primos
num=int(input("ingrese numero: "))
if num < 4 and num > 0: #filtra a 1 2 y 3 como primos
    print("el numero", num, "es primo")
elif num%2 == 0: #descarta numeros divididos por 2
    print("el numero", num, "no es primo")
else :
    i=0
    while i < num: #ciclo que recore todas las posibles diviciones de numeros menores al de la consulta          
        if num%(i+1) == 0 and i!=0 and i+1 != num: # si se divide por alguno se corta ciclo y muestrea en pantalla que no es primo
            print("el numero", num, "no es primo")
            i += num
        elif i+1 == num: #si la anterior condicion no resulta se confirma que es primo
            print("el numero", num, "es primo")
        i+=1
