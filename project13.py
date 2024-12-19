import requests

while True:
    pokemon = input("Which Pokemon do you want to find (or type 'exit' to quit): ").strip().lower()
    
    if pokemon == 'exit':
        print("Exiting the program. Goodbye!")
        break
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    req = requests.get(url)
    
    if req.status_code == 200:
        data = req.json()
        print(f"\nName: {data['name'].capitalize()}")
        print("Abilities:")
        for ability in data['abilities']:
            print(f"- {ability['ability']['name']}")
        print("\n")
    else:
        print("Pokemon not found. Please try again.")
