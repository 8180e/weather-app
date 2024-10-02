# Warning!
This is the source code of my project for those who are curious. To use this app, you have two options:
1. Easy Way:

    Click this link to visit the Heroku site of the app: https://weather-app-by-8180e-04210bdd5152.herokuapp.com/
2. More Difficult Way:
    - Download the zip file of the project
    - Extract the files
    - Create an OpenWeatherMap account from this link and get an API key: https://home.openweathermap.org/users/sign_up 
    - Create a ".env" file in the extracted folder
    - In the ".env" file type "OPENWEATHER_API_KEY={type_your_api_key_here}" with your API key
    - Type "SECRET_KEY={type_a_secure_secret_key_here}" in the ".env" file again by using a random generated key
    - Run the "app.py" file
    - Type "localhost:5000" in a browser
# Real Time Weather Forecast App
This project is a web application that provides real-time weather data for a specific city using the OpenWeatherMap API. Developed with the Flask framework, it allows users to access temperature, humidity, wind speed and 5-day weather forecasts by entering the city name. With IP-based location detection, instant weather information for the city where the user is located is also displayed.


Features:

- Instant and 5-day weather forecast with OpenWeatherMap API integration.
- IP-based automatic city detection.
- Dynamic and user-friendly interface with the Flask framework.
- Processing of weather data in JSON format and updating with AJAX.
- Advanced error management and modular structure.

This project is a fully-featured application that showcases my API usage, web development and data processing skills.
