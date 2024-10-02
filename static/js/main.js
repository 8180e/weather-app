var i = 0;
    
function updateWeatherData(cityName) {
    fetch("/update_weather", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `i=${i}&city_name=${cityName}`
    })
    .then(response => response.json())
    .then(data => {
        document.querySelector(".content .main img").src = `/static/icons/${data.icon}`;
        document.querySelector(".right_align_date").textContent = data.date;
        document.querySelector(".main p").textContent = `${data.temperature}°C`;
        document.querySelector(".right_align i").textContent = `Feels Like: ${data.feels_like}°C`;
        document.querySelector(".right_align span").textContent = `${data.probability_of_precipitation}%`;
        document.querySelector(".content .weather").textContent = data.weather;
        document.querySelector(".content .humidity").textContent = `${data.humidity}%`;
        document.querySelector(".content .right_align_pressure").textContent = `Pressure: ${data.pressure} hPa`;
        document.querySelector(".content .cloudiness").textContent = `${data.cloudiness}%`;
        document.querySelector(".content .right_align_wind").textContent = `Wind Speed: ${data.wind_speed} meter/sec`;
        document.querySelector(".content .visibility").textContent = `${data.visibility} km`;
    })
    .catch(err => console.error(err));
}

document.getElementById("left").addEventListener("click", function(e) {
    e.preventDefault();
    if (i > 0) {
        i -= 1;
        updateWeatherData(document.getElementById("city_name").value || "Paris");
    }
});

document.getElementById("right").addEventListener("click", function(e) {
    e.preventDefault();
    i += 1;
    updateWeatherData(document.getElementById("city_name").value || "Paris");
});