# Weather Dashboard

A Python-based command-line application that displays real-time weather information for any city using the OpenWeatherMap API.

## Features

- Real-time weather data retrieval
- Temperature, humidity, wind speed, and weather conditions display
- Support for multiple cities
- Continuous operation with loop functionality
- Error handling for invalid cities and API issues

## Prerequisites

- Python 3.x
- OpenWeatherMap API key (free tier available)

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/Weather-Dashboard.git
cd Weather-Dashboard

2. Install required dependencies:
pip install requests python-dotenv

3. Obtain a free API key from [OpenWeatherMap](https://openweathermap.org/api)

4. Copy .env.example to .env and add your API key:
cp .env.example .env
Then edit .env and replace your_api_key_here with your actual OpenWeatherMap API key.

## Configuration

The application uses environment variables for secure API key management. Create a .env file in the project root and add your OpenWeatherMap API key as shown above. The .env file is ignored by git to protect sensitive credentials.

## Usage

Run the application:
python weather_dashboard.py

Enter a city name when prompted. Use quit to exit the program.

## Technologies Used

- Python
- Requests library for API calls
- python-dotenv for environment variable management
- OpenWeatherMap API

## License

MIT License