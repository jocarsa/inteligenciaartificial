import time
import random
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "vidaartificial",
    "password": "vidaartificial",
    "database": "vidaartificial",
}
conexion = mysql.connector.connect(**db_config)
cursor = conexion.cursor()
cursor.execute("TRUNCATE entidades")
conexion.commit()
class Ser:
    def __init__(self):
        self.edad = 0
        self.id = random.randint(0,10000000)
        self.duracion = 100-random.randint(0,20)
        self.posx = random.randint(0,512)
        self.posy = random.randint(0,512)
        self.posz = 0
        self.rotx = 0
        self.roty = 0
        self.rotz = random.randint(0,360)
        self.imagen = ""
        self.color = ""

    def pasoTiempo(self):
        self.edad += 1
        
    def dameEdad(self):
        return self.edad

seres = []
numeroseres = 10
for i in range(0,numeroseres):
    seres.append(Ser())
for ser in seres:
    peticion = '''
        INSERT INTO entidades
        VALUES (
        NULL,
        '''+str(ser.id)+''',
        "'''+str(ser.edad)+'''",
        "'''+str(ser.posx)+'''",
        "'''+str(ser.posy)+'''",
        "'''+str(ser.posz)+'''",
        "'''+str(ser.rotx)+'''",
        "'''+str(ser.roty)+'''",
        "'''+str(ser.rotz)+'''",
        "'''+str(ser.imagen)+'''",
        "'''+str(ser.color)+'''"
        )'''
    cursor.execute(peticion)
conexion.commit()
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
    
