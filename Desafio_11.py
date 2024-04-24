#11 piedra papel y tijera
puntosA = 0
puntosB = 0
while puntosA != 3 and puntosB != 3:
    jugadorA = input("A: ").lower()
    jugadorB = input("B: ").lower()
    if jugadorA == "tijera":
        if jugadorB == "papel":
            puntosA+=1
        elif jugadorB == "piedra":
            puntosB+=1
    elif jugadorA == "piedra":
        if jugadorB == "tijera":
            puntosA+=1
        elif jugadorB == "papel":
            puntosB+=1 
    elif jugadorA == "papel":
        if jugadorB == "piedra":
            puntosA+=1
        elif jugadorB == "tijera":
            puntosB+=1
    print(puntosA, "-", puntosB)
    if puntosA == 3:
        print("A es el ganador")
    elif puntosB == 3:
        print("B es el ganador")
