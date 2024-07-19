import tkinter as tk
from tkinter import messagebox
import requests
import json

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather():
    location = entry_location.get().strip()
    if not location:
        messagebox.showerror("Input Error", "Please enter a location.")
        return

    weather_data = get_weather(api_key, location)
    if weather_data:
        city = weather_data['name']
        weather = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        result_var.set(f"City: {city}\nWeather: {weather}\nTemperature: {temp}°C\nHumidity: {humidity}%")
    else:
        messagebox.showerror("Error", "Weather data could not be retrieved.")

# Set up the GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

api_key = 'dc477727831d4a7cda8870ea91b79b98'  # Replace with your actual API key

tk.Label(root, text="Enter city name or ZIP code:").pack(pady=10)
entry_location = tk.Entry(root, width=30)
entry_location.pack(pady=5)

tk.Button(root, text="Get Weather", command=display_weather).pack(pady=20)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, justify="left").pack(pady=10)

root.mainloop()
