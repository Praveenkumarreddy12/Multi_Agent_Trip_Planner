import os
import requests

from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool("Weather Search Tool")
def get_weather(city: str) -> str:
    """Get current weather and temperature for a specified city."""

    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return "Weather API key is missing."

    url = "https://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(
            url,
            params={
                "q": city,
                "appid": api_key,
                "units": "metric"
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return (
            f"Weather in {city}: {description}, "
            f"temperature: {temperature}°C"
        )

    except requests.RequestException as error:
        return f"Unable to retrieve weather: {error}"