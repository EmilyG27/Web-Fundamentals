import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet["name"]
            mass = planet["mass"]
            orbit_period = planet["sideralOrbit"]
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

def find_heaviest_planet():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            mass = planet["mass"]
            mass = max(mass.values())
            name = planet["name"]
            print(f"The heaviest planet is {name} with a mass of {mass} kg.")

find_heaviest_planet()
