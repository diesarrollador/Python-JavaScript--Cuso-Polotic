#Dada una lista ( lista1 12 15 32 42 55 75 122 132 150 180 200 ]]), iterarla y
#mostrar números divisibles por cinco, y si encuentra un número mayor que 150, detenga la iteración
#del bucle.

lista = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
nuevaLista = []
for i in range(len(lista)):
    if lista[i] % 5 == 0:
        if lista[i] <= 150:
            nuevaLista.append(lista[i])
print(nuevaLista)