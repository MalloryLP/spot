from django.shortcuts import render
import requests

# Create your views here.

def render_api(request):

    if request.method == "GET":
        return render(request, template_name="api/main.html")

    elif request.method == "POST":

        if "find" in request.POST:

            city = request.POST.get("city", None)

            URL_GPS = "https://api-adresse.data.gouv.fr/search/?q=" + city
            r  = requests.get(url = URL_GPS)
            data = r.json()
            insee = data["features"][0]["properties"]["id"]

            api_key = '10d3757de06174a1a026b2ccbd16edbfd4f2ba5de5c0081df040fbde6fa407dd'
            URL_METEO = "https://api.meteo-concept.com/api/forecast/daily?token="+ api_key +'&insee='+ insee +''
            r  = requests.get(url = URL_METEO)
            data = r.json()

            (city,forecast) = (data[k] for k in ('city','forecast'))

            for i,r2 in enumerate(forecast):
                insee_code = r2["insee"]          # Code Insee de la commune
                postal_code = r2["cp"]            # Code postal de la commune
                latitude = r2["latitude"]         # Latitude décimale de la commune
                longitude = r2["longitude"]       # Longitude décimale de la commune
                day = r2["day"]                   # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
                datetime = r2["datetime"]         # Date en heure locale, format ISO8601
                wind10m = r2["wind10m"]           # Vent moyen à 10 mètres en km/h
                gust10m = r2["gust10m"]           # Rafales de vent à 10 mètres en km/h
                dirwind10m = r2["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
                rr10 = r2["rr10"]                 # Cumul de pluie sur la journée en mm
                rr1 = r2["rr1"]                   # Cumul de pluie maximal sur la journée en mm
                probarain = r2["probarain"]       # Probabilité de pluie entre 0 et 100%
                weather = r2["weather"]           # Temps sensible (Code temps) – Voir Annexes
                tmin = r2["tmin"]                 # Température minimale à 2 mètres en °C
                tmax = r2["tmax"]                 # Température maximale à 2 mètres en °C
                sun_hours = r2["sun_hours"]       # Ensoleillement en heures
                etp = r2["etp"]                   # Cumul d'évapotranspiration en mm
                probafrost = r2["probafrost"]     # Probabilité de gel entre 0 et 100%
                probafog = r2["probafog"]         # Probabilité de brouillard entre 0 et 100%
                probawind70 = r2["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
                probawind100 = r2["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
                gustx = r2["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h
            
            return render(request, template_name="api/city.html", context={"ville": city["name"], "data" : {"tmin": tmin, "tmax": tmax, "pres": 1/100, "humi": 1}, "analysis": {"temp_analysis": 1, "humi_analysis": 1}})

def weather_analysis(temp, humi):
    if temp < 10:
        temp_msg = "froid"
    elif 10 < temp < 20:
        temp_msg = "tiède"
    elif 20 < temp:
        temp_msg = "chaud"
    else:
        temp_msg = "error"

    if humi < 70:
        humi_msg = "sec"
    elif 70 < humi:
        humi_msg = "humide"
    else:
        humi_msg = "error"

    return temp_msg, humi_msg

    