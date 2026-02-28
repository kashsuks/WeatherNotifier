import requests
import os
from dotenv import load_dotenv
import random

def getWeather(city):
    load_dotenv()
    apiKey = os.getenv('WEATHERAPI')
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    completeUrl = baseUrl + "appid=" + apiKey + "&q=" + city
    response = requests.get(completeUrl)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = round(main['feels_like'] - 273.15, 2)
        description = data['weather'][0]['description']
        with open("weatherData.txt", "w") as file:
            file.write(f"{temperature}\n{description}\n")
        return f"{temperature},{description}"
    else:
        return "City not found or an error occurred."

def getClothingRecommendation(temperature, location):
    temp = float(temperature)
    
    cold_recommendations = [
        "Layer up with a warm coat, thermal underwear, and waterproof boots.",
        "Wear a heavy winter jacket, insulated gloves, and a warm hat.",
        "Put on a thick coat, wool sweater, and waterproof outer layer.",
        "Use thermal layers, a sturdy winter coat, and moisture-wicking clothing."
    ]
    
    if temp <= 0:
        return random.choice(cold_recommendations)
    elif 0 < temp <= 10:
        return "Wear a warm jacket, long pants, and consider a scarf and gloves."
    elif 10 < temp <= 15:
        return "A light jacket or sweater will keep you comfortable. Layer if needed."
    elif 15 < temp <= 20:
        return "Light long-sleeve shirt or light jacket works well in this temperature."
    else:
        return "Comfortable light clothing is best. Stay hydrated and cool."

def main():
    
    with open("location.txt", "r") as file:
        city = file.readline().strip()

    weatherInfo = getWeather(city)

    with open("weatherData.txt", "r") as file:
        temperature = file.readline().strip()
        description = file.readline().strip()

    clothingAdvice = getClothingRecommendation(temperature, city)

    notificationMessage = f"It is currently {temperature}°C in {city} with {description}\n\n{clothingAdvice}"
    
    print(notificationMessage)

if __name__ == "__main__":
    print("Hello")
    main()