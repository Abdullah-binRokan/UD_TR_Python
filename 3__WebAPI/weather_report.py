import requests

# store the api urls inside global variables
search_url = 'https://www.metaweather.com/api/location/search/?query='
location_url = 'https://www.metaweather.com/api/location/'


# define a function to input city name then requests its weather
def getWeather():
    city = input("Where in the world are you? ")

    # Catches ConnectionError exceptions and prevents
    # a traceback. Instead, it prints a msg
    try:
        location = requests.get(search_url + city)
        # Call the json method to Convert the respose object
        # from json text to Python dictionary
        location_D = location.json()
        # Catches IndexError exceptions
        # (when the user enters non existing city)
        try:
            woeid = str(location_D[0]['woeid'])
            weather = requests.get(location_url + woeid)
            weather_D = weather.json()
            print(f"Weather for {weather_D['title']}:")
            displayWeather(weather_D)
        except IndexError:
            print('I don\'t know where that is.\n')
    except requests.exceptions.ConnectionError:
        print('Could not connect to server.\n')


# loop over the dictionary and display the
# forecast for each day
def displayWeather(weather_D):
    for forecast in weather_D['consolidated_weather']:
        date = forecast['applicable_date']
        state = forecast['weather_state_name']
        max_temp = 'high ' + str(round(forecast['max_temp'], 1)) + '°C'
        min_temp = 'low ' + str(round(forecast['min_temp'], 1)) + '°C'
        print(f'{date}\t{state}\t{max_temp}\t{min_temp}')
    print('\n')


while True:
    getWeather()
