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
