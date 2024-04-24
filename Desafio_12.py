#12 Torneo de Tenis.
tenistas = []
for i in range (8):
    tenistas.append(input("Jugador "+ str(1+i)+": "))
ganadores=[]
i = 0
while i < len(tenistas) and len(tenistas) != 1: 
    if len(tenistas) > 4:
        if i == 0:
            print("\nRonda 1")
        partida = input("a." + str(tenistas[i] + " - b." + str(tenistas[i+1])+ ": "))
        if partida == "b":
            tenistas.remove(tenistas[i])
            i+=1
            if i == 4:
                i=0
        else:
            tenistas.remove(tenistas[i+1])
            i+=1
            if i == 4:
                i=0
    elif len(tenistas) > 2:
        if i == 0:
            print("\nRonda 2")
        partida = input("a." + str(tenistas[i] + " - b." + str(tenistas[i+1])+ ": "))
        if partida == "b":
            tenistas.remove(tenistas[i])
            i+=1
            if i == 2:
                i=0
        else:
            tenistas.remove(tenistas[i+1])
            i+=1
            if i == 2:
                i=0
    else:
        if i == 0:
            print("\nRonda 3")
        partida = input("a." + str(tenistas[i] + " - b." + str(tenistas[i+1])+ ": "))
        if partida == "b":
            tenistas.remove(tenistas[i])
        else:
            tenistas.remove(tenistas[i+1])
print("\n\nCampeon:", tenistas[0])