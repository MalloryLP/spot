#!/usr/bin/python

import requests

'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("location")
args = parser.parse_args()
location = args.location
'''

location = '29019' # Code Insee de la ville de Brest

api_key = '10d3757de06174a1a026b2ccbd16edbfd4f2ba5de5c0081df040fbde6fa407dd' # Token unique API Météo Concept (obtenu gratuitement sur inscription)

WEATHER = {
	0: "Soleil",
	1: "Peu nuageux",
	2: "Ciel voilé",
	3: "Nuageux",
	4: "Très nuageux",
	5: "Couvert",
	6: "Brouillard",
	7: "Brouillard givrant",
	10: "Pluie faible",
	11: "Pluie modérée",
	12: "Pluie forte",
	13: "Pluie faible verglaçante",
	14: "Pluie modérée verglaçante",
	15: "Pluie forte verglaçante",
	16: "Bruine",
	20: "Neige faible",
	21: "Neige modérée",
	22: "Neige forte",
	30: "Pluie et neige mêlées faibles",
	31: "Pluie et neige mêlées modérées",
	32: "Pluie et neige mêlées fortes",
	40: "Averses de pluie locales et faibles",
	41: "Averses de pluie locales",
	42: "Averses locales et fortes",
	43: "Averses de pluie faibles",
	44: "Averses de pluie",
	45: "Averses de pluie fortes",
	46: "Averses de pluie faibles et fréquentes",
	47: "Averses de pluie fréquentes",
	48: "Averses de pluie fortes et fréquentes",
	60: "Averses de neige localisées et faibles",
	61: "Averses de neige localisées",
	62: "Averses de neige localisées et fortes",
	63: "Averses de neige faibles",
	64: "Averses de neige",
	65: "Averses de neige fortes",
	66: "Averses de neige faibles et fréquentes",
	67: "Averses de neige fréquentes",
	68: "Averses de neige fortes et fréquentes",
	70: "Averses de pluie et neige mêlées localisées et faibles",
	71: "Averses de pluie et neige mêlées localisées",
	72: "Averses de pluie et neige mêlées localisées et fortes",
	73: "Averses de pluie et neige mêlées faibles",
	74: "Averses de pluie et neige mêlées",
	75: "Averses de pluie et neige mêlées fortes",
	76: "Averses de pluie et neige mêlées faibles et nombreuses",
	77: "Averses de pluie et neige mêlées fréquentes",
	78: "Averses de pluie et neige mêlées fortes et fréquentes",
	100: "Orages faibles et locaux",
	101: "Orages locaux",
	102: "Orages fort et locaux",
	103: "Orages faibles",
	104: "Orages",
	105: "Orages forts",
	106: "Orages faibles et fréquents",
	107: "Orages fréquents",
	108: "Orages forts et fréquents",
	120: "Orages faibles et locaux de neige ou grésil",
	121: "Orages locaux de neige ou grésil",
	122: "Orages locaux de neige ou grésil",
	123: "Orages faibles de neige ou grésil",
	124: "Orages de neige ou grésil",
	125: "Orages de neige ou grésil",
	126: "Orages faibles et fréquents de neige ou grésil",
	127: "Orages fréquents de neige ou grésil",
	128: "Orages fréquents de neige ou grésil",
	130: "Orages faibles et locaux de pluie et neige mêlées ou grésil",
	131: "Orages locaux de pluie et neige mêlées ou grésil",
	132: "Orages fort et locaux de pluie et neige mêlées ou grésil",
	133: "Orages faibles de pluie et neige mêlées ou grésil",
	134: "Orages de pluie et neige mêlées ou grésil",
	135: "Orages forts de pluie et neige mêlées ou grésil",
	136: "Orages faibles et fréquents de pluie et neige mêlées ou grésil",
	137: "Orages fréquents de pluie et neige mêlées ou grésil",
	138: "Orages forts et fréquents de pluie et neige mêlées ou grésil",
	140: "Pluies orageuses",
	141: "Pluie et neige mêlées à caractère orageux",
	142: "Neige à caractère orageux",
	210: "Pluie faible intermittente",
	211: "Pluie modérée intermittente",
	212: "Pluie forte intermittente",
	220: "Neige faible intermittente",
	221: "Neige modérée intermittente",
	222: "Neige forte intermittente",
	230: "Pluie et neige mêlées",
	231: "Pluie et neige mêlées",
	232: "Pluie et neige mêlées",
	235: "Averses de grêle",
}

# ********************* MENU ************************** #
print("\nVeuillez faire votre choix entre 1 et 8 : \n")
choice = input(" 0 > Informations diverses sur la commune \n" + 
               " 1 > Éphéméride pour un jour à venir (J+14 maximum) \n" +
               " 2 > Prévisions journalières sur les 14 prochains jours \n" +
               " 3 > Prévisions journalières pour un jour (J+14 maximum) \n" +
               " 4 > Prévisions par périodes de la journée sur les 14 prochains jours \n" +
               " 5 > Prévisions par périodes de la journée pour un jour (J+14 maximum) \n" +  
               " 6 > Prévisions pour une période de la journée pour un jour (J+14 maximum) \n" +
               " 7 > Prévisions horaires pour les 12 prochaines heures \n" + 
               " 8 > Données météorologiques d'une station à proximité \n" + 
               " q > Quitter \n" + 
               "\nChoix : ")

if(choice == '0'):
    r0 = requests.get('https://api.meteo-concept.com/api/location/city?token='+ api_key +'&insee='+ location).json()
    
    # city object
    insee_code = r0['city']['insee']    # Code Insee de la commune
    postal_code = r0['city']['cp']      # Code postal de la commune
    latitude = r0['city']['latitude']   # Latitude décimale de la commune
    longitude = r0['city']['longitude'] # Longitude décimale de la commune
    altitude = r0['city']['altitude']   # Altitude de la commune en mètres
    city_name = r0['city']['name']      # Nom de la commune
    
    print("\nNom de la ville : ", city_name)
    print("Code INSEE : ", insee_code)
    print("Code postal : ", postal_code)
    print("Latitude : ", latitude)
    print("Longitude : ", longitude)
    print("Altitude : ", altitude, "m")
    
    '''
    # Informations diverses sur une commune ou une liste de communes recherchées en fonction de son nom, premiers caractères, ou code postal. 
    r0 = requests.get('https://api.meteo-concept.com/api/location/cities/?token='+          api_key +'&search='+ location +'').json()
    '''

elif(choice == '1'):
    choice_day = input("\nChoisir le jour (entre 0 et 13) : ")
    r1 = requests.get('https://api.meteo-concept.com/api/ephemeride/' + choice_day + '?token=' + api_key +'&insee='+ location +'').json()

    insee_code = r1["ephemeride"]["insee"]                    # Code Insee de la commune
    latitude = r1["ephemeride"]["latitude"]                   # Latitude décimale de la commune
    longitude = r1["ephemeride"]["longitude"]                 # Longitude décimale de la commune
    day = r1["ephemeride"]["day"]                             # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
    datetime = r1["ephemeride"]["datetime"]                   # Date en heure locale, format ISO8601
    sunrise = r1["ephemeride"]["sunrise"]                     # Heure du lever du soleil, format HH:MM
    sunset = r1["ephemeride"]["sunset"]                       # Heure du coucher du soleil, format HH:MM
    duration_day = r1["ephemeride"]["duration_day"]           # Durée du jour en heure et minutes, format HH:MM
    diff_duration_day = r1["ephemeride"]["diff_duration_day"] # Gain ou perte de durée du jour par rapport à la veille en minutes

    print("\nJour  : J+", str(day))
    print("Heure locale : ", datetime)
    print("Lever du soleil : ", sunrise)
    print("Coucher du soleil : ", sunset)
    print("Durée du jour : ", duration_day)
    print("Gain ou perte de durée du jour : ", diff_duration_day, "min")

elif(choice == '2'):
    f = requests.get('https://api.meteo-concept.com/api/forecast/daily?token='+ api_key +'&insee='+ location +'').json()
    (city,forecast) = (f[k] for k in ('city','forecast'))

    for i,r2 in enumerate(forecast):
        # forecast-day object
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

        print("\nPrévision : J+" + str(i))
        print("Heure locale : ", datetime)
        print("Vent moyen à 10m : ", wind10m, "km/h")
        print("Rafales de vent à 10m : ", gust10m, "km/h")
        print("Direction du vent : ", dirwind10m, "°")
        print("Cumul de pluie sur la journée: ", rr10, "mm")
        print("Cumul de pluie maximal sur la journée : ", rr1, "mm")
        print("Probabilité de pluie : ", probarain, "%")
        print("Temps : ", WEATHER[weather])
        print("Température minimale (à 2m) : ", tmin, "°C")
        print("Température maximale (à 2m) : ", tmax, "°C")
        print("Ensoleillement : ", sun_hours, "h")
        print("Evapotranspiration : ", etp, "mm")
        print("Probabilité de gel : ", probafrost, "%")
        print("Probabilité de brouillard : ", probafog, "%")
        print("Probabilité de vent >70 km/h : ", probawind70, "%")
        print("Probabilité de vent >100 km/h : ", probawind100, "%")
        print("Rafale de vent potentielle sous orage : ", gustx, "km/h")

elif(choice == '3'):
    choice_day = input("\nChoisir le jour (entre 0 et 13) : ")
    r3 = requests.get('https://api.meteo-concept.com/api/forecast/daily/' + choice_day + '?token='+ api_key +'&insee='+ location +'').json()

    # forecast-day object
    insee_code = r3["forecast"]["insee"]          # Code Insee de la commune
    postal_code = r3["forecast"]["cp"]            # Code postal de la commune
    latitude = r3["forecast"]["latitude"]         # Latitude décimale de la commune
    longitude = r3["forecast"]["longitude"]       # Longitude décimale de la commune
    day = r3["forecast"]["day"]                   # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
    datetime = r3["forecast"]["datetime"]         # Date en heure locale, format ISO8601
    wind10m = r3["forecast"]["wind10m"]           # Vent moyen à 10 mètres en km/h
    gust10m = r3["forecast"]["gust10m"]           # Rafales de vent à 10 mètres en km/h
    dirwind10m = r3["forecast"]["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
    rr10 = r3["forecast"]["rr10"]                 # Cumul de pluie sur la journée en mm
    rr1 = r3["forecast"]["rr1"]                   # Cumul de pluie maximal sur la journée en mm
    probarain = r3["forecast"]["probarain"]       # Probabilité de pluie entre 0 et 100%
    weather = r3["forecast"]["weather"]           # Temps sensible (Code temps) – Voir Annexes
    tmin = r3["forecast"]["tmin"]                 # Température minimale à 2 mètres en °C
    tmax = r3["forecast"]["tmax"]                 # Température maximale à 2 mètres en °C
    sun_hours = r3["forecast"]["sun_hours"]       # Ensoleillement en heures
    etp = r3["forecast"]["etp"]                   # Cumul d'évapotranspiration en mm
    probafrost = r3["forecast"]["probafrost"]     # Probabilité de gel entre 0 et 100%
    probafog = r3["forecast"]["probafog"]         # Probabilité de brouillard entre 0 et 100%
    probawind70 = r3["forecast"]["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
    probawind100 = r3["forecast"]["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
    gustx = r3["forecast"]["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h

    print("\nPrévision :  J+" + str(day))
    print("Heure locale : ", datetime)
    print("Vent moyen à 10m : ", wind10m, "km/h")
    print("Rafales de vent à 10m : ", gust10m, "km/h")
    print("Direction du vent : ", dirwind10m, "°")
    print("Cumul de pluie sur la journée: ", rr10, "mm")
    print("Cumul de pluie maximal sur la journée : ", rr1, "mm")
    print("Probabilité de pluie : ", probarain, "%")
    print("Temps : ", WEATHER[weather])
    print("Température minimale (à 2m) : ", tmin, "°C")
    print("Température maximale (à 2m) : ", tmax, "°C")
    print("Ensoleillement : ", sun_hours, "h")
    print("Evapotranspiration : ", etp, "mm")
    print("Probabilité de gel : ", probafrost, "%")
    print("Probabilité de brouillard : ", probafog, "%")
    print("Probabilité de vent >70 km/h : ", probawind70, "%")
    print("Probabilité de vent >100 km/h : ", probawind100, "%")
    print("Rafale de vent potentielle sous orage : ", gustx, "km/h")

elif(choice == '4'):
    r4 = requests.get('https://api.meteo-concept.com/api/forecast/daily/periods?token='+ api_key +'&insee='+ location +'').json()
    
    forecast = [r4['forecast'][k][0] for k in range(0,14)]

    for f in forecast:

        # forecast-period object
        insee_code = f["insee"]          # Code Insee de la commune
        postal_code = f["cp"]            # Code postal de la commune
        latitude = f["latitude"]         # Latitude décimale de la commune
        longitude = f["longitude"]       # Longitude décimale de la commune
        day = f["day"]                   # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
        period = f["period"]             # Période de la journée (Nuit : 0; Matin : 1; Après-midi : 2; Soir : 3).
        datetime = f["datetime"]         # Date en heure locale, format ISO8601
        wind10m = f["wind10m"]           # Vent moyen à 10 mètres en km/h
        gust10m = f["gust10m"]           # Rafales de vent à 10 mètres en km/h
        dirwind10m = f["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
        rr10 = f["rr10"]                 # Cumul de pluie sur la journée en mm
        rr1 = f["rr1"]                   # Cumul de pluie maximal sur la journée en mm
        probarain = f["probarain"]       # Probabilité de pluie entre 0 et 100%
        weather = f["weather"]           # Temps sensible (Code temps) – Voir Annexes
        probafrost = f["probafrost"]     # Probabilité de gel entre 0 et 100%
        probafog = f["probafog"]         # Probabilité de brouillard entre 0 et 100%
        probawind70 = f["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
        probawind100 = f["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
        gustx = f["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h
        update = r4["update"]            # Chaîne de caractère donnant la date de la prévision (au format ISO8601)

        print("\nPrévision :  J+" + str(day))
        print("Période : ", period)
        if(period == 0):
            period = 'Nuit'
        elif(period == 1):
            period = 'Matin'
        elif(period == 2):
            period = 'Après-midi'
        else:
            period = 'Soir'
        print("Heure de mise à jour : ", update)
        print("Heure locale : ", datetime)
        print("Vent moyen à 10m : ", wind10m, "km/h")
        print("Rafales de vent à 10m : ", gust10m, "km/h")
        print("Direction du vent : ", dirwind10m, "°")
        print("Cumul de pluie sur la journée: ", rr10, "mm")
        print("Cumul de pluie maximal sur la journée : ", rr1, "mm")
        print("Probabilité de pluie : ", probarain, "%")
        print("Temps : ", WEATHER[weather])
        print("Probabilité de gel : ", probafrost, "%")
        print("Probabilité de brouillard : ", probafog, "%")
        print("Probabilité de vent >70 km/h : ", probawind70, "%")
        print("Probabilité de vent >100 km/h : ", probawind100, "%")
        print("Rafale de vent potentielle sous orage : ", gustx, "km/h")

elif(choice == '5'):
    choice_day = input("\nChoisir le jour (entre 0 et 13) : ")
    r5 = requests.get('https://api.meteo-concept.com/api/forecast/daily/' + choice_day+ '/periods?token='+ api_key +'&insee='+ location +'').json()

    forecast = [r5['forecast'][k] for k in range(0,4)]

    for f in forecast:

        # forecast-period object
        insee_code = f["insee"]          # Code Insee de la commune
        postal_code = f["cp"]            # Code postal de la commune
        latitude = f["latitude"]         # Latitude décimale de la commune
        longitude = f["longitude"]       # Longitude décimale de la commune
        day = f["day"]                   # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
        period = f["period"]             # Période de la journée (Nuit : 0; Matin : 1; Après-midi : 2; Soir : 3).
        if(period == 0):
            period = 'Nuit'
        elif(period == 1):
            period = 'Matin'
        elif(period == 2):
            period = 'Après-midi'
        else:
            period = 'Soir'
        datetime = f["datetime"]         # Date en heure locale, format ISO8601
        wind10m = f["wind10m"]           # Vent moyen à 10 mètres en km/h
        gust10m = f["gust10m"]           # Rafales de vent à 10 mètres en km/h
        dirwind10m = f["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
        rr10 = f["rr10"]                 # Cumul de pluie sur la journée en mm
        rr1 = f["rr1"]                   # Cumul de pluie maximal sur la journée en mm
        probarain = f["probarain"]       # Probabilité de pluie entre 0 et 100%
        weather = f["weather"]           # Temps sensible (Code temps) – Voir Annexes
        probafrost = f["probafrost"]     # Probabilité de gel entre 0 et 100%
        probafog = f["probafog"]         # Probabilité de brouillard entre 0 et 100%
        probawind70 = f["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
        probawind100 = f["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
        gustx = f["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h
        update = r5["update"]            # Chaîne de caractère donnant la date de la prévision (au format ISO8601)

        print("\nPrévision :  J+" + str(day))
        print("Période : ", period)
        print("Heure de mise à jour : ", update)
        print("Heure locale : ", datetime)
        print("Vent moyen à 10m : ", wind10m, "km/h")
        print("Rafales de vent à 10m : ", gust10m, "km/h")
        print("Direction du vent : ", dirwind10m, "°")
        print("Cumul de pluie sur la journée: ", rr10, "mm")
        print("Cumul de pluie maximal sur la journée : ", rr1, "mm")
        print("Probabilité de pluie : ", probarain, "%")
        print("Temps : ", WEATHER[weather])
        print("Probabilité de gel : ", probafrost, "%")
        print("Probabilité de brouillard : ", probafog, "%")
        print("Probabilité de vent >70 km/h : ", probawind70, "%")
        print("Probabilité de vent >100 km/h : ", probawind100, "%")
        print("Rafale de vent potentielle sous orage : ", gustx, "km/h")

elif(choice == '6'):
    choice_day = input("\nChoisir le jour (entre 0 et 13) : ")
    choice_period = input("Période de la journée : \n" + 
                          " 0 > Nuit \n" +
                          " 1 > Matin \n" + 
                          " 2 > Après-midi \n" + 
                          " 3 > Soir \n" + 
                          "Choix : ")
    r6 = requests.get('https://api.meteo-concept.com/api/forecast/daily/' + choice_day + '/period/' + choice_period + '?token='+ api_key +'&insee='+ location +'').json() 
    
    # forecast-period object
    insee_code = r6["forecast"]["insee"]          # Code Insee de la commune
    postal_code = r6["forecast"]["cp"]            # Code postal de la commune
    latitude = r6["forecast"]["latitude"]         # Latitude décimale de la commune
    longitude = r6["forecast"]["longitude"]       # Longitude décimale de la commune
    day = r6["forecast"]["day"]                   # Jour entre 0 et 13 (Pour le jour même : 0, pour le lendemain : 1, etc.)
    period = r6["forecast"]["period"]             # Période de la journée (Nuit : 0; Matin : 1; Après-midi : 2; Soir : 3).
    if(period == 0):
        period = 'Nuit'
    elif(period == 1):
        period = 'Matin'
    elif(period == 2):
        period = 'Après-midi'
    else:
        period = 'Soir'
    datetime = r6["forecast"]["datetime"]         # Date en heure locale, format ISO8601
    wind10m = r6["forecast"]["wind10m"]           # Vent moyen à 10 mètres en km/h
    gust10m = r6["forecast"]["gust10m"]           # Rafales de vent à 10 mètres en km/h
    dirwind10m = r6["forecast"]["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
    rr10 = r6["forecast"]["rr10"]                 # Cumul de pluie sur la journée en mm
    rr1 = r6["forecast"]["rr1"]                   # Cumul de pluie maximal sur la journée en mm
    probarain = r6["forecast"]["probarain"]       # Probabilité de pluie entre 0 et 100%
    weather = r6["forecast"]["weather"]           # Temps sensible (Code temps) – Voir Annexes
    probafrost = r6["forecast"]["probafrost"]     # Probabilité de gel entre 0 et 100%
    probafog = r6["forecast"]["probafog"]         # Probabilité de brouillard entre 0 et 100%
    probawind70 = r6["forecast"]["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
    probawind100 = r6["forecast"]["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
    gustx = r6["forecast"]["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h
    update = r6["update"]                         # Chaîne de caractère donnant la date de la prévision (au format ISO8601)

    print("\nPrévision : J+" + str(day))
    print("Période :", period)
    print("Heure de mise à jour :", update)
    print("Heure locale :", datetime)
    print("Vent moyen à 10m :", wind10m, "km/h")
    print("Rafales de vent à 10m :", gust10m, "km/h")
    print("Direction du vent :", dirwind10m, "°")
    print("Cumul de pluie sur la journée:", rr10, "mm")
    print("Cumul de pluie maximal sur la journée :", rr1, "mm")
    print("Probabilité de pluie :", probarain, "%")
    print("Temps :", WEATHER[weather])
    print("Probabilité de gel :", probafrost, "%")
    print("Probabilité de brouillard :", probafog, "%")
    print("Probabilité de vent >70 km/h :", probawind70, "%")
    print("Probabilité de vent >100 km/h: ", probawind100, "%")
    print("Rafale de vent potentielle sous orage: ", gustx, "km/h")

elif(choice == '7'):
    r7 = requests.get('https://api.meteo-concept.com/api/forecast/nextHours?token='+ api_key +'&insee='+ location +'').json()
    forecast = r7["forecast"]

    for f in forecast:

        # forecast-hour object
        insee_code = f["insee"]          # Code Insee de la commune
        postal_code = f["cp"]            # Code postal de la commune
        latitude = f["latitude"]         # Latitude décimale de la commune
        longitude = f["longitude"]       # Longitude décimale de la commune
        datetime = f["datetime"]         # Date en heure locale, format ISO8601
        rh2m = f["rh2m"]                 # Humidité à 2 mètres en %
        wind10m = f["wind10m"]           # Vent moyen à 10 mètres en km/h
        gust10m = f["gust10m"]           # Rafales de vent à 10 mètres en km/h
        dirwind10m = f["dirwind10m"]     # Direction du vent en degrés (0 à 360°)
        rr10 = f["rr10"]                 # Cumul de pluie sur la journée en mm
        rr1 = f["rr1"]                   # Cumul de pluie maximal sur la journée en mm
        probarain = f["probarain"]       # Probabilité de pluie entre 0 et 100%
        weather = f["weather"]           # Temps sensible (Code temps) – Voir Annexes
        probafrost = f["probafrost"]     # Probabilité de gel entre 0 et 100%
        probafog = f["probafog"]         # Probabilité de brouillard entre 0 et 100%
        probawind70 = f["probawind70"]   # Probabilité de vent >70 km/h entre 0 et 100%
        probawind100 = f["probawind100"] # Probabilité de vent >100 km/h entre 0 et 100%
        tsoil1 = f["tsoil1"]             # Température du sol entre 0 et 10 cm en °C
        tsoil2 = f["tsoil2"]             # Température du sol entre 10 et 40 cm en °C.
        gustx = f["gustx"]               # Rafale de vent potentielle sous orage ou grain en km/h
        iso0 = f["iso0"]                 # Altitude du isotherme 0°C en mètres
        update = r7["update"]            # Chaîne de caractère donnant la date de la prévision (au format ISO8601)   

        print("\nHeure locale : ", datetime)
        print("Heure de mise à jour : ", update)
        print("Vent moyen à 10m : ", wind10m, "km/h")
        print("Rafales de vent à 10m : ", gust10m, "km/h")
        print("Direction du vent : ", dirwind10m, "°")
        print("Cumul de pluie sur la journée: ", rr10, "mm")
        print("Cumul de pluie maximal sur la journée : ", rr1, "mm")
        print("Probabilité de pluie : ", probarain, "%")
        print("Temps : ", WEATHER[weather])
        print("Probabilité de gel : ", probafrost, "%")
        print("Probabilité de brouillard : ", probafog, "%")
        print("Probabilité de vent >70 km/h : ", probawind70, "%")
        print("Probabilité de vent >100 km/h : ", probawind100, "%")
        print("Rafale de vent potentielle sous orage : ", gustx, "km/h")
        print("Altitude du isotherme 0°C : ", iso0, "°C")
        print("Température du sol entre 0 et 10 cm : ", tsoil1, "°C")
        print("Température du sol entre 10 et 40 cm : ", tsoil2, "°C")

elif(choice == '8'):
    choice_radius = input("\nRayon de recherche en km de la station à proximité : \n" +  
                          " 5 > 5km \n" + 
                          " 10 > 10km \n" +
                          " 20 > 20km \n" +
                          " 50 > 50km \n" + 
                          "Choix : ")
    r8 = requests.get('https://api.meteo-concept.com/api/observations/around?token='+ api_key +'&insee='+ location +'&radius=' + choice_radius).json()
    (station,observation) = (r8[0][k] for k in ('station','observation'))
    
    # station object 
    name_station = station['name']         # Nom attribué à la station
    uuid = station["uuid"]                 # Identifiant de la station sous une forme d'une chaîne de 36 caractères hexadécimaux et tirets de la forme XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.
    latitude = station["latitude"]         # Latitude décimale de la station
    longitude = station["longitude"]       # Longitude décimale de la station
    elevation = station["elevation"]       # Altitude de la station (au-dessus du niveau de la mer)
    city = station["city"]                 # Commune et département d'installation de la commune (si connu)

    print("\nNom de la station :", name_station)
    print("Identifiant de la station :", uuid)
    print("Latitude :", latitude)
    print("Longitude :", longitude)
    print("Altitude :", elevation, "m")
    print("Commune :", city)

    # observation object
    time = observation["time"]                                            # Date et heure de l'observation, au format ISO8601
    print("Date et heure de l'observation :", time)

    if observation.get('outside_temperature') is not None:
        outside_temperature = observation["outside_temperature"]["value"] # Température extérieure en °C
        print("Température extérieure:", outside_temperature, observation["outside_temperature"]["unit"])

    if observation.get('barometer') is not None:
        barometer = observation["barometer"]["value"]                     # Pression atmosphérique en hPa
        print("Pression atmosphérique :", barometer, observation["barometer"]["unit"])

    if observation.get('wind_speed') is not None:
        wind_speed = observation["wind_speed"]["value"]                   # Vitesse du vent en km/h
        print("Vitesse du vent :", wind_speed, observation["wind_speed"]["unit"])

    if observation.get('wind_s') is not None:
        wind_s = observation["wind_s"]["value"]                           # Vent moyen en km/h
        print("Vent moyen :", wind_s, observation["wind_s"]["unit"])

    if observation.get('wind_10m') is not None:
        wind_10m = observation["wind_10m"]["value"]                       # Vent moyen en km/h
        print("Vent moyen à 10m:", wind_s, observation["wind_10m"]["unit"])
    
    if observation.get('windgust_s') is not None:
        windgust_speed = observation["windgust_s"]["value"]               # Vitesse des rafales du vent en km/h
        print("Vitesse des rafales de vent :", windgust_speed, observation["windgust_s"]["unit"])
    
    if observation.get('windgust_10m') is not None:
        windgust_10m = observation["windgust_10m"]["value"]               # Vitesse des rafales du vent à 10m en km/h
        print("Rafales de vents à 10m :", windgust_10m, observation["windgust_10m"]["unit"])

    if observation.get('wind_direction_s') is not None:
        wind_direction_s = observation["wind_direction_s"]["value"]       # Direction du vent moyen
        print("Direction du vent moyen :", wind_direction_s, observation["wind_direction_s"]["unit"])

    if observation.get("wind_direction") is not None:
        wind_direction = observation["wind_direction"]["value"]           # Direction du vent
        print("Direction du vent :", wind_direction, observation["wind_direction"]["unit"])

    if observation.get("outside_humidity") is not None:
        outside_humidity = observation["outside_humidity"]["value"]       # Humidité relative en %
        print("Humidité relative :", outside_humidity, observation["outside_humidity"]["unit"])

    if observation.get('rainfall') is not None:
        rainfall = observation["rainfall"]["value"]                       # Précipitations en mm
        print("Précipitations :", rainfall, observation["rainfall"]["unit"])
    
    if observation.get('dew_point') is not None:
        dewpoint = observation["dew_point"]["value"]                      # Point de rosée en °C
        print("Point de rosée :", dewpoint, observation["dew_point"]["unit"])

    if observation.get("evapotranspiration") is not None:
        evapotranspiration = observation["evapotranspiration"]["value"]   # Évapotranspiration en mm
        print("Évapotranspiration :", evapotranspiration, observation["evapotranspiration"]["unit"])

    if observation.get('global_radiation') is not None:
        solar_radiation = observation["global_radiation"]["value"]        # Rayonnement solaire en W/m2
        print("Rayonnement solaire : ", solar_radiation, observation["evapotranspiration"]["unit"])

    if observation.get('wind_chill') is not None:
        windchill = observation["wind_chill"]["value"]                    # Température ressentie
        print("Température ressentie :", windchill, observation["wind_chill"]["unit"] )
    
    if observation.get('rainrate') is not None:
        rainrate = observation["rainrate"]["value"]                       # Intensité des précipitation en mm/h
        print("Intensité des précipitations :", rainrate, observation["rainrate"]["unit"] )

    if observation.get('insolation_time') is not None:
        insolation_time = observation["insolation_time"]["value"]         # Durée d'ensoleillement en min
        print("Durée d'ensoleillement : ", insolation_time, observation["insolation_time"]["unit"])

    '''
    Note : Si la clé "insolation_time" n'existe pas, cela ne va pas générer une erreur. 
    Sans cette technique, on obtient une erreur KeyError car on essaye d'accéder à une valeur dans un dictionnaire à l'aide d'une clé qui n'existe pas. 
    En utilisant .get("MYKEY"), si la clé "MYKEY" n'existe pas, get() retourne None.
    '''