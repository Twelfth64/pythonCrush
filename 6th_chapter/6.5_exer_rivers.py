bigest_rivers_and_countries = {
    'nile': 'egypt',
    'volga': 'russia',
    'nebraska': 'usa',
}

for river, country in bigest_rivers_and_countries.items():
    print(f"The {river.title()} runs through {country.title()}")


for river in bigest_rivers_and_countries.keys():
    print(f"{river.title()}")

for country in set(bigest_rivers_and_countries.values()):
    print(f"{country.title()}")

