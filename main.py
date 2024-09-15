import requests
import json
every_pokemon_data = {}

a = int(input("Enter the number of the pokemond data you want: ")) 


for i in range(1, a+1):  
    url = "https://pokeapi.co/api/v2/pokemon/" + str(i)  
    response = requests.get(url)  
    data = response.json() 
    poke_name = data['name'] 
    stats = {}  
    for stat in data['stats']:  
        stat_name = stat['stat']['name']
        base_stat = stat['base_stat'] 
        if stat_name in ['hp', 'attack','special-attack', 'defense','special-defense','speed']:  
            stats[stat_name] = base_stat  
    every_pokemon_data[poke_name] = stats  


with open('poke.json', 'w') as file:
    json.dump(every_pokemon_data, file, indent=4)

print("Sucessfully fetched thed data") 


b = input('Enter the name of the Pokémon, whose data you want: ').lower()

with open('poke.json', 'r') as file:
    data = json.load(file)

for stat_name, stat_value in data[b].items():
    print(f"{stat_name()}: {stat_value}")


# testing the changes
