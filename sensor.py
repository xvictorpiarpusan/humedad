from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import MySQLdb

# Configuración del sensor DHT
dht_sensor_port = 7
dht_sensor_type = 0  # 0 = DHT11 (azul), 1 = DHT22 (blanco)

# Color del fondo del LCD
setRGB(0, 255, 0)

# Conectar a la base de datos MariaDB
try:
    conn = MySQLdb.connect(
        host="localhost",
        user="prueba_user1",

        passwd="1234",
        db="SensorHome"
    )
    cursor = conn.cursor()
except Exception as e:
    print("Error al conectar a la base de datos:", e)
    exit(1)

# Bucle principal
while True:
    try:
        # Leer temperatura y humedad
        [temp, hum] = dht(dht_sensor_port, dht_sensor_type)
        print("temp =", temp, "C\thumidity =", hum, "%")

        if isnan(temp) or isnan(hum):
            raise TypeError("Error: Valor no válido (NaN)")

        # Mostrar en pantalla LCD
        setText_norefresh("Temp:" + str(temp) + "C\n" + "Humidity :" + str(hum) + "%")

        # Insertar en la base de datos
        query = "INSERT INTO Clima (temperatura, humedad) VALUES (%s, %s)"
        cursor.execute(query, (temp, hum))
        conn.commit()

    except:
        pass

    sleep(2)

# Cerrar conexión
cursor.close()
conn.close()