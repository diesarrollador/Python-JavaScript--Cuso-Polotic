#Escribe un programa en Python que reciba 5 números enteros del usuario y los guarde en una lista.
#Luego recorrer la lista y mostrar los números por pantalla.

numeros = []
for i in range(5):
    numeros.append(int(input(f"Ingrese numero {i+1}: ")))
print(numeros)