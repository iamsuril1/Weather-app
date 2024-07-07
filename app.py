from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    api_key = '9ae92a0734944b7ea45822aad48cbf55c'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    
    if weather_data.get('cod') != 200:
        return render_template('index.html', error=weather_data.get('message'))
    
    weather = {
        'city': city,
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon'],
        'humidity': weather_data['main']['humidity'],
        'wind_speed': weather_data['wind']['speed'],
        'pressure': weather_data['main']['pressure'],
    }
    
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
