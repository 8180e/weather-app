const notification = document.getElementById("notification");

async function getData() {
  const city = document.getElementById("cityInput").value;
  const url = `https://weather-app-proxy.vercel.app/api/proxy?city=${city}`;
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    return json;
  } catch (error) {
    if (error.message.slice(-3) === "404") {
      notification.innerHTML = "City not found!";
    } else {
      notification.innerHTML = "An error occurred, please try again";
    }

    notification.classList.remove("animate");
    notification.style.display = "inherit";
    void notification.offsetWidth;
    notification.classList.add("animate");
    console.error(error.message);
  }
}

async function displayWeather(event) {
  event.preventDefault();

  const data = await getData();
  if (data) {
    const [weather, main, wind] = [data.weather[0], data.main, data.wind];
    const icon = document.getElementById("icon");
    const iconSrc = `https://openweathermap.org/img/wn/${weather.icon}@2x.png`;

    for (const pair of [
      ["cityName", `Weather Forecast For ${data.name}`],
      ["weather", `${weather.main}, `],
      ["temp", `${main.temp}°C`],
      ["feelsLike", `Feels like ${main.feels_like}°C`],
      ["pressure", `Pressure: ${main.pressure}hPa`],
      ["humidity", `Humidity: ${main.humidity}%`],
      ["minTemp", `${main.temp_min}°C`],
      ["maxTemp", `${main.temp_max}°C`],
      ["windSpeed", `Wind Speed: ${wind.speed}m/s`],
      ["windDirection", `Wind Direction: ${wind.deg}°`],
      ["cloudiness", `Cloudiness: ${data.clouds.all}%`],
    ]) {
      document.getElementById(pair[0]).textContent = pair[1];
    }

    if (icon) {
      icon.src = iconSrc;
    } else {
      const img = document.createElement("img");

      img.id = "icon";
      img.src = iconSrc;
      img.alt = "Weather icon";
      img.className = "left";
      img.style.width = "75px";
      img.style.height = "75px";

      document.getElementById("weatherData").prepend(img);
    }
  }
}
