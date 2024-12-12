import requests
import json

def fetch_pokemon_data(pokemon_names):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_names}"
    response = requests.get(url)
    json_data = response.text
    pokemon_data = json.loads(json_data)
    print(pokemon_data)

fetch_pokemon_data("pikachu")
fetch_pokemon_data("bulbasaur")
fetch_pokemon_data("charmander")

def calculate_average_weight(name_1, name_2, name_3):
    response_1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name_1}")
    response_2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name_2}")
    response_3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name_3}")

    data_1 = response_1.json()
    data_2 = response_2.json()
    data_3 = response_3.json()
    print(data_1["weight"] + data_2["weight"] + data_3["weight"] / 3)

name_1 = "pikachu"
name_2 = "bulbasaur"
name_3 = "charmander"
calculate_average_weight(name_1, name_2, name_3)

