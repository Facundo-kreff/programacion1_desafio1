#5 Año Bisiesto
año = int(input("Ingrese el Año a evaluar: ")) #ingreso año  
if año%4 == 0 and año%400 != 0: #si se divide por 4 pero no por 400 es bisiesto
    print("El Año " + str(año) + " es bisiesto")
else:
    print("El Año " + str(año) + " NO es bisiesto")
