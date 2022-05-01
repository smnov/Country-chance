d = { line.split()[0] : int(line.split()[1]) for line in open("list_of_countries.txt") }

for key in d:
    country = input('Enter the country name: ')
    if country in d:
        chance = (d.get(country) / sum(d.values())) * 100
        print('Your chance to be born in', country, 'is', chance, '%')
    else:
        print('There is no such a country')
        continue