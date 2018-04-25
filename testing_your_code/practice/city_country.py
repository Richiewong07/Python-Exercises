from city_function import get_city_country

print("Enter 'q' at any time to quit.")

while True:
    city = input("\nEnter name of a city: ")
    if city == 'q':
        break
    country = input("Enter name of a country: ")
    if country == 'q':
        break
    population = input("Enter population: ")
    if population == 'q':
        break

    city_country = get_city_country(city, country, population)
    print("\tCity, Country, Population: " + city_country + ".")
