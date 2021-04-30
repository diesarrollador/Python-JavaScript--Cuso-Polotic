#Escribe un programa en Python que muestre la hora actual con una suma de dos horas adicionales
import datetime
fechayHora = datetime.datetime.now()
adelantado = fechayHora + datetime.timedelta(hours=2)
print(adelantado)
