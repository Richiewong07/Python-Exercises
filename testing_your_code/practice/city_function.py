
"""A collection of functions for working with cities."""

def get_city_country(city, country, population = 0):
    """Return a city,country string"""
    if population:
        return(city.title() + ", " + country.title() + ": " + population)
    else:
        return(city.title() + ", " + country.title())
