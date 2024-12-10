from flask import Flask
from flask import jsonify
from weather_api import get_weather
from weather_model import check_bad_weather

app = Flask(__name__)

@app.route('/')
def index():
    return "Weather Route Forecast Service"

@app.route('/test/<latitude>/<longitude>')
def test_weather(latitude, longitude):
    weather_data = get_weather(latitude, longitude)
    result = check_bad_weather(weather_data)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
    