#6 triangulo 
renglones = int(input("Ingrese cantidad de renglones: "))
j=0
lista = []
while j < renglones:
    a = (j+1)*2
    lista.append(a)
    print("".join(str(lista)))
    j+=1 