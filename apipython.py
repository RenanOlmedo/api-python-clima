import requests

def get_weather_data(city_name, api_key):
    """Fetch weather data from OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Não foi achado dados para {city_name}. Status code: {response.status_code}")
        return None

def display_weather(data):
    """Display weather information in a user-friendly format."""
    if data:
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]

        print(f"\nTempo em {city}, {country}:\n")
        print(f"Temperatura: {temperature} °C")
        print(f"clima: {weather}")
        print(f"Humidade: {humidity}%")
    else:
        print("Sem dados para mostrar.")

def main():
    print("Bem vindo a Consulta do Tempo")
    api_key = "*************"  # Replace with your OpenWeather API key

    while True:
        city_name = input("\nDigite o nome da cidade (ou digite 'exit' para sair): ").strip()
        if city_name.lower() == 'exit':
            print("Goodbye!")
            break

        weather_data = get_weather_data(city_name, api_key)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
