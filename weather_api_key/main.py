import requests

params_set = {
    'lat': 55.030498,
    'lon': 82.977459,
    'exclude': 'current,minutely,daily,alerts',
    'appid': '48316d7c73422506081bbbd6b921876e',

}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=params_set)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data['hourly'][0:12:]

will_rain = False

for each_hour_data in hourly_data:
    condition_code = each_hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

print(hourly_data)
