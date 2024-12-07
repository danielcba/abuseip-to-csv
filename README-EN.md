# IP Checker with AbuseIPDB

This Python script uses the [AbuseIPDB API](https://www.abuseipdb.com) to query information about suspicious IP addresses and log the number of abuse reports associated with each IP in a CSV file.

## Description

The script reads a text file (`equipos.txt`) containing a list of IP addresses and queries the AbuseIPDB API to get data on the number of abuse reports recorded for each IP in the past 60 days. The results are saved in a CSV file (`resultado.csv`) with the columns:
- `IP Address`
- `Number of Reports`

This script is ideal for system administrators and security professionals who need to analyze potentially dangerous IP addresses and determine their abuse report history.

## Requirements

- Python 3.x
- [requests](https://docs.python-requests.org/en/master/) library to make HTTP requests
- [csv](https://docs.python.org/3/library/csv.html) library (included in Python) to handle CSV files

You can install `requests` if you don’t have it by running:
```bash
pip install requests
```

## Setup

1. Clone this repository:
   ```bash
    git clone https://github.com/danielcba/abuseip-to-csv.git
    cd abuseip-to-csv
   ```

2. Replace the API key in the Python file with your own AbuseIPDB API key. You can obtain an API key by registering at [AbuseIPDB](https://www.abuseipdb.com/register).

3. Make sure you have a `equipos.txt` file in the same directory with the following structure:
   ```
   addresses
   192.168.1.1
   203.0.113.5
   ...
   ```

## Usage

To run the script and generate the `resultado.csv` file, use the following command:
```bash
python abuseip-to-csv.py
```

## Code Explanation

1. **API Connection**: The script uses the API key and AbuseIPDB URL to authenticate the request and access IP information.

2. **Query Parameters**:
   - `ipAddress`: IP address to be queried.
   - `maxAgeInDays`: Limits the reports to the last 60 days to obtain recent data (adjustable value).

3. **Response Handling**: The script processes the JSON response, extracts the number of abuse reports associated with the IP, and logs them in a CSV file. If there is an error in the request or response, the script displays a message indicating the issue.

## Example Output

The output of the script is a `resultado.csv` file with the following format:
```csv
Dirección IP, Cantidad de Reportes
192.168.1.1, 15
203.0.113.5, 42
...
```

Additionally, the script displays a message on the console like:
```
Para la IP 192.168.1.1, tiene estos reportes: 15
Para la IP 203.0.113.5, tiene estos reportes: 42
```

## AbuseIPDB Documentation

[AbuseIPDB](https://www.abuseipdb.com) is a collaborative database that collects reports of malicious IP address activities, helping identify and block suspicious IPs. The AbuseIPDB API allows various queries, such as:
- **IP Check** (`check`): queries an IP's report history.
- **Blacklist** (`blacklist`): provides a list of IPs in the database with high report counts.
- **IP Reports** (`report`): lets users report a specific IP if they have detected suspicious activity.

For more information, see the [official AbuseIPDB API documentation](https://docs.abuseipdb.com/#introduction).

## Security Notes

Do not include your API key directly in the code if you plan to share the repository publicly. Instead, use environment variables to handle API keys securely:
```python
import os
api_key = os.getenv("ABUSEIPDB_API_KEY")
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
