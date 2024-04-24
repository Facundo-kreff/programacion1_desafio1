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
