import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

# Replace with your OpenWeatherMap API key
API_KEY = "889253587a0f694945f999ec1c992be9"

def get_weather_data(city):
    try:
        # Request weather data from OpenWeatherMap API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            raise Exception(data["message"])
        
        return data
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def update_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    data = get_weather_data(city)
    if data:
        display_weather(data)

def display_weather(data):
    city_label.config(text=f"{data['name']}, {data['sys']['country']}")
    temp_label.config(text=f"{data['main']['temp']}°C")
    condition_label.config(text=data['weather'][0]['description'].capitalize())
    wind_label.config(text=f"Wind: {data['wind']['speed']} m/s")
    humidity_label.config(text=f"Humidity: {data['main']['humidity']}%")
    pressure_label.config(text=f"Pressure: {data['main']['pressure']} hPa")
    
    icon_url = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    icon_response = requests.get(icon_url)
    icon_image = Image.open(io.BytesIO(icon_response.content))
    icon_photo = ImageTk.PhotoImage(icon_image)
    icon_label.config(image=icon_photo)
    icon_label.image = icon_photo

# Setting up the main application window
root = tk.Tk()
root.title("Weather App")

# City input
tk.Label(root, text="Enter City:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
city_entry = tk.Entry(root, width=25)
city_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Search button
search_button = tk.Button(root, text="Search", command=update_weather)
search_button.grid(row=0, column=2, padx=10, pady=5)

# Weather details
city_label = tk.Label(root, text="", font=("Helvetica", 20))
city_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

icon_label = tk.Label(root)
icon_label.grid(row=2, column=0, rowspan=4, padx=10, pady=10)

temp_label = tk.Label(root, text="", font=("Helvetica", 20))
temp_label.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

condition_label = tk.Label(root, text="", font=("Helvetica", 14))
condition_label.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

wind_label = tk.Label(root, text="", font=("Helvetica", 14))
wind_label.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

humidity_label = tk.Label(root, text="", font=("Helvetica", 14))
humidity_label.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

pressure_label = tk.Label(root, text="", font=("Helvetica", 14))
pressure_label.grid(row=6, column=1, columnspan=2, padx=10, pady=5)

root.mainloop()
