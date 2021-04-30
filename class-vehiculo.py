# Crea una clase Minibus que herede de la clase Vehiculo. Debes poder tener
# un método capacidad() que defina por defecto la capacidad de 6 asientos.
# Luego crea una clase Pasajero que puedas ir agregando a una instancia de
# Minibus. Esa instancia no deberá permitir mas de 50 pasajeros únicos (no
# se permiten pasajeros repetidos)

import sys

class Vehiculo:
    def __init__(self, asientos=6):
        self.asientos = asientos

class Minibus(Vehiculo):
    def __init__(self):
        super().__init__(self)
        self.ocupados = []

    def capacidad(self, nuevo_asientos):
        self.asientos = nuevo_asientos
        if self.asientos > 50:
            print("La capacidad limite es hasta 50")
            sys.exit(1)

    def pasajeros(self, pasajero):
        if self.disponibilidad():
            if pasajero in self.ocupados:
                print(f'{pasajero} ya esta dentro!')
            else:
                self.ocupados.append(pasajero)
        else:
            print('Capacidad full')

    def disponibilidad(self):
        asientos = self.asientos - len(self.ocupados)
        return asientos

    def mensaje(self):
        print(f'Hay {self.asientos - len(self.ocupados)} asientos libres')

class Pasajero:
    def __init__(self, nombre):
        self.nombre = nombre

carro1 = Vehiculo()
print(carro1.asientos)

bus1 = Minibus()
bus1.capacidad(2)
print(bus1.asientos)

while bus1.disponibilidad() != 0:
    bus1.mensaje()
    nombre = input('nombre del pasajero: ')
    pasajero = Pasajero(nombre)
    bus1.pasajeros(pasajero.nombre)
    print(bus1.ocupados)
print('Capacidad llena del bus 🚍')
