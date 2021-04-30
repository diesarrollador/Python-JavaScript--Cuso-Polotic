#Escribe un programa en Python que acepte una cadena de caracteres y cuente el tamaño de la
#cadena y cuantas veces aparece la letra A ( mayuscula y minúscula)

cadena = str(input("Ingrese una cadena de carácteres: ")).lower()
cadena2 = cadena.replace(" ", "")
print("La cadena tiene: {} carácteres y la 'a' se repite: {} vez/veces.".format(len(cadena2), cadena2.count('a')))