#Parte 1 a)Verificacion Status Code y Contenido Esperado.
import random
import string

import requests

def test_validate_pokemon_API_response():
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(url)

    assert response.status_code == 200

def test_validate_existing_pokemon_bulbasaur():
    url = "https://pokeapi.co/api/v2/pokemon/1"
    response = requests.get(url)
    data = response.json()
    assert url is not None
    assert data["name"] == "bulbasaur"

def test_validate_existing_ivysaur():
    url = "https://pokeapi.co/api/v2/pokemon/2"
    response = requests.get(url)
    data = response.json()
    assert url is not None
    print(data["name"])
    assert data["name"] == "ivysaur"
    assert response.status_code == 200


def test_validate_existing_venusaur():
    url = "https://pokeapi.co/api/v2/pokemon/3"
    response = requests.get(url)
    data = response.json()
    assert url is not None
    print(data["name"])
    assert data["name"] == "venusaur"
    assert response.status_code == 200

def test_validate_existing_charmander():
    url = "https://pokeapi.co/api/v2/pokemon/4"
    response = requests.get(url)
    data = response.json()
    assert url is not None
    print(data["name"])
    assert data["name"] == "charmander"
    assert response.status_code == 200


def test_validate_existing_charmeleon():
    url = "https://pokeapi.co/api/v2/pokemon/5"
    response = requests.get(url)
    data = response.json()
    assert url is not None
    print(data["name"])
    assert data["name"] == "charmeleon"
    assert response.status_code == 200

def test_validate_star_wars_API_response():
    url = "https://swapi.info/"
    response = requests.get(url)

    assert response.status_code == 200

def test_validate_existing_film():
    url = "https://swapi.info/api/people/1"
    response = requests.get(url)
    data = response.json()
    assert data is not None
    assert response.status_code == 200
    assert int(data["height"]) == 172


#IDs Inexistentes
def test_validate_non_existing_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/100000"
    response = requests.get(url)
    assert response is not None
    assert response.status_code == 404

def test_validate_non_existing_film():
    url = "https://swapi.info/api/people/100000"
    response = requests.get(url)
    assert response is not None
    assert response.status_code == 404

#Esperamos un 404, ya que la API no valida el formato de lo enviado en la request,
# y devuelve not found, quise elegir la letra de forma random.
def test_validate_invalid_format():
    letter = random.choice(string.ascii_letters)
    url = f"https://swapi.info/api/people/{letter}"
    response = requests.get(url)
    assert response is not None
    assert response.status_code == 404


#Comparar altura promedio de Pokémon de tipo "dragon", con la de los personajes de Star Wars raza “wookiee”
#1 - Obtenemos los nombres de los pokemones de tipo fuego y la cantidad de los mismos, por cada nombre de pokemon que obtengamos
#hacemos una request y obtenemos la altura de ese pokemon y las sumamos, luego dividimos altura de pokemons sobre cantidad de pokemons

def get_average_height() -> float:
    url = "https://pokeapi.co/api/v2/type/fire"
    response = requests.get(url)
    data = response.json()
    pokemons = data["pokemon"]
    quantity = 0
    total_height = 0
    for entry in pokemons:
        quantity += 1
        url = entry["pokemon"]["url"]
        response = requests.get(url)
        data = response.json()
        total_height += data["height"]
    average_height = total_height / quantity
    return round(average_height, 2)


def test_average_pokemon_height():
    height = get_average_height()
    assert height == 28.43