# Learned about making API calls in this blog: https://www.section.io/engineering-education/integrating-external-apis-with-flask/

import os
import requests
import urllib.request, json

from flask import redirect, render_template, request, session
from functools import wraps

def coordinates(zipcode):
    """Get latitude and longitude for US zipcode"""

    # Contact API
    api_key = os.environ.get("API_KEY")
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},us&appid={api_key}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return (dict)

def getweather(lat, lon, units):
    # Contact API
    api_key = os.environ.get("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return (dict)

def getaqi(lat, lon):
    # Contact API
    api_key = os.environ.get("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return (dict)