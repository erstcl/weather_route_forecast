from flask import Flask
from flask import jsonify
from weather_api import get_weather
from weather_model import check_bad_weather
from flask import request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Weather Route Forecast Service"

@app.route('/test/<latitude>/<longitude>')
def test_weather(latitude, longitude):
    weather_data = get_weather(latitude, longitude)
    result = check_bad_weather(weather_data)
    return jsonify(result)

@app.route('/', methods=['GET', 'POST'])
def route_weather():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        return f"Weather check for {start} to {end}"
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
