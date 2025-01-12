import requests
import tkinter as tk
from tkinter import messagebox

def get_weather_data(city_name, api_key):
    """Fetch weather data from OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    """Format weather information for display."""
    if data:
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]

        return (f"Clima em {city}, {country}:\n"
                f"Temperatura: {temperature} °C\n"
                f"Condição: {weather}\n"
                f"Umidade: {humidity}%")
    else:
        return "Erro: Não foi possível obter os dados do clima."

def search_weather():
    city_name = city_entry.get().strip()
    if not city_name:
        messagebox.showwarning("Erro de entrada", "Por favor, insira o nome de uma cidade.")
        return

    api_key = "106e557aa58df1a15a881e80f8792550"  # Substitua pela sua chave da API do OpenWeather
    weather_data = get_weather_data(city_name, api_key)

    if weather_data:
        result = display_weather(weather_data)
        result_label.config(text=result)
    else:
        messagebox.showerror("Erro", "Não foi possível obter os dados. Verifique o nome da cidade ou sua chave da API.")

# Cria a janela GUI
app = tk.Tk()
app.title("Aplicativo de Clima")
app.geometry("400x300")

# Rótulo e entrada para o nome da cidade
city_label = tk.Label(app, text="Insira o nome da cidade:")
city_label.pack(pady=5)

city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=5)

# Botão de pesquisa
search_button = tk.Button(app, text="Pesquisar Clima", command=search_weather)
search_button.pack(pady=10)

# Rótulo para exibição dos resultados
result_label = tk.Label(app, text="", justify="left", wraplength=350)
result_label.pack(pady=10)

# Executa o loop de eventos da GUI
app.mainloop()
