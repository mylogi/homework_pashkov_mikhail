"""The Weather app

Write a console application which takes as an input a city name and returns current weather in the format of your
choice. For the current task, you can choose any weather API or website or use https://openweathermap.org

"""

# Solution:

import json

import requests

api_key = ''

units = 'units=metric'

iso_code_ukraine = 'ISO 3166-2:UA'

city_name = input('Please enter your city: ')

url_api_geocoding_api = f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},,{iso_code_ukraine}&limit=5&appid={api_key}'


def first_response():
    response = requests.get(url_api_geocoding_api)
    data_as_json_first_response = response.text
    return json.loads(data_as_json_first_response)


def get_city_lat_and_lon(list_1: list):
    dictionary_from_list: dict = list_1[0]
    lat_new = ''
    lon_new = ''
    for _, _ in dictionary_from_list.items():
        lat_new = dictionary_from_list['lat']
        lon_new = dictionary_from_list['lon']
    return [lat_new, lon_new]


lat = get_city_lat_and_lon(first_response())[0]
lon = get_city_lat_and_lon(first_response())[1]

url_api_current_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&{units}'


def second_response():
    response_2 = requests.get(url_api_current_weather)
    data_as_json_second_response = response_2.text
    return json.loads(data_as_json_second_response)


def human_views(dict_1: dict):
    func_data = dict_1
    for _, _ in func_data.items():
        # weather = func_data['weather'][0]['main']
        weather_info = func_data['weather'][0]['description']
        temperature = func_data['main']['temp']
        feels_like = func_data['main']['feels_like']
        wind = func_data['wind']['speed']
        return f'Weather: {weather_info.capitalize()}\nTemperature: {temperature}\nFeels like: {feels_like}\nWind: {wind}'


def main():
    print(f'\n{human_views(second_response())}')


if __name__ == '__main__':
    main()
