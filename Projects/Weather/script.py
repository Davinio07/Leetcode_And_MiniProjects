import requests
from datetime import datetime

class Weather():
    def extractingDataFromApi(self):
        url: str = "https://api.open-meteo.com/v1/forecast?latitude=52.3676&longitude=4.9041&current_weather=true"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def cleaningUpData(self, raw_data):
        clean_data = {}
        temperature: float = float(raw_data["current_weather"]["temperature"])
        temperature_weather_units: str = str(raw_data["current_weather_units"]["temperature"])

        windspeed: float = float(raw_data["current_weather"]["windspeed"])
        windspeed_weather_units: str = str(raw_data["current_weather_units"]["windspeed"])
        
        str_date_Weather: str = str(raw_data["current_weather"]["time"])
        date_Weather = datetime.strptime(str_date_Weather, "%Y-%m-%dT%H:%M")
        time_stamp = datetime.now()
        clean_data["time"] = date_Weather
        clean_data["temperature"] = temperature
        clean_data["windspeed"] = windspeed
        Clean_Data_String: str = (f'[{date_Weather}] Amsterdam Weather - Temp: {temperature}{temperature_weather_units}, Wind: {windspeed} {windspeed_weather_units}, Timestamp: {time_stamp}')
            
        
        
        return Clean_Data_String
        
#weather = Weather()
#extractingDataFromApi = weather.extractingDataFromApi()
#cleaningUpData = weather.cleaningUpData(extractingDataFromApi)
#print(cleaningUpData)
