# Escribí un programa que solicite al usuario una letra y,
# si es una vocal, muestre el mensaje “Es vocal”.
# Verificar si el usuario ingresó un string de más de un carácter y,
# en ese caso, informarle que no se puede procesar el dato.

letra = input("Letra")

if (len(letra)!=1):
    print("No se puede procesar el dato")
else:
    if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
        print("La letra ingresada es una vocal")
    else:
        print("La letra ingresada no es una vocal")
        
