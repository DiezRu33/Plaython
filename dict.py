
dict = {}
for i in range(1, 15):
    dict[i] = i * 10

print(dict)

dict_v2 = { i: i *2 for i in range(1,5 )}
print(dict_v2)

import random
countries = ['col', 'mex', 'arg', 'chi']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

#short v
population_v2 = { country: random.randint(1, 100) for country in countries}
print(population_v2)


names = ['nico', 'zule', 'zeus']
ages = [12, 42, 232]

# zip une lista, list() lo convierte;
print(list(zip(names, ages)))

# short v para zip using dictionaries
new_dict = {
    name: age for (name, age) in zip(names, ages)
}

print(new_dict)