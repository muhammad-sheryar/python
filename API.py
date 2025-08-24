#Python How to Connect API Using Python


import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    
    url = f"{base_url}/pokemon/{name}"
    
    response = requests.get(url)
    
    # print(response)
    
    if response.status_code == 200:
        # print("Data Retrieved!")
        
        pokemon_data = response.json()
        # print(pokemon_data)
        return pokemon_data
    
        
    else:
        print(f"Failed to Retrieved Data {response.status_code}!")

pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")