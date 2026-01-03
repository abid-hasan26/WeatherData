import requests

city_name = 'Rangpur'
API_key= '285708e18f1cae13b76f572677b079c3'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('weather is', data['weather'][0]['description'])
    print('Current Temparature is', data['main']['temp'])
    print('Current Temparature Feels like', data['main']['feels_like'])
    print('Humidity is', data['main']['humidity'])
