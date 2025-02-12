import requests
import pprint
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
YEAR = 2019

url = f'https://api.tfl.gov.uk/AccidentStats/{YEAR}?app_id={APP_ID}&app_key={API_KEY}'

# fetch

response = requests.get(url)

if response.status_code == 200:
    accident_data = response.json()
    pprint.pprint(accident_data[:2])
else:
    print(f'Error: {response.status_code}, {response.text}')

for accident in accident_data[:10]:
    date = accident['date']
    borough = accident['borough']
    lat = accident['lat']
    lon = accident['lon']
    severity = accident['severity']
    vehicles = [vehicle['type'] for vehicle in accident['vehicles']]

    print(f'\n\nDate: {date}\n Borough: {borough}\n Severity: {severity}\n Vehicle: {vehicles}\n\n')
