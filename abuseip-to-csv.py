import requests  # Importa la biblioteca requests para realizar solicitudes HTTP
import csv       # Importa la biblioteca csv para manipular archivos CSV

# Definir la URL de la API de AbuseIPDB y la clave de la API para autenticación
url = "https://api.abuseipdb.com/api/v2/check"
# Reemplazar la clave de la API con tu propia clave de AbuseIPDB
api_key = "you_api_key"

# Crear el archivo CSV de salida y escribir el encabezado de las columnas
with open('resultado.csv', mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    # Escribir el encabezado de las columnas en el archivo CSV
    writer.writerow(["Dirección IP", "Cantidad de Reportes"])

    # Leer el archivo CSV que contiene las direcciones IP para la consulta
    with open('equipos.txt') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extrae la dirección IP de cada fila
            direccion_ip = row['direcciones']

            # Define los parámetros para la solicitud a la API
            informacion = {
                "ipAddress": direccion_ip,  # Dirección IP que se va a consultar
                "maxAgeInDays": "60"        # Limita los reportes a los últimos 60 días
            }

            # Cabeceras necesarias para la autenticación y formato de la respuesta de la API
            api = {
                "Key": api_key,              # Clave de API para autenticación en AbuseIPDB
                "Accept": "application/json"  # Define el formato de respuesta como JSON
            }

            # Realizar la solicitud GET a la API de AbuseIPDB con los parámetros y cabeceras especificados
            try:
                response = requests.get(url, headers=api, params=informacion)
                response.raise_for_status()  # Verifica si hubo algún error en la solicitud

                # Convertir la respuesta en un objeto JSON
                respuesta = response.json()

                # Extraer datos relevantes de la respuesta JSON
                # Dirección IP consultada
                ip = respuesta['data']['ipAddress']
                # Total de reportes para la IP
                reportes = respuesta['data']['totalReports']

                # Escribir los datos en el archivo CSV de salida
                writer.writerow([ip, reportes])

                # Imprimir el resultado de la consulta en consola
                print(f"Para la IP {ip}, tiene estos reportes: {reportes}")

            except requests.RequestException as e:
                print(f"Error al consultar la IP {direccion_ip}: {e}")
            except KeyError:
                print(
                    f"Error al procesar la respuesta para la IP {direccion_ip}")
