**Proyecto Sensor de Humedad con Raspberry Pi y MariaDB**
Este repositorio contiene un script en Python para leer datos de temperatura y humedad desde un sensor DHT (11 o 22) conectado a una Raspberry Pi usando GrovePi, mostrarlos en un display LCD y almacenarlos en una base de datos MariaDB.

## Descripción

Este script se ejecuta en bucle continuo, leyendo la temperatura y humedad del sensor DHT cada 2 segundos.

* Muestra los valores en la consola.
* Actualiza el texto del display LCD Grove RGB.
* Inserta cada lectura válida en la tabla `Clima` de una base de datos MariaDB.

## Características

* Soporta sensores **DHT11** (azul) y **DHT22** (blanco).
* Filtra lecturas inválidas (`NaN`).
* Reconoce fallos de conexión al sensor e imprime errores.
* Gestión de conexión a MariaDB con reconexión y commit por lectura.
* Formato de salida claro en consola y LCD.

## Requisitos

* **Hardware**:

  * Raspberry Pi con GrovePi instalado.
  * Sensor DHT11 o DHT22 conectado al puerto digital 7.
  * Grove RGB LCD conectado a su puerto I2C.
* **Software**:

  * Python 2.7.1
  * Módulos Python:

    * `grovepi`
    * `grove_rgb_lcd`
    * `MySQLdb` (paquete `mysqlclient`)
    * `time`, `math` (incluidos en la librería estándar)
* **Base de datos**:

  * MariaDB 10.x o superior
  * Usuario y base de datos creados (ver sección *Estructura de la base de datos*)

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/raspberrypi-humedad.git
   cd raspberrypi-humedad
   ```
2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instala las dependencias:

   ```bash
   pip install grovepi grove_rgb_lcd mysqlclient
   ```

## Configuración

Edita las siguientes constantes al inicio del archivo `sensor_humedad.py`:

```python
# Puerto digital donde está conectado el sensor DHT (Grove Port 7)
dht_sensor_port = 7
# Tipo de sensor: 0 = DHT11, 1 = DHT22
dht_sensor_type = 0

# Parámetros de conexión a MariaDB
host = "localhost"
user = "prueba_user1"
passwd = "1234"
db = "SensorHome"
```

Asegúrate de que el usuario y la base de datos existen y tienen permisos de INSERT.

## Uso

Ejecuta el script desde la terminal:

```bash
python sensor_humedad.py
```

Verás salidas como:

```
temp = 23.4 C   humidity = 45.2 %
```

y en el LCD:

```
Temp:23.4C
Humidity :45.2%
```

Cada lectura se almacenará en la tabla `Clima`.

## Estructura de la base de datos

Ejecuta este script SQL para crear la tabla:

```sql
CREATE DATABASE IF NOT EXISTS SensorHome;
USE SensorHome;

CREATE TABLE IF NOT EXISTS Clima (
  id INT AUTO_INCREMENT PRIMARY KEY,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  temperatura FLOAT NOT NULL,
  humedad FLOAT NOT NULL
);
```

## Manejo de errores

* Si el sensor devuelve `NaN`, se lanza un `TypeError` y se limpia el LCD.
* Si falla la lectura (`IOError`), se imprime el error y el script sigue intentando.
* Errores de conexión a la base de datos abortan el programa al inicio.

## Detención del programa

Presiona <kbd>Ctrl+C</kbd> para interrumpir. El cursor y la conexión a MariaDB se cerrarán antes de salir.

## Contribuciones

¡Bienvenidas! Para sugerir mejoras o reportar errores, abre un Issue o Pull Request en GitHub.

## Licencia

Este proyecto está bajo la licencia MIT. Revisa el archivo [LICENSE](LICENSE) para más detalles.
