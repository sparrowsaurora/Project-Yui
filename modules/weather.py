# https://open-meteo.com/en/docs#hourly=&daily=

import requests

# Function to get the weather from Open-Meteo
def get_weather(lat, lon):
    """
    Fetches the current weather data for the given latitude and longitude using Open-Meteo.
    - lat: Latitude of the location.
    - lon: Longitude of the location.

    Returns a dictionary with the weather details.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        # Make a request to Open-Meteo
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()  # Parse JSON response
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Main function
def main():
    # Coordinates for Mahogany Creek, Western Australia
    latitude = -31.8976
    longitude = 116.1124

    # Get the current weather data
    weather_data = get_weather(latitude, longitude)

    # Display the weather data
    if weather_data:
        current_weather = weather_data.get("current_weather", {})
        temperature = current_weather.get("temperature", "N/A")
        windspeed = current_weather.get("windspeed", "N/A")
        winddirection = current_weather.get("winddirection", "N/A")
        weather_code = current_weather.get("weathercode", "N/A")

        print(f"Current Weather in Mahogany Creek, WA:")
        print(f"Temperature: {temperature}°C")
        print(f"Windspeed: {windspeed} km/h")
        print(f"Wind Direction: {winddirection}°")
        print(f"Weather Code: {weather_code}")
    else:
        print("No weather data to display.")

main()
