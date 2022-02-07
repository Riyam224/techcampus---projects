import requests


city = input('enter the city... ')
api_address = 'https://samples.openweathermap.org/data/2.5/weather?q={},uk&appid=b6907d289e10d714a6e88b30761fae22'.format(
    city)


url = api_address + city
data = requests.get(url).json()
# print(data)

weather = data['weather']
print(weather[0]['description'])
