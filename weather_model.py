def check_bad_weather(weather_data):
    temp = weather_data['Temperature']['Maximum']['Value']
    wind = weather_data['Wind']['Speed']['Value']
    rain_chance = weather_data['Day']['PrecipitationProbability']
    
    if temp < 0 or temp > 35 or wind > 50 or rain_chance > 70:
        return "Bad Weather"
    return "Good Weather"
