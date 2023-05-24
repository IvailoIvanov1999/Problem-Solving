country_names = [key for key in input().split(", ")]
capitals = [value for value in input().split(", ")]

for (country_name, capital) in (zip(country_names, capitals)):
    print(f'{country_name} -> {capital}')
