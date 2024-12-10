import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ACCUWEATHER_API_KEY")

def get_weather(latitude, longitude):
    url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{latitude},{longitude}"
    params = {
        "apikey": API_KEY,
        "metric": True
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API Request Failed")
