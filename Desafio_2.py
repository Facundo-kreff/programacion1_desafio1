#2
hora = int(input("Ingrese Hora actual: "))
horas_futuras = int(input("Ingrese Horas:"))
hora += horas_futuras
actual = hora % 12
if actual == 0:
    print("En ",horas_futuras," el reloj marcara las", 12)
else:
    print("En",horas_futuras,"el reloj marcara las", actual)

