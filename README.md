# The Nowcast

#### Video Demo: https://youtu.be/6tMH4ATphnQ

#### Description:
The Nowcast provides you with a basic weather and air quality report, detailed weather report, or detailed air quality report for your zipcode right now. It's built with Python Flask, HTML (including the Bootstrap library), and CSS.

#### Dependencies
* The web program is written in Python 3 with the Flask framework.
* Some code depends on the Flask library:
    * app.py
    * helpers.py
* Some code depends on the requests library:
    * helpers.py
* Some code depends on the urllib.request library:
    * helpers.py
* Some code depends on the json library:
    * helpers.py
* HTML and CSS are used as markup langauges.
* The user is required to provide an API key for the [Open Weather API](api.openweathermap.org). Do this by entering `export API_KEY={api_key}` from your terminal once you've opened the project files.

#### Files

#### HTML and CSS Files

| File | Description|
| --- | --- |
|style.css| This file includes the basic styling for classes used across different html files. Classes addressed in this file include the header, the footer, body, and h3.
|apology.html| Provides a descriptive error message the you receive if you do not submit a zipcode.|
|get_Basic_weather.html| Submit your zipcode and preferred units of measurement (Imperial or Metric) to get a basic weather report.|
|basic_weather.html| Returns a basic weather report with current conditions for the your zipcode.|
|get_full_weather.html| Submit your zipcode and preferred units of measurement (Imperial or Metric) to get a more detailed weather report|
|full_weather.html| Returns a detailed weather report with current conditions for the your zipcode.|
|get_full_aqi.html| Submit your zipcode to get a detailed report on the air quality in your area.|
|full_aqi_report.html| Returns a detailed report on the air quality in your area based on your zipcode.|
|layout.html| An html template page that is used throughout the other html pages with Jinja. Provides the content for the navbar and footer. Within the navbar, the text of "The Nowcast" on the top left sends the user to the content of the get_basic_weather.html page, since that should be a good starting point for the majority of users.|

#### Python Files

| File | Description|
| --- | --- |
|app.py| This file contains the "meat" of the Flask application creating this webpage. It includes three functions: weather_basic(), full_weather(), and full_aqi(). All three functions serve html pages that allow users to submit a zipcode, and then based on that zipcode give basic or detailed reports with information from OpenWeather APIs.
|helpers.py| This file contains the helper functions for app.py. The get_coordinates() function takeesthe zipcode submitted by the user and returns the approximate latitude and longitude of that zipcode using the OpenWeather Geocoding API. The get_weather() function takes the user's latitude, longitue, and preferred units of measurement and returns the weather using the OpenWeather Current Weather API. And the get_aqi() function returns data on the Air Quality Index (AQI) for the user's zipcode with the OpenWeather Air Pollution API. Ultimately, the API Calls in each of these functions return crucial data the user is looking for, which is then routed in the appropriate way in by functions in the app.py file to the relevant html display pages.
