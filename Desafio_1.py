#desafio 1

"""
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
        i+=1"""


"""
#4 Tiempo de viaje
tiempo = 0
tramos = 0
while tramos != 1: #ciclo para el ingreso de tiempo
    ingreso_tiempo= int(input("Duracion de tramo: "))
    tiempo += ingreso_tiempo # sumador de tiempo de tramos
    if ingreso_tiempo == 0: #comdicional para salir de ciclo
        tramos = 1

horas = tiempo//60 #hora
minutos = tiempo%60 #Minutos
print("Tiempo total de viaje: " + str(horas) +  ":" + str(minutos) + " horas") #imprecion en pantalla
"""

"""
#5 Año Bisiesto
año = int(input("Ingrese el Año a evaluar: ")) #ingreso año  
if año%4 == 0 and año%400 != 0: #si se divide por 4 pero no por 400 es bisiesto
    print("El Año " + str(año) + " es bisiesto")
else:
    print("El Año " + str(año) + " NO es bisiesto")
"""

'''
#6 triangulo 
renglones = int(input("Ingrese cantidad de renglones: "))
j=0
lista = []
while j < renglones:
    a = (j+1)*2
    lista.append(a)
    print("".join(str(lista)))
    j+=1 '''

'''
#7 secuencia de Collatz 
collat = int(input("ingrese un numero: "))
coleccione_collat = [collat]
while collat > 1 or collat < 0:
    if collat%2 == 0:
        collat//=2
        coleccione_collat.append(collat)
    else:
        collat = (collat*3) + 1
        coleccione_collat.append(collat)
print(coleccione_collat)
'''

'''
#8 cambio
eleccion = input("Elija producto: ")
if eleccion == 'A':
    eleccion = 270
elif eleccion == 'B':
    eleccion = 340
else:
    eleccion = 390
monedas = 0
while monedas < eleccion:
    monedas+=int(input("Ingrese Monedas: "))
diferencia = monedas - eleccion
print("Su vuelto:")
while diferencia > 0:
    if diferencia > 100:
        diferencia-=100
        print(100)
    elif diferencia > 50:
        diferencia-=50
        print(50)
    else:
        diferencia-=10
        print(10)
'''

'''
#9 anagrama
palabra1 = input("Ingrese palabra1: ")
palabra2 = input("Ingrese palabra2: ")
if palabra1 == palabra2 or len(palabra1) != len(palabra2): #cortar programa si la palabra no tiene la misma cantidad de letras o es la misma palabra
    print(False)
else:
    contador_palabras = 0
    i = 0
    while i < len(palabra1): #ciclo para valuar letra por letra y sumarlo a un contador
        j = 0
        while j < len(palabra2):
            if palabra1[i] == palabra2[j]:
                contador_palabras += 1
                j+=len(palabra2)
            j+=1
        i+=1
    if contador_palabras == len(palabra1): # si la palbra y el contador son iguales es true
        print(True)
    else:
        print(False)
'''

#10 


