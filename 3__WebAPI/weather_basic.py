import requests

r = requests.get('https://www.metaweather.com/api/location/2455920')
d = r.json()

for forecast in d['consolidated_weather']:
    date = forecast['applicable_date']
    humidity = forecast['humidity']
    print(f"date: {date} \thumidity: {humidity}")
