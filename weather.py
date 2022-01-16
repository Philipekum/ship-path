import requests as r

# Gets weather data
def weather_getter(lat, lon):
    url = 'https://api.weather.yandex.ru/v2/forecast/'
    api_key = 'ff2a5ef9-128a-47c8-81d7-be2adfa7d7c3'
    data = {'lat': lat,
            'lon': lon}
    headers = {'X-Yandex-API-Key': api_key}

    data = r.get(url, data, headers=headers).json()

    wind_speed = data['fact']['wind_speed']
    wind_dir = data['fact']['wind_dir']

    return wind_speed, wind_dir

# lat, lon = '55.75396', '37.620393'
lat, lon = '-7.12082', '-12.884849'
print(weather_getter(lat, lon))
