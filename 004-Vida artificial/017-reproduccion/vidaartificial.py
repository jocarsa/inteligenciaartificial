import time
import random
import mysql.connector
import math

anchura = 1920
altura = 1080
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

def euclidean_distance(point1, point2):
    # point1 and point2 should be tuples or lists with coordinates (x, y) or (x, y, z) in 2D or 3D respectively
    if len(point1) != len(point2):
        raise ValueError("Both points should have the same number of coordinates (2D or 3D)")

    squared_sum = sum((x - y) ** 2 for x, y in zip(point1, point2))
    distance = math.sqrt(squared_sum)
    return distance
def angle_between_points(point1, point2):
    # point1 and point2 should be tuples or lists with coordinates (x, y) or (x, y, z) in 2D or 3D respectively
    if len(point1) != len(point2):
        raise ValueError("Both points should have the same number of coordinates (2D or 3D)")

    dot_product = sum(x * y for x, y in zip(point1, point2))
    magnitudes_product = euclidean_distance(point1, (0, 0)) * euclidean_distance(point2, (0, 0))
    
    if magnitudes_product == 0:
        raise ValueError("One of the points is the origin, and the angle cannot be determined.")

    cosine_angle = dot_product / magnitudes_product
    angle = math.acos(cosine_angle)

    # Convert the angle from radians to degrees
    angle_degrees = math.degrees(angle)
    return angle_degrees
def calculate_angle(x1, y1, x2, y2):
    # Calculate the differences in x and y coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the angle in radians using atan2
    angle_radians = math.atan2(dy, dx)

    return angle_radians

# Example usage
x1, y1 = 0, 0  # First point
x2, y2 = 3, 4  # Second point
angle_rad = calculate_angle(x1, y1, x2, y2)
class Ser:
    def __init__(self):
        self.edad = 0
        self.id = random.randint(0,10000000)
        self.duracion = 10000000000000-random.randint(0,20)
        self.posx = random.randint(0,anchura)
        self.posy = random.randint(0,altura)
        self.posz = 0
        self.rotx = 0
        self.roty = 0
        self.rotz = random.uniform(0,math.pi*2)
        self.imagen = ""
        self.color = "red"
        self.energia = 1000
        self.hambre = 1
        self.sexo = random.randint(0,1)
        

    def pasoTiempo(self):
        self.edad += 1
        self.hambre += 1
        self.mueve()
        
        
    def dameEdad(self):
        return self.edad
    def mueve(self):
        if self.hambre < 100:
            self.posx = self.posx + math.cos(self.rotz)
            self.posy = self.posy + math.sin(self.rotz)
        else:
            distancia = 10000000
            mejorcandidato = comidas[0]
            for comida in comidas:
                if euclidean_distance((self.posx,self.posy),(comida.posx,comida.posy)) < distancia:
                    distancia = euclidean_distance((self.posx,self.posy),(comida.posx,comida.posy))
                    #print(distancia)

                    mejorcandidato = comida
            try:
                angulo =  calculate_angle(self.posx,self.posy,mejorcandidato.posx,mejorcandidato.posy)
                #print(angulo)
                self.posx = self.posx + math.cos(angulo)
                self.posy = self.posy + math.sin(angulo)
                if euclidean_distance((self.posx,self.posy),(mejorcandidato.posx,mejorcandidato.posy)) < 2:
                    self.hambre -= 100
                    comidas.remove(mejorcandidato)
                    peticion = '''
                    DELETE FROM entidades
                    WHERE
                    id = '''+str(mejorcandidato.id)+''' '''
                    #print(peticion)
                    cursor.execute(peticion)
                    conexion.commit()
                    
                    
            except:
                pass
        if self.hambre <  100 and self.edad > 200:
            distancia = 10000000
            mejorcandidato = seres[0]
            for ser in seres:
                if euclidean_distance((self.posx,self.posy),(ser.posx,ser.posy)) < distancia and ser.sexo != self.sexo:
                    distancia = euclidean_distance((self.posx,self.posy),(ser.posx,ser.posy))
                
                    mejorcandidato = ser
            try:
                angulo =  calculate_angle(self.posx,self.posy,mejorcandidato.posx,mejorcandidato.posy)
                #print(angulo)
                self.posx = self.posx + math.cos(angulo)
                self.posy = self.posy + math.sin(angulo)
            except:
                pass
        
class Comida:
    def __init__(self):
        self.id = random.randint(0,10000000)
        self.posx = random.randint(0,anchura)
        self.posy = random.randint(0,altura)

seres = []
numeroseres = 100
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
        "'''+str(ser.color)+'''",
        "'''+str(ser.sexo)+'''",
        "hambre: '''+str(ser.hambre)+'''"
        )'''
    
    cursor.execute(peticion)
conexion.commit()

comidas = []
numerocomida = 100
for i in range(0,numerocomida):
    comidas.append(Comida())
for comida in comidas:
    peticion = '''
        INSERT INTO entidades
        VALUES (
        NULL,
        '''+str(comida.id)+''',
        "",
        "'''+str(comida.posx)+'''",
        "'''+str(comida.posy)+'''",
        "0",
        "0",
        "0",
        "0",
        "0",
        "blue",
        "",
        "comida"
        )'''
    cursor.execute(peticion)
conexion.commit()

def bucle():
    #print("Estoy en el bucle")
    comidas.append(Comida())
    peticion = '''
        INSERT INTO entidades
        VALUES (
        NULL,
        '''+str(comidas[-1].id)+''',
        "",
        "'''+str(comidas[-1].posx)+'''",
        "'''+str(comidas[-1].posy)+'''",
        "0",
        "0",
        "0",
        "0",
        "0",
        "blue",
        "",
        "comida"
        )'''
    cursor.execute(peticion)
    conexion.commit()
    for ser in seres:
        ser.pasoTiempo()
        #print(ser.dameEdad())
        if ser.edad > ser.duracion or ser.hambre > 200:
            seres.remove(ser)
            peticion = '''
            DELETE FROM entidades
            WHERE
            id = '''+str(ser.id)+'''
            '''

            cursor.execute(peticion)
        peticion = '''
        UPDATE entidades
        SET
        edad = "'''+str(ser.edad)+'''",
        posx = "'''+str(ser.posx)+'''",
        posy = "'''+str(ser.posy)+'''",
        mensaje = "hambre: '''+str(ser.hambre)+'''"
        WHERE
        id = '''+str(ser.id)+'''
        '''
        #print(peticion)
        cursor.execute(peticion)
    conexion.commit()
    time.sleep(0.1)
    bucle()

bucle()
    
