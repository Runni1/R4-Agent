import requests

def get_weather(city):
    try:
        # Step 1: Dapatkan koordinat kota (lat & lon)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_data = requests.get(geo_url).json()

        if "results" not in geo_data or not geo_data["results"]:
            return f"Kota '{city}' tidak ditemukan."

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # Step 2: Ambil data cuaca berdasarkan lat & lon
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true"
        )
        weather = requests.get(weather_url).json()

        temp = weather["current_weather"]["temperature"]
        wind = weather["current_weather"]["windspeed"]

        return f"Cuaca di {city}: {temp}°C, angin {wind} km/jam."

    except Exception as e:
        return f"Terjadi error: {e}"
