#9 Anagrama
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
