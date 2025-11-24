import os
import requests

def get_weather_forecast(city: str):
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    if not API_KEY:
        return {"error": "Missing OPENWEATHER_API_KEY"}

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={API_KEY}&units=metric"
    )

    response = requests.get(url).json()

    return {
        "temperature": response.get("main", {}).get("temp"),
        "conditions": response.get("weather", [{}])[0].get("description"),
        "humidity": response.get("main", {}).get("humidity")
    }