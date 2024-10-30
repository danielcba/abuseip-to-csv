# IP Checker con AbuseIPDB

Este proyecto utiliza la [API de AbuseIPDB](https://www.abuseipdb.com) para consultar información sobre direcciones IP sospechosas y registrar la cantidad de reportes de abuso asociados a cada IP en un archivo CSV.

## Descripción

El script lee un archivo de texto (`equipos.txt`) con una lista de direcciones IP y consulta la API de AbuseIPDB para obtener datos sobre la cantidad de reportes de abuso registrados para cada IP en los últimos 60 días. Los resultados se guardan en un archivo CSV (`resultado.csv`) con las columnas:
- `Dirección IP`
- `Cantidad de Reportes`

Este script es ideal para administradores de sistemas y profesionales de seguridad que necesitan analizar direcciones IP potencialmente peligrosas y determinar su historial de reportes.

## Requisitos

- Python 3.x
- Biblioteca [requests](https://docs.python-requests.org/en/master/) para realizar solicitudes HTTP
- Biblioteca [csv](https://docs.python.org/3/library/csv.html) (incluida en Python) para manipular archivos CSV

Puedes instalar `requests` si no lo tienes ejecutando:
```bash
pip install requests
```

## Configuración

1. Clona este repositorio:
   ```bash
   git clone https://github.com/danielcba/abuseip-to-csv.git
   cd ip-checker
   ```

2. Reemplaza la clave de API en el archivo Python con tu propia clave de AbuseIPDB. Puedes obtener una clave de API registrándote en [AbuseIPDB](https://www.abuseipdb.com/register).

3. Asegúrate de tener un archivo `equipos.txt` en el mismo directorio con la siguiente estructura:
   ```
   direcciones
   192.168.1.1
   203.0.113.5
   ...
   ```

## Uso

Para ejecutar el script y generar el archivo `resultado.csv`, usa el siguiente comando:
```bash
python abuseip-to-csv.py
```

## Explicación del Código

1. **Conexión a la API**: El script utiliza la clave de API y la URL de AbuseIPDB para autenticar la solicitud y acceder a la información de la IP.

2. **Parámetros de Consulta**: 
   - `ipAddress`: Dirección IP que se va a consultar.
   - `maxAgeInDays`: Limita los reportes a los últimos 60 días para obtener datos recientes (valor ajustable).

3. **Manejo de la Respuesta**: El script procesa la respuesta en formato JSON, extrayendo la cantidad de reportes de abuso asociados a la IP y registrándolos en un archivo CSV. Si hay algún error en la solicitud o en la respuesta, el script muestra un mensaje indicando el problema.

## Ejemplo de Salida

La salida del script es un archivo `resultado.csv` con el siguiente formato:
```csv
Dirección IP, Cantidad de Reportes
192.168.1.1, 15
203.0.113.5, 42
...
```

Además, el script muestra en la consola un mensaje similar a:
```
Para la IP 192.168.1.1, tiene estos reportes: 15
Para la IP 203.0.113.5, tiene estos reportes: 42
```

## Documentación de AbuseIPDB

[AbuseIPDB](https://www.abuseipdb.com) es una base de datos colaborativa que recopila reportes de actividades maliciosas de direcciones IP, ayudando a identificar y bloquear IP sospechosas. La API de AbuseIPDB permite realizar diversas consultas, como:
- **Verificación de IP** (`check`): consulta el historial de reportes de una IP.
- **Listado de IP bloqueadas** (`blacklist`): proporciona una lista de IP en la base de datos con altos números de reportes.
- **Reportes de IP** (`report`): permite a los usuarios reportar una IP específica si han detectado actividad sospechosa.

Para obtener más información, consulta la [documentación oficial de la API de AbuseIPDB](https://www.abuseipdb.com/docs).

## Notas de Seguridad

No incluyas tu clave de API directamente en el código si planeas compartir el repositorio, usa variables de entorno para manejar las claves de API de manera segura:
```python
import os
api_key = os.getenv("ABUSEIPDB_API_KEY")
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

