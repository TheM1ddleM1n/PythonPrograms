"""Weather Fetcher — powered by Open-Meteo (no API key needed)"""

import json
import urllib.request
import urllib.parse

# World Meteorological Organization weather codes
WMO_CODES = {
    0: "☀️ Clear sky",
    1: "🌤️ Mainly clear",
    2: "⛅ Partly cloudy",
    3: "☁️ Overcast",
    45: "🌫️ Fog",
    48: "🌫️ Icy fog",
    51: "🌦️ Light drizzle",
    53: "🌦️ Moderate drizzle",
    55: "🌧️ Heavy drizzle",
    61: "🌧️ Light rain",
    63: "🌧️ Moderate rain",
    65: "🌧️ Heavy rain",
    71: "🌨️ Light snow",
    73: "🌨️ Moderate snow",
    75: "❄️ Heavy snow",
    80: "🌦️ Light showers",
    81: "🌧️ Moderate showers",
    82: "⛈️ Heavy showers",
    95: "⛈️ Thunderstorm",
    96: "⛈️ Thunderstorm with hail",
}


def fetch_json(url):
    """Fetch JSON data from a URL."""
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read())


def geocode_city(city):
    """Convert city name to (name, country, lat, lon)."""
    url = (
        "https://geocoding-api.open-meteo.com/v1/search?"
        f"name={urllib.parse.quote(city)}&count=1&language=en&format=json"
    )

    data = fetch_json(url)
    results = data.get("results")

    if not results:
        return None

    r = results[0]
    return r["name"], r["country"], r["latitude"], r["longitude"]


def fetch_weather(lat, lon):
    """Fetch current and 3-day forecast weather data."""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,apparent_temperature,weather_code,"
        "wind_speed_10m,relative_humidity_2m"
        "&daily=temperature_2m_max,temperature_2m_min,weather_code"
        "&forecast_days=3&timezone=auto"
    )

    return fetch_json(url)


def format_current_weather(current):
    """Return formatted current weather string."""
    return (
        f"🌡️ Temp: {current.get('temperature_2m')}°C "
        f"(feels like {current.get('apparent_temperature')}°C)\n"
        f"{WMO_CODES.get(current.get('weather_code'), '❓ Unknown')}\n"
        f"💨 Wind: {current.get('wind_speed_10m')} km/h\n"
        f"💧 Humidity: {current.get('relative_humidity_2m')}%"
    )


def format_forecast(daily):
    """Return formatted 3-day forecast string."""
    lines = ["\n📅 3-Day Forecast", "-" * 30]

    for i in range(3):
        date = daily["time"][i]
        hi = daily["temperature_2m_max"][i]
        lo = daily["temperature_2m_min"][i]
        code = daily["weather_code"][i]

        condition = WMO_CODES.get(code, "❓ Unknown")
        lines.append(f"{date}  ↑{hi}°C ↓{lo}°C  {condition}")

    return "\n".join(lines)


def main():
    print("\n🌤️ WEATHER FETCHER")
    print("=" * 40)
    print("Powered by Open-Meteo — no API key needed!\n")

    while True:
        city = input("Enter city (or 'quit'): ").strip()

        if city.lower() == "quit":
            print("\n👋 Stay dry!")
            break

        print("Fetching...\n")

        try:
            location = geocode_city(city)

            if not location:
                print(f"❌ Couldn't find '{city}'. Try another spelling.\n")
                continue

            name, country, lat, lon = location
            weather_data = fetch_weather(lat, lon)

            current = weather_data["current"]
            daily = weather_data["daily"]

            print(f"📍 {name}, {country}")
            print("=" * 35)
            print(format_current_weather(current))
            print(format_forecast(daily))
            print()

        except Exception as e:
            print(f"⚠️ Error: {e}")
            print("Check your internet connection.\n")


if __name__ == "__main__":
    main()
