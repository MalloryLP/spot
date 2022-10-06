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
            print(data["features"])


            URL_METEO = "http://www.infoclimat.fr/public-api/gfs/json?_ll=48.85341,-4.6735&_auth=ABpWQVQqUnAEKQYxAXdVfFkxATQLfQYhBHgEZwlsUC0DaFAxAmIDZVQ6B3oEK1BmWHUCYV5lBDQKYVYuDX8HZgBqVjpUP1I1BGsGYwEuVX5ZdwFgCysGIQRvBGIJelA2A2NQKgJgA2BUOwd7BDZQYVhrAn1efgQ9Cm9WNw1lB2QAY1YzVDVSNARrBnsBLlVnWWkBYgtgBmsEYARiCWxQMwMzUDMCYQNpVDgHewQzUGBYagJgXmMEOQpsVjUNfwd7ABpWQVQqUnAEKQYxAXdVfFk%2FAT8LYA%3D%3D&_c=a91613ef539610b21236d6330be95eeb"
            r  = requests.get(url = URL_METEO)
            data = r.json()

            temp = data[list(data.keys())[9]]["temperature"]["2m"]
            pres = data[list(data.keys())[9]]["pression"]["niveau_de_la_mer"]
            humi = data[list(data.keys())[9]]["humidite"]["2m"]
            
            
            return render(request, template_name="api/city.html", context={"ville": city,"temp": temp, "pres": pres, "humi": humi})
