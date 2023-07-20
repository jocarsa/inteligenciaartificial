import time
import random
import mysql.connector
import math

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
        self.rotz = random.uniform(0,math.pi*2)
        self.imagen = ""
        self.color = ""
        

    def pasoTiempo(self):
        self.edad += 1
        self.mueve()
        
    def dameEdad(self):
        return self.edad
    def mueve(self):
        self.posx = self.posx + math.cos(self.rotz)
        self.posy = self.posy + math.sin(self.rotz)

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
        peticion = '''
        UPDATE entidades
        SET
        posx = "'''+str(ser.posx)+'''",
        posy = "'''+str(ser.posy)+'''"
        WHERE
        id = '''+str(ser.id)+'''
        '''

        cursor.execute(peticion)
    conexion.commit()
    time.sleep(1)
    bucle()

bucle()
    
