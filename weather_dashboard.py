import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_weather(city):
    """Fetch weather data from OpenWeatherMap API"""

    # Get API key from environment variable
    api_key = os.getenv('OPENWEATHER_API_KEY')

    if not api_key:
        print("Error: API key not found in .env file")
        return None

    # API endpoint
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'  # Fahrenheit (use 'metric' for Celsius)
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise error if request failed
        return response.json()

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Error: City '{city}' not found")
        else:
            print(f"HTTP Error: {e}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def display_weather(weather_data):
    """Display weather information in a nice format"""

    if not weather_data:
        return

    # Extract data from the JSON response
    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']

    # Display formatted output
    print("\n" + "=" * 50)
    print(f"   Weather in {city}, {country}")
    print("=" * 50)
    print(f"  🌡️  Temperature: {temp}°F")
    print(f"  🤔 Feels Like: {feels_like}°F")
    print(f"  ☁️  Conditions: {description.capitalize()}")
    print(f"  💧 Humidity: {humidity}%")
    print(f"  💨 Wind Speed: {wind_speed} mph")
    print("=" * 50 + "\n")


def main():
    """Main program loop"""

    print("🌤️  Welcome to Weather Dashboard!")
    print("-" * 50)

    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()

        if city.lower() == 'quit':
            print("Goodbye! 👋")
            break

        if not city:
            print("Please enter a valid city name")
            continue

        # Fetch and display weather
        weather_data = get_weather(city)
        display_weather(weather_data)


if __name__ == "__main__":
    main()