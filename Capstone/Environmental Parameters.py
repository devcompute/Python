"""
Create a script called weather that return the environmental parameters (temperature (min, max), windspeed, humidity, 
cloud, pressure, sunrise and sunset) of any location you want; after passing arguments (like user api and city id).
"""
import requests
import argparse


def get_weather(api_key, city_id):
    # Construct the API request URL
    api_url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}"

    # Make the API request
    response = requests.get(api_url)
    data = response.json()

    # Extract the relevant data from the response
    temperature = data['main']['temp']
    wind_speed = data['wind']['speed']
    humidity = data['main']['humidity']
    clouds = data['clouds']['all']
    pressure = data['main']['pressure']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']

    # Return the weather data
    return {
        'temperature': temperature,
        'wind_speed': wind_speed,
        'humidity': humidity,
        'clouds': clouds,
        'pressure': pressure,
        'sunrise': sunrise,
        'sunset': sunset
    }


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-key', required=True, help='OpenWeatherMap API key')
    parser.add_argument('--city-id', required=True, help='City ID')
    args = parser.parse_args()

    # Get the weather data
    weather_data = get_weather(args.api_key, args.city_id)

    # Print the weather data
    print(weather_data)
