
def country_city(country, city, population=''):
    """Make formatted City, Country string."""

    if population:
        formatted_string = f"{country}, {city} - {population}"
    else:
        formatted_string = f"{country}, {city}"
    return formatted_string.title()
