import os

from flask import Flask, flash, redirect, render_template, request, session
from helpers import coordinates, getweather, getaqi

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def weather_basic():
    """Look up basic weather by zipcode"""

    # Render page template if request method is GET
    if request.method == "GET":
        return render_template("get_basic_weather.html")

    # Get zipcode if request method is POST
    if request.method == "POST":

        # Ensure that zipcode field is not emptty
        if not request.form.get("zipcode"):
            return render_template("apology.html")
            
        zipcode = request.form.get("zipcode")

        # Convert zipcode to string and get length to confirm length of form submission
        if len(str(zipcode)) > 5:
            return render_template("apology.html")

        # Make zipcode an int
        zipcode = int(zipcode)

        # Return apology if shares is 0 or negative number
        if zipcode < 1:
            return render_template("apology.html")

        else:
            # Get user's preferred units of measurement
            units = request.form.get("units")

            # Get latitude and longitude for zipcode
            latlong = coordinates(zipcode)
            lat = latlong["lat"]
            lon = latlong["lon"]

            # Get weather by latitude and longitude
            weather = getweather(lat, lon, units)
            aqi = getaqi(lat, lon)

            return render_template("basic_weather.html", weather=weather, aqi=aqi, units=units)

@app.route("/get_full_weather", methods=["GET", "POST"])
def full_weather():
    """Look up weather by zipcode"""

    # Render page template if request method is GET
    if request.method == "GET":
        return render_template("get_full_weather.html")

    # Get zipcode if request method is POST
    if request.method == "POST":

        # Ensure that zipcode field is not emptty
        if not request.form.get("zipcode"):
            return render_template("apology.html")

        zipcode = request.form.get("zipcode")

        # Convert zipcode to string and get length to confirm length of form submission
        if len(str(zipcode)) > 5:
            return render_template("apology.html")

        # Make zipcode an int
        zipcode = int(zipcode)

        # Return apology if shares is 0 or negative number
        if zipcode < 1:
            return render_template("apology.html")

        else:
            # Get user's preferred units of measurement
            units = request.form.get("units")

            # Get latitude and longitude for zipcode
            latlong = coordinates(zipcode)
            lat = latlong["lat"]
            lon = latlong["lon"]

            # Get weather by latitude and longitude
            weather = getweather(lat, lon, units)
            aqi = getaqi(lat, lon)

            return render_template("full_weather.html", weather=weather, aqi=aqi, units=units)

@app.route("/get_full_aqi", methods=["GET", "POST"])
def full_aqi():
    """Look AQI"""

    # Render page template if request method is GET
    if request.method == "GET":
        return render_template("get_full_aqi.html")

    # Get zipcode if request method is POST
    if request.method == "POST":

        # Ensure that zipcode field is not emptty
        if not request.form.get("zipcode"):
            return render_template("apology.html")

        zipcode = request.form.get("zipcode")

        # Convert zipcode to string and get length to confirm length of form submission
        if len(str(zipcode)) > 5:
            return render_template("apology.html")

        # Make zipcode an int
        zipcode = int(zipcode)

        # Return apology if shares is 0 or negative number
        if zipcode < 1:
            return render_template("apology.html")

        else:

            # Get latitude and longitude for zipcode
            latlong = coordinates(zipcode)
            lat = latlong["lat"]
            lon = latlong["lon"]

            # Get weather by latitude and longitude
            aqi = getaqi(lat, lon)

            return render_template("full_aqi_report.html",  aqi=aqi)

