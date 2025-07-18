from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan

# Configuración del sensor DHT
dht_sensor_port = 7
dht_sensor_type = 0  # 0 = DHT11 (azul), 1 = DHT22 (blanco)

# Color del fondo del LCD
setRGB(0, 255, 0)

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

    except:
        pass

