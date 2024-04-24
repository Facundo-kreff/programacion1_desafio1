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
