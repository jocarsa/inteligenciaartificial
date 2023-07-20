import time

class Ser:
    def __init__(self):
        self.edad = 0

    def pasoTiempo(self):
        self.edad += 1

seres = []
numeroseres = 10
for i in range(0,numeroseres):
    seres.append(Ser())

def bucle():
    print("Estoy en el bucle")
    for ser in seres:
        ser.pasoTiempo()
    time.sleep(1)
    bucle()

bucle()
    
