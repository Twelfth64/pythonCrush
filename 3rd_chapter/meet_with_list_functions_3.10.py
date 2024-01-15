
def country_list_reader():
    country_list_in_string = ''
    counter = 0
    for country in countries_for_visit:
        country_list_in_string += country
        if counter == len(countries_for_visit) - 1:
            pass
        else:
            country_list_in_string += ', '
            counter += 1

    print(country_list_in_string)


countries_for_visit = ['Japan', 'Poland', 'Norway', 'Iceland', 'Canada']

print('In this program I\'ll meet you with countries I\'m gonna visit and in the same moment '
      'I\'ll use all possible list methods')

print("So, I'm gonna visit " + str(len(countries_for_visit)) + " countries")

print("I still don't know in what order I will do it")
print("Maybe in the following order")
print(sorted(countries_for_visit))
print("Maybe in this one")

countries_for_visit.reverse()

country_list_reader()

print("Or maybe I will choose alphabetic order")
countries_for_visit.sort()
country_list_reader()

last_country_in_the_list = countries_for_visit.pop()

print(f"In case I can't visit some countries by some reasons I will remove it from the list, "
      f"like {last_country_in_the_list}")

print("Or I always can add some extra countries. In the end of my list")
countries_for_visit.append('Turkey')
country_list_reader()
countries_for_visit.remove('Turkey')
print("Or in the middle of my list")
countries_for_visit.insert(3, 'Thailand')
country_list_reader()
del countries_for_visit[3]
print("And don't forget that we can choose our plans if we want it")
countries_for_visit[0] = 'Sweden'
country_list_reader()



