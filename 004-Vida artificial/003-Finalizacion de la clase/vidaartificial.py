import time
import random

class Ser:
    def __init__(self):
        self.edad = 0
        self.duracion = 100-random.randint(0,20)

    def pasoTiempo(self):
        self.edad += 1
        
    def dameEdad(self):
        return self.edad

seres = []
numeroseres = 10
for i in range(0,numeroseres):
    seres.append(Ser())

def bucle():
    print("Estoy en el bucle")
    for ser in seres:
        ser.pasoTiempo()
        print(ser.dameEdad())
        if ser.edad > ser.duracion:
            seres.remove(ser)
    time.sleep(0.1)
    bucle()

bucle()
    
